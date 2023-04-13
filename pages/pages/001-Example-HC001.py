# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# import numpy as np
import streamlit as st
from META_TOOLBOX import HILL_CLIMBING_001 # or from META_TOOLBOX import *

# +
# Input
PARAMETERS = {'PERCENTAGE STD (SIGMA)': 10.0} # equal 10%

st.markdown(
    """
    SETUP = {
        'N_REP': 10,
        'N_POP': 1,
        'N_ITER': 100,
        'X_L': [-2, -2, -2],
        'X_U': [2, 2, 2],
        'D': 3,
        'NULL_DIC': None,
        'PARAMETERS': PARAMETERS
        }
    """
)
# OF statement
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Call algorithm
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = HILL_CLIMBING_001(OF_FUNCTION, SETUP)
