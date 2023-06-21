from META_TOOLBOX import *
from UTILS import *

def FIREFLY(USER_INSTANCE):
    st.markdown("""
    ### Algorithms Parameters
    """)

    BETA_0 = st.number_input("ATTRACTIVENESS (BETA_0)", value=0.98, format="%0.2f")
    ALPHA_MIN = st.number_input("MIN. RANDOM FACTOR (ALPHA_MIN)", value=0.20, format="%0.2f")
    ALPHA_MAX = st.number_input("MAX. RANDOM FACTOR (ALPHA_MAX)", value=0.95, format="%0.2f")
    # GAMMA = st.text_input("LIGHT ABSORPTION (GAMMA)")
    THETA = st.number_input("THETA", value=0.98, format="%0.2f")
    # TYPE_ALPHA_UPDATE = st.text_input("TYPE ALPHA UPDATE")
    # S_D = st.checkbox("SCALING (S_D)")

    st.markdown("""
    ### Setup Algorithm
    """)
    N_REP = st.number_input("N_REP", value= 10, step=1)
    N_POP = st.number_input("N_POP", value= 100, step=1)
    N_ITER = st.number_input("N_ITER", value= 1, step=1)

    if st.button("Run"):
        # Knapsack instace selected by user
        D = KNAPSACK_DIMENSION(USER_INSTANCE)

        # Input variables knapsakc problem
        VARS = []
        for I in range(D):
            VARS.append({'X': [0, 1]})

        # Design space
        X_L = [0.0] * D
        X_U = [1.0] * D

        # Setup FA method
        GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)
        PARAMETERS = {
            'ATTRACTIVENESS (BETA_0)': BETA_0,
            'MIN. RANDOM FACTOR (ALPHA_MIN)': ALPHA_MIN,
            'MAX. RANDOM FACTOR (ALPHA_MAX)': ALPHA_MAX,
            'LIGHT ABSORPTION (GAMMA)': GAMMA,
            'THETA': THETA,
            'TYPE ALPHA UPDATE': 'YANG 0',
            'SCALING (S_D)': True
        }

        # Setup optimization
        SETUP_FA = {
            'N_REP': N_REP,
            'N_ITER': N_ITER,
            'N_POP': N_POP,
            'D': D,
            'X_L': X_L,
            'X_U': X_U,
            'PARAMETERS': PARAMETERS,
            'NULL_DIC': {'X': VARS, 'INSTANCE': USER_INSTANCE, 'R_P': 10 ** 6}
        }

        # Print Vars
        st.code(f"""
            SETUP_FA = {{
                'N_REP': {N_REP},
                'N_ITER': {N_ITER},
                'N_POP': {N_POP},
                'D': {D},
                'X_L': [-2, -2, -2],
                'X_U': [2, 2, 2],
                'PARAMETERS': {{
                    'ATTRACTIVENESS (BETA_0)': {BETA_0},
                    'MIN. RANDOM FACTOR (ALPHA_MIN)': {ALPHA_MIN},
                    'MAX. RANDOM FACTOR (ALPHA_MAX)': {ALPHA_MAX},
                    'LIGHT ABSORPTION (GAMMA)': GAMMA,
                    'THETA': {THETA},
                    'TYPE ALPHA UPDATE': 'YANG 0',
                    'SCALING (S_D)': True
                }}
                'NULL_DIC': {{
                    'X': {VARS}, 
                    'INSTANCE': {USER_INSTANCE}, 
                    'R_P': {10 ** 6}
                }}
            }}
        """)

        # OF statement and OF auxiliar
        def OF_FUNCTION(X, NULL_DIC):
            DISCRETE_DATA = NULL_DIC['X']
            D = len(DISCRETE_DATA)
            X_NEW = CONVERT_CONTINUOUS_DISCRETE(X, DISCRETE_DATA)
            _, G_0, OF = KNAPSACK(X_NEW, NULL_DIC['INSTANCE'])
            PSEUDO_OF = OF + (np.maximum(0, G_0)) * NULL_DIC['R_P']

            return PSEUDO_OF

        def OF_FUNCTION_AUX(X, NULL_DIC):
            DISCRETE_DATA = NULL_DIC['X']
            D = len(DISCRETE_DATA)
            X_NEW = CONVERT_CONTINUOUS_DISCRETE(X, DISCRETE_DATA)
            COST, G_0, OF = KNAPSACK(X_NEW, NULL_DIC['INSTANCE'])

            return COST, G_0, OF

        # Optimization
        RESULTS_REP_FA, BEST_REP_FA, AVERAGE_REP_FA, WORST_REP_FA, SATUS_FA = FIREFLY_ALGORITHM_001(OF_FUNCTION, SETUP_FA)

        # Best dimension
        BESTBEST_FA = SATUS_FA[0]
        BEST = BEST_REP_FA[BESTBEST_FA]
        DIMENSOES = list(BEST['X_POSITION'][-1,:])

        # Design variables of optimum point
        DATA_DISCRETE = SETUP_FA['NULL_DIC']['X']
        X_NEW = CONVERT_CONTINUOUS_DISCRETE(DIMENSOES, DATA_DISCRETE)

        # Best Result and Cost
        COST, G_0, BEST_RESULT = OF_FUNCTION_AUX(DIMENSOES, SETUP_FA['NULL_DIC'])

        LATEST_FILE = GET_LATEST_FILE("./")
        # st.write("The most recently created file is:", LATEST_FILE)

        st.markdown(f"""
            ## Optimization results:
            
            - Design Variables: {X_NEW}
            - Profit($): {-BEST_RESULT:.6e}
            - Cost($): {COST:.6e}
            - Constraint: {G_0:.6e}
        """)

        with open(f'{LATEST_FILE}', 'rb') as file:
            FILE_CONTENT = file.read()

        st.download_button(
            label="Download File 📊",
            data=FILE_CONTENT,
            file_name=f'{LATEST_FILE}',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )

def OUTRO(USER_INSTANCE):
    # ...
    return USER_INSTANCE
