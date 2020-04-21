from .conf import lcdm_params
from classy import Class
import numpy as np

def get_lcdm_pk(k):
    """Returns theoretical p(k) at z=0 given k values with given cosmo params

    Parameters
    ----------
    k : array-like
        k values at which to evaluate theoretical p(k)

    Returns
    -------
    Pk*norm : array
       Theoretical p(k), with proper normalization
    """

    return get_theory_pk(k, lcdm_params)


def get_theory_pk(k, params):
    """Returns theoretical p(k) at z=0 given k values with given cosmo params

    Parameters
    ----------
    k : array-like
        k values at which to evaluate theoretical p(k)
    params : dict
        Cosmological parameters to pass to Class

    Returns
    -------
    Pk*norm : array
       Theoretical p(k), with proper normalization
    """

    # initialize class
    cosmo = Class()
    cosmo.set({"output": "mPk", **params})

    # run class
    cosmo.compute()

    # calculate Pk at all k values (note the normalization for k and P_k)
    h = params["h"]
    return np.array([cosmo.pk(kk * h, 0) * h ** 3 for kk in k])
