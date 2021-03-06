from numpy import einsum, zeros
from objects.fields.tensorfield import TensorField
from objects.grtensors.christoffelsymbol import ChristoffelSymbol
from objects.grtensors.metrictensor import MetricTensor
from objects.simplifyobjects import Simplify
from sympy import Array, MutableDenseNDimArray, diff


class VectorField():
    def __init__(self, metric_tensor, coord_sys, vector_field, vector_field_type):
        """
        Creating the vector field object

        Args:
            metric_tensor [list]: The metric tensor, provided by the user
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
            vector_field [list]: The vector field, provided by the user
            vector_field_type [str]: Type of the vector field. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)
        """
        self.metric_obj = metric_tensor
        self.coord_sys = coord_sys
        self.vector_field = vector_field
        self.vector_field_type = vector_field_type
        self.ndim = len(coord_sys)

    def get_vectorfield(self):
        """
        Returns the vector field object
        """
        return Simplify(self.vector_field)

    def get_vectorfield_type(self):
        """
        Returns the type of the vector field
        """
        return self.vector_field_type

    def cal_covariant_derivative(self, index):
        """
        The covariant derivative of a vector field for a given type and index

        Args:
            index [int]: The index of the coordinate system given as an integer; (0-ndim)
        """
        cs = ChristoffelSymbol(self.metric_obj, self.coord_sys)
        chris_symbol = cs.get_christoffelsymbol()
        cd_vector_field = []
        if self.vector_field_type == 'u':
            for a in range(self.ndim):
                V_partial = diff(self.vector_field[a], self.coord_sys[index])
                einstein_sum = 0
                for b in range(self.ndim):
                    einstein_sum += chris_symbol[a,
                                                 index, b]*self.vector_field[b]
                cov_V = V_partial + einstein_sum
                cd_vector_field.append(cov_V)

        elif self.vector_field_type == 'd':
            for a in range(self.ndim):
                V_partial = diff(self.vector_field[a], self.coord_sys[index])
                einstein_sum = 0
                for b in range(self.ndim):
                    einstein_sum += chris_symbol[b,
                                                 index, a]*self.vector_field[b]
                cov_V = V_partial - einstein_sum
                cd_vector_field.append(cov_V)
        return Simplify(Array(cd_vector_field))

    def cal_lie_derivative(self, X):
        """
        The lie derivative of a vector field with respect to another vector field, X

        Args:
            X [list]: Given vector field that the lie derivative is taken w.r.t
        """
        ld_vector_field = []
        if self.vector_field_type == 'u':
            for a in range(self.ndim):
                einstein_sum = 0
                for c in range(self.ndim):
                    einstein_sum += X[c]*diff(self.vector_field[a], self.coord_sys[c]) - \
                        self.vector_field[c]*diff(X[a], self.coord_sys[c])
                ld_vector_field.append(einstein_sum)

        elif self.vector_field_type == 'd':
            for a in range(self.ndim):
                einstein_sum = 0
                for c in range(self.ndim):
                    einstein_sum += X[c]*diff(self.vector_field[a], self.coord_sys[c]) + \
                        self.vector_field[c]*diff(X[c], self.coord_sys[a])
                ld_vector_field.append(einstein_sum)
        return Simplify(Array(ld_vector_field))

    def isKillingField(self, xvector_field):
        """
        Checking if a giving vector field with type (1,0) is a killing field or not
        """
        g = TensorField(self.metric_obj, self.coord_sys, self.metric_obj, 'dd')
        if g.cal_lie_derivative(xvector_field) == MutableDenseNDimArray(zeros((4,)*2)):
            return True
        return False

    def vary_vectorfield_type(self, xvector_field, new_type):
        """
        Varying the type of the vector field

        Args:
            xvector_field [list]: Given vector field
            new_type [str]: The new type of the vector field. It should be given
            in terms of 'u': contravariant (upper-indices) and 'd': covariant (lower-indices)

        Returns:
            The new vector field for a given type
        """
        self.vector_field_type = new_type
        if new_type == 'u':
            mt = MetricTensor(self.metric_obj, self.coord_sys)
            inverse_metric = mt.get_inverse()
            return Simplify(Array(einsum('ij,i->j', inverse_metric, xvector_field, optimize='optimal')))
        elif new_type == 'd':
            return Simplify(Array(einsum('ij,i->j', self.metric_obj, xvector_field, optimize='optimal')))
