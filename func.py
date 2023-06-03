import streamlit as st
import os
import text
from META_TOOLBOX import *

def style_setup():
    streamlit_style = """
    <style>
        html, body, [class*="css"]  {
            text-align: justify;
        }
        /* Selecionar a barra de rolagem vertical */
        ::-webkit-scrollbar {
            width: 12px;
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
        firefly(selected_instance)


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
        firefly(selected_instance)

    elif selected_instance == "F3-LOWKP-4D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 9          | 6           |
            | 2          | 11         | 5           |
            | 3          | 13         | 9           |
            | 4          | 15         | 7           |
        """)
        firefly(selected_instance)

    elif selected_instance == "F4-LOWKP-4D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 6          | 2           |
            | 2          | 10         | 4           |
            | 3          | 12         | 6           |
            | 4          | 13         | 7           |
        """)
        firefly(selected_instance)

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
        firefly(selected_instance)

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
        firefly(selected_instance)

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
        firefly(selected_instance)

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
        firefly(selected_instance)

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
        firefly(selected_instance)

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
        firefly(selected_instance)

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

    return selected_instance


def get_latest_file(path):
    # Get a list of all files in the directory
    list_of_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    # Get the file with the maximum creation time (i.e., the most recent file)
    latest_file = max(list_of_files, key=lambda x: os.path.getctime(os.path.join(path, x)))
    return latest_file

def firefly(USER_INSTANCE):
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
        # file_name = EXCEL_PROCESS_RESUME(NAME, D, DATASET, N_ITER, N_REP)

        # Print
        # st.write('\n Optimization results:', '\n \n',
        #       '- Design Variables: ', X_NEW, '\n',
        #       '- Profit($): {:.6e}'.format(-BEST_RESULT), '\n',
        #       '- Cost($): {:.6e}'.format(COST), '\n',
        #       '- Constraint: {:.6e}'.format(G_0))

        latest_file = get_latest_file("./")
        st.write("The most recently created file is:", latest_file)

        st.markdown(f"""
        ## Optimization results:
        
        - Design Variables: {X_NEW}
        - Profit($): {-BEST_RESULT:.6e}
        - Cost($): {COST:.6e}
        - Constraint: {G_0:.6e}
        """)
        with open(f'{latest_file}', 'rb') as file:
            file_content = file.read()

        st.download_button(
            label="Baixar arquivo 📊",
            data=file_content,
            file_name=f'{latest_file}',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
