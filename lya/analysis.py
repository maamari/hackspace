import numpy as np
from .data import get_data_transfer_function
from .theory import *
from .conf import idm_params

from scipy.optimize import minimize


def model(k, sigma0):
    """Returns values of alpha-beta-gamma model at given k values

    Parameters
    ----------
    k : array

    alpha, beta, gamma : float
        Parameters of model
    """
    
    print(sigma0)
    idm_params['sigma_dmeff']=sigma0
    TkIDM = get_theory_pk(k,idm_params)/get_lcdm_pk(k)
  
    return TkIDM


def residuals(sigma0, data):
    """Returns data - model for given values of parameters

    Parameters
    ----------
    pars : array-like
        [alpha, beta, gamma] parameters.

    data : Data object (string)
        Data to be compared with model.
    """

    mod = model(data.x, sigma0)
    res = data.y-mod

    return res


def objective(pars, data):
    """Objective function to miminize
    """


    return (residuals(pars, data) ** 2 / data.y_unc ** 2).sum()


def get_best_fit():
    """Compute best-fit model parameters


    Returns
    -------
    pars : array-like
        Best-fit [alpha, beta, gamma] parameters 
    """

    data = get_data_transfer_function()
    f = lambda pars: objective(pars, data)
    res = minimize(f, (0, 7, 0))

    return res.x

