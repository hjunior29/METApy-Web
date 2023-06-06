from ALGORITHMS import *

def KP_INSTANCES_SETUP(ALGORITHM):
    INSTANCE = ["Selecione a instância","F1-LOWKP-10D", "F2-LOWKP-20D", "F3-LOWKP-4D", "F4-LOWKP-4D", "F5-LOWKP-15D", "F6-LOWKP-10D", "F7-LOWKP-7D", "F8-LOWKP-23D","F9-LOWKP-5D", "F10-LOWKP-20D", "Instance Custom"]
    SELECTED_INSTANCE = st.selectbox("Selecione:", INSTANCE)

    if SELECTED_INSTANCE == "F1-LOWKP-10D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...


    elif SELECTED_INSTANCE == "F2-LOWKP-20D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F3-LOWKP-4D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 9          | 6           |
            | 2          | 11         | 5           |
            | 3          | 13         | 9           |
            | 4          | 15         | 7           |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F4-LOWKP-4D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 6          | 2           |
            | 2          | 10         | 4           |
            | 3          | 12         | 6           |
            | 4          | 13         | 7           |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F5-LOWKP-15D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F6-LOWKP-10D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F7-LOWKP-7D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F8-LOWKP-23D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F9-LOWKP-5D":
        st.markdown("""
            | Objeto $i$ | Peso $P_i$ | Valor $V_i$ |
            |------------|------------|-------------|
            | 1          | 33         | 15          |
            | 2          | 24         | 20          |
            | 3          | 36         | 17          |
            | 4          | 37         | 8           |
            | 5          | 12         | 31          |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "F10-LOWKP-20D":
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
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    elif SELECTED_INSTANCE == "Instance Custom":

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

        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
         OUTRO(SELECTED_INSTANCE)
        # elif ...

    # add more instances

    return SELECTED_INSTANCE

def PORTFOLIO_INSTANCES_SETUP(ALGORITHM):
    INSTANCE = ["Selecione a instância", "Conjunto de ativos 1", "Conjunto de ativos 2", "Conjunto de ativos 3", "Custom"]
    SELECTED_INSTANCE = st.selectbox("Selecione:", INSTANCE)

    if SELECTED_INSTANCE == "Conjunto de ativos 1":
        st.markdown("""
            | Empresa                 | Símbolo   |
            |-------------------------|-----------|
            |WEG S.A.                 | WEGE3.SA  |
            |Lojas Renner S.A.        | LREN3.SA  | 
            |Vale S.A.                | VALE3.SA  | 
            |Petróleo Brasileiro S.A. | PETR4.SA  |
            |Equatorial Energia S.A.  | EQTL3.SA  |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    if SELECTED_INSTANCE == "Conjunto de ativos 2":
        st.markdown("""
            | Empresa                  | Símbolo   |
            |--------------------------|-----------|
            |Engie Brasil Energia S.A. | EGIE3.SA  |
            |Magazine Luiza S.A.       | MGLU3.SA  | 
            |Ambev S.A.                | ABEV3.SA  | 
            |Banco Bradesco S.A.       | BBDC3.SA  |
            |NIKE, Inc.                | NIKE34.SA |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    if SELECTED_INSTANCE == "Conjunto de ativos 3":
        st.markdown("""
            | Empresa                  | Símbolo   |
            |--------------------------|-----------|
            |C&A Modas S.A.            | CEAB3.SA  |
            |Itaúsa S.A.               | ITSA4.SA  | 
            |Atacadão S.A.             | CRFB3.SA  | 
            |Sony Group Corporation    | SNEC34.SA |
            |Nu Holdings Ltd.          | NUBR33.SA |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...

    if SELECTED_INSTANCE == "Custom":
        st.markdown("""
            | Empresa                 | Símbolo   |
            |-------------------------|-----------|
            |WEG S.A.                 | WEGE3.SA  |
            |Lojas Renner S.A.        | LREN3.SA  | 
            |Vale S.A.                | VALE3.SA  | 
            |Petróleo Brasileiro S.A. | PETR4.SA  |
            |Equatorial Energia S.A.  | EQTL3.SA  |
        """)
        if ALGORITHM == "Firefly":
            FIREFLY(SELECTED_INSTANCE)
        elif ALGORITHM == "Outro":
            OUTRO(SELECTED_INSTANCE)
        # elif ...