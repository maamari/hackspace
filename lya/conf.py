import os

# get the lya data path
path = os.path.abspath(__file__)
lya_data_path = os.path.join(os.path.dirname(path), "..", "data", "lyman-alpha.txt")

# set up comological parameters
lcdm_params = {
    "omega_b": 0.02233,
    "omega_cdm": 0.1198,
    "h": 0.6737,
    "A_s": 2.097e-9,
    "n_s": 0.9652,
    'P_k_max_h/Mpc': 66.,
    "tau_reio": 0.0540,
}

idm_params = {
    'output': 'mPk',
    'omega_b': 0.022068,
    'omega_cdm': 0.,
    'omega_dmeff': 0.1199,
    "h": 0.6737,    
    'npow_dmeff': 0,
    'm_dmeff': 0.0001,
    'sigma_dmeff': 1e-20,
    'k_per_decade_for_pk': 30,
    'P_k_max_h/Mpc': 66.,
    'z_pk': 99
}