import numpy as np

def esi_calc(xe, x, w=0.57):
    """ The earth similar index.
    Parameters
    ----------
    x  : int
        Parameter value of the exoplanet
    xe : int
        Reference value (planet earth)
    w  : int
        Weighted value 

    Return
    ------
    esi : earth similarity index
    """

    esi = (1 - np.abs((xe - x)/(xe + x))**w

    return(esi)
