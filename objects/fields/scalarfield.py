from objects.simplifyobjects import Simplify
from sympy import diff


class ScalarField():
    def __init__(self, coord_sys, scalar_field):
        """
        Creating the scalar field object

        Args:
            coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
            scalar_field [sympy.symbol]: The scalar field, provided by the user
        """
        self.coord_sys = coord_sys
        self.scalar_field = scalar_field
        self.ndim = len(coord_sys)

    def get_scalarfield(self):
        """
        Returns the scalar field object
        """
        return Simplify(self.scalar_field)

    def cal_covariant_derivative(self, index):
        """
        The covariant derivative of a scalar field for a given index

        Args:
            index [int]: The index of the coordinate system given as an integer; (0-ndim)
        """
        return Simplify(diff(self.scalar_field, self.coord_sys[index]))

    def cal_lie_derivative(self, X):
        """
        The lie derivative of a scalar field with respect to vector field, X

        Args:
            X [list]: Given vector field that the lie derivative is taken w.r.t
        """
        ld_scalar_field = 0
        for c in range(self.ndim):
            ld_scalar_field += X[c]*diff(self.scalar_field, self.coord_sys[c])
        return Simplify(ld_scalar_field)
