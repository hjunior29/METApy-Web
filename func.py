import numpy as np
import streamlit as st
import pandas as pd
import text
from META_TOOLBOX import *
from META_TOOLBOX.META_KNAPSACK import *


def style_setup():
    streamlit_style = """
    <style>
        html, body, [class*="css"]  {
            text-align: justify;
        }
    </style>
    """
    st.markdown(streamlit_style, unsafe_allow_html=True)

style_setup()

def instance_setup():
    instance = ["Selecione a instância","F1-LOWKP-10D", "F2-LOWKP-20D", "F3-LOWKP-4D", "F4-LOWKP-4D", "F5-LOWKP-15D", "F6-LOWKP-10D", "F7-LOWKP-7D", "F8-LOWKP-23D","F9-LOWKP-5D", "F10-LOWKP-20D", "Instance Custom"]
    selected_instance = st.selectbox("Selecione:", instance)

    if selected_instance == "F1-LOWKP-10D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 55         | 95          |
            | 2          | 10         | 4           |
            | 3          | 47         | 60          |
            | 4          | 5          | 32          |
            | 5          | 4          | 23          |
            | 6          | 50         | 72          |
            | 7          | 8          | 80          |
            | 8          | 61         | 62          |
            | 9          | 85         | 65          |
            | 10         | 87         | 46          |
        """)
        firefly()


    elif selected_instance == "F2-LOWKP-20D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 44         | 92          |
            | 2          | 46         | 4           |
            | 3          | 90         | 43          |
            | 4          | 72         | 83          |
            | 5          | 91         | 84          |
            | 6          | 40         | 68          |
            | 7          | 75         | 92          |
            | 8          | 35         | 82          |
            | 9          | 8          | 6           |
            | 10         | 54         | 44          |
            | 11         | 78         | 32          |
            | 12         | 40         | 18          |
            | 13         | 77         | 56          |
            | 14         | 15         | 83          |
            | 15         | 61         | 25          |
            | 16         | 17         | 96          |
            | 17         | 75         | 70          |
            | 18         | 29         | 48          |
            | 19         | 75         | 14          |
            | 20         | 63         | 58          |
        """)
        firefly()

    elif selected_instance == "F3-LOWKP-4D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 9          | 6           |
            | 2          | 11         | 5           |
            | 3          | 13         | 9           |
            | 4          | 15         | 7           |
        """)
        firefly()

    elif selected_instance == "F4-LOWKP-4D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 6          | 2           |
            | 2          | 10         | 4           |
            | 3          | 12         | 6           |
            | 4          | 13         | 7           |
        """)
        firefly()

    elif selected_instance == "F5-LOWKP-15D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 0.125126   | 56.358531   |
            | 2          | 19.330424  | 80.874050   |
            | 3          | 58.500931  | 47.987304   |
            | 4          | 35.029145  | 89.596240   |
            | 5          | 82.284005  | 74.660482   |
            | 6          | 17.410810  | 85.894345   |
            | 7          | 71.050142  | 51.353496   |
            | 8          | 30.399487  | 1.498459    |
            | 9          | 9.140294   | 36.445204   |
            | 10         | 14.731285  | 16.589862   |
            | 11         | 98.852504  | 44.569231   |
            | 12         | 11.908322  | 0.466933    |
            | 13         | 0.891140   | 37.788018   |
            | 14         | 53.166295  | 57.118442   |
            | 15         | 60.176397  | 60.716575   |
        """)
        firefly()

    elif selected_instance == "F6-LOWKP-10D":
        st.markdown("""
        | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
        |------------|------------|-------------|
        | 1          | 20         | 30          |
        | 2          | 18         | 25          |
        | 3          | 17         | 20          |
        | 4          | 15         | 18          |
        | 5          | 15         | 17          |
        | 6          | 10         | 11          |
        | 7          | 5          | 5           |
        | 8          | 3          | 2           |
        | 9          | 1          | 1           |
        | 10         | 1          | 1           |
    """)
        firefly()

    elif selected_instance == "F7-LOWKP-7D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 70         | 31          |
            | 2          | 20         | 10          |
            | 3          | 39         | 20          |
            | 4          | 37         | 19          |
            | 5          | 7          | 4           |
            | 6          | 5          | 3           |
            | 7          | 10         | 6           |
        """)
        firefly()

    elif selected_instance == "F8-LOWKP-23D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 981        | 983         |
            | 2          | 980        | 982         |
            | 3          | 979        | 981         |
            | 4          | 978        | 980         |
            | 5          | 977        | 979         |
            | 6          | 976        | 978         |
            | 7          | 487        | 488         |
            | 8          | 974        | 976         |
            | 9          | 970        | 972         |
            | 10         | 485        | 486         |
            | 11         | 485        | 486         |
            | 12         | 970        | 972         |
            | 13         | 970        | 972         |
            | 14         | 484        | 485         |
            | 15         | 484        | 485         |
            | 16         | 976        | 969         |
            | 17         | 974        | 966         |
            | 18         | 482        | 483         |
            | 19         | 962        | 964         |
            | 20         | 961        | 963         |
            | 21         | 959        | 961         |
            | 22         | 958        | 958         |
            | 23         | 857        | 959         |
        """)
        firefly()

    elif selected_instance == "F9-LOWKP-5D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 33         | 15          |
            | 2          | 24         | 20          |
            | 3          | 36         | 17          |
            | 4          | 37         | 8           |
            | 5          | 12         | 31          |
        """)
        firefly()

    elif selected_instance == "F10-LOWKP-20D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 91         | 84          |
            | 2          | 72         | 83          |
            | 3          | 90         | 43          |
            | 4          | 46         | 4           |
            | 5          | 55         | 44          |
            | 6          | 8          | 6           |
            | 7          | 35         | 82          |
            | 8          | 75         | 92          |
            | 9          | 61         | 25          |
            | 10         | 15         | 83          |
            | 11         | 77         | 56          |
            | 12         | 40         | 18          |
            | 13         | 63         | 58          |
            | 14         | 75         | 14          |
            | 15         | 29         | 48          |
            | 16         | 75         | 70          |
            | 17         | 17         | 96          |
            | 18         | 78         | 32          |
            | 19         | 40         | 68          |
            | 20         | 44         | 92          |
        """)
        firefly()

    elif selected_instance == "Instance Custom":

        df = pd.DataFrame(
            [
                {
                    "Objeto": 1,
                    "Peso": 0,
                    "Valor": 0
                }
            ]
        )
        edited_df = st.experimental_data_editor(df, num_rows="dynamic")
        text.firefly()

def firefly():
    st.markdown("""
    ### Algorithms Parameters
    """)
    st.code("""
    PARAMETERS = {
              'ATTRACTIVENESS (BETA_0)': 0.98,
              'MIN. RANDOM FACTOR (ALPHA_MIN)': 0.20,
              'MAX. RANDOM FACTOR (ALPHA_MAX)': 0.95,
              'LIGHT ABSORPTION (GAMMA)': GAMMA,
              'THETA': 0.98,
              'TYPE ALPHA UPDATE': 'YANG 0',
              'SCALING (S_D)': True
    }
    """)

    BETA_0 = st.number_input("ATTRACTIVENESS (BETA_0)", format="%0.2f")
    ALPHA_MIN = st.number_input("MIN. RANDOM FACTOR (ALPHA_MIN)", format="%0.2f")
    ALPHA_MAX = st.number_input("MAX. RANDOM FACTOR (ALPHA_MAX)", format="%0.2f")
    # GAMMA = st.text_input("LIGHT ABSORPTION (GAMMA)")
    THETA = st.number_input("THETA", format="%0.2f")
    # TYPE_ALPHA_UPDATE = st.text_input("TYPE ALPHA UPDATE")
    # S_D = st.checkbox("SCALING (S_D)")

    st.markdown("""
    ### Setup Algorithm
    """)
    st.code(
        """
        SETUP = {
                'N_REP': 10,
                'N_ITER': 100,
                'N_POP': 1,
                'D': 3,
                'X_L': [-2, -2, -2],
                'X_U': [2, 2, 2],
                'NULL_DIC': None,
                'PARAMETERS': PARAMETERS
        }
        """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    if st.button("Run"):
        # Knapsack instace selected by user
        USER_INSTANCE = 'F1-LOWKP-10D'
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
            'N_REP': 10,
            'N_ITER': 200,
            'N_POP': 10,
            'D': D,
            'X_L': X_L,
            'X_U': X_U,
            'PARAMETERS': PARAMETERS,
            'NULL_DIC': {'X': VARS, 'INSTANCE': USER_INSTANCE, 'R_P': 10 ** 6}
        }

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

        # Print
        st.write('\n Optimization results:', '\n \n',
              '- Design Variables: ', X_NEW, '\n',
              '- Profit($): {:.6e}'.format(-BEST_RESULT), '\n',
              '- Cost($): {:.6e}'.format(COST), '\n',
              '- Constraint: {:.6e}'.format(G_0))