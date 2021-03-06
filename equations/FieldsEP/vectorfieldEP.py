#---------- PRODUCING EQUATIONS OF VECTOR FIELD ----------#

from objects.fields.vectorfield import VectorField
from sympy import latex


def cd_vectorfield10_ep(metric_tensor, coord_sys, vector_field, index_symbol):
    """
    Producing equations of covariant derivative for type (1,0) vector field

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field [list]: The vector field, provided by the user
        index_symbol [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(vf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}V^{{\\alpha}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}V^{{a}} = {1}$$'.format(cd_component, cd_eqn)


def ld_vectorfield10_ep(metric_tensor, coord_sys, vector_field, X):
    """
    Producing equations of lie derivative of type (1,0) vector field with respect to another vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field [list]: The vector field, provided by the user
        X [list]: Given vector field that the lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    ld_eqn = latex(vf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XV^{{\\alpha}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XV^{{a}} = {0}$$'.format(ld_eqn)


def cd_vectorfield01_ep(metric_tensor, coord_sys, vector_field, index_symbol):
    """
    Producing equations of covariant derivative for type (0,1) vector field

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field [list]: The vector field, provided by the user
        index_symbol [sympy.symbol]: The index of the coordinate system given as a symbol (e.g., t, r, theta or phi)
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    index_int = coord_sys.index(index_symbol)
    cd_component = latex(index_symbol)
    cd_eqn = latex(vf.cal_covariant_derivative(index_int))
    if ndim == 4:
        return '$$\\nabla_{{{0}}}V_{{\\alpha}} = {1}$$'.format(cd_component, cd_eqn)
    elif ndim == 3:
        return '$$\\nabla_{{{0}}}V_{{a}} = {1}$$'.format(cd_component, cd_eqn)


def ld_vectorfield01_ep(metric_tensor, coord_sys, vector_field, X):
    """
    Producing equations of lie derivative of type (0,1) vector field with respect to another vector field, X

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field [list]: The vector field, provided by the user
        X [list]: Given vector field that the lie derivative is taken w.r.t
    """
    ndim = len(coord_sys)
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    ld_eqn = latex(vf.cal_lie_derivative(X))
    if ndim == 4:
        return '$$\mathcal{{L}}_XV_{{\\alpha}} = {0}$$'.format(ld_eqn)
    elif ndim == 3:
        return '$$\mathcal{{L}}_XV_{{a}} = {0}$$'.format(ld_eqn)


def killingfield10_ep(metric_tensor, coord_sys, vector_field):
    """
    Producing equation of a killing field for type (1,0) vector field

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field [list]: The vector field, provided by the user
    """
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'u')
    if vf.isKillingField(vector_field) == True:
        return '$$V^{{\\alpha}}={0}~\\text{{is a killing field}}$$'.format(latex(vector_field))
    else:
        return '$$V^{{\\alpha}}={0}~\\text{{is not a killing field}}$$'.format(latex(vector_field))


def killingfield01_ep(metric_tensor, coord_sys, vector_field):
    """
    Producing equation of a killing field for type (0,1) vector field

    Args:
        metric_tensor [list]: The metric tensor, provided by the user
        coord_sys [list]: The coordinate system given as a list (e.g., [t,x,y,z])
        vector_field [list]: The vector field, provided by the user
    """
    vf = VectorField(metric_tensor, coord_sys, vector_field, 'd')
    vector_field_raised = vf.vary_vectorfield_type(vector_field, 'u')
    # since the lie derivative in the killing vector equation only takes upper indices
    if vf.isKillingField(vector_field_raised) == True:
        return '$$V_{{\\alpha}}={0}~\\text{{is a killing field}}$$'.format(latex(vector_field))
    else:
        return '$$V_{{\\alpha}}={0}~\\text{{is not a killing field}}$$'.format(latex(vector_field))
