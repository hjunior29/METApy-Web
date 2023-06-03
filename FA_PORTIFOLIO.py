from META_TOOLBOX import *
import streamlit as st

def FIREFLY():
    USER_INSTANCE = 'USA-1'
    D = PORTIFOLIO_DIMENSION(USER_INSTANCE)
    STOCKS, START_DAY, END_DAY, RISK_FREE_ASSET = PORTIFOLIO_TICKERS(USER_INSTANCE)

    # Input variables portifolio problem
    PORTIFOLIO_RETURNS, PORTIFOLIO_RISKS = STOCKS_RISK_AND_RETURN(STOCKS, START_DAY, END_DAY)

    # Design space
    X_L = [0.00001] * D
    X_U = [0.99999] * D

    # Setup FA method 
    GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)
    PARAMETERS = {
                'ATTRACTIVENESS (BETA_0)': 0.98,
                'MIN. RANDOM FACTOR (ALPHA_MIN)': 0.20,
                'MAX. RANDOM FACTOR (ALPHA_MAX)': 0.95,
                'LIGHT ABSORPTION (GAMMA)': GAMMA,
                'THETA': 0.98,
                'TYPE ALPHA UPDATE': 'YANG 0',
                'SCALING (S_D)': True
                }
                
    # Setup optimization
    SETUP_FA = { 
                'N_REP': 30,
                'N_ITER': 50, #500
                'N_POP': 20,
                'D': D,
                'X_L': X_L,
                'X_U': X_U,
                'PARAMETERS': PARAMETERS,
                'NULL_DIC': {'RETURN': PORTIFOLIO_RETURNS, 'RISK': PORTIFOLIO_RISKS, 'RISK_FREE': RISK_FREE_ASSET, 'RP': 1E6}
                }

    # OF Statement
    def OF_FUNCTION(X, NULL_DIC):
        RET, VOL = PORTIFOLIO(X, NULL_DIC['RISK'], NULL_DIC['RETURN'])
        OF = SHARP(RET, VOL, NULL_DIC['RISK_FREE'])     
        OF *= -1  
        G_0 = sum(X) - 1
        PSEUDO_OF = OF + (G_0 ** 2) * NULL_DIC['RP']
        return PSEUDO_OF

    def OF_FUNCTION_AUX(X, NULL_DIC):
        RET, VOL = PORTIFOLIO(X, NULL_DIC['RISK'], NULL_DIC['RETURN'])
        SHARP_INDEX = SHARP(RET, VOL, NULL_DIC['RISK_FREE'])     
        SUMA = sum(X)
        G_0 = sum(X) - 1
        return RET, VOL, SHARP_INDEX, SUMA, G_0
        
    # Optimization
    RESULTS_REP_FA, BEST_REP_FA, AVERAGE_REP_FA, WORST_REP_FA, SATUS_FA = FIREFLY_ALGORITHM_001(OF_FUNCTION, SETUP_FA)
    # Best dimension
    BESTBEST_FA = SATUS_FA[0]
    BEST = BEST_REP_FA[BESTBEST_FA]
    DIMENSIONS = list(BEST['X_POSITION'][-1,:])

    # Best Result and Cost
    RET, VOL, SHARP_INDEX, SUMA, G_0 = OF_FUNCTION_AUX(DIMENSIONS, SETUP_FA['NULL_DIC'])

    # Print
#print('\n Optimization results:', '\n')
#print(' - Design Variables: ', [f'{TIC}: {100 * PERC:.2f} %' for TIC, PERC in zip(STOCKS, DIMENSIONS)])
#print(' - Sharp index:    {:.2f}'.format(SHARP_INDEX), '\n',
 #     '- Risk free (%):  {:.2f}'.format(RISK_FREE_ASSET * 100), '\n',
  #    '- Return (%):     {:.2f}'.format(RET * 100), '\n',
   #   '- Risk (%):       {:.2f}'.format(VOL * 100), '\n',
    #  '- Constrain:      {:.6e}'.format(G_0), '\n',
    #  '- sum(x):         {:.6e}'.format(SUMA))
    st.subheader('Optimization results:')

    st.write('- Design Variables:', [f'{TIC}: {100 * PERC:.2f} %' for TIC, PERC in zip(STOCKS, DIMENSIONS)])
    st.write('- Sharp index:    {:.2f}'.format(SHARP_INDEX))
    st.write('- Risk free (%):  {:.2f}'.format(RISK_FREE_ASSET * 100))
    st.write('- Return (%):     {:.2f}'.format(RET * 100))
    st.write('- Risk (%):       {:.2f}'.format(VOL * 100))
    st.write('- Constrain:      {:.6e}'.format(G_0))
    st.write('- sum(x):         {:.6e}'.format(SUMA))
