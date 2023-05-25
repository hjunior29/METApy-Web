import random
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import func
import text

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

def algorithms_setup():
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    instances = ["Instance 1", "Instance 2", "Instance 3", "Instance 4", "Instance 5", "Custom"]
    selected_instance = st.selectbox("Instance", instances)
    if selected_instance == "Instance 1":
        st.markdown(
        """
        | Nome da Instância | Número de Objetos | Capacidade (c_max) | Ótimo    |
        |-------------------|-------------------|--------------------|----------|
        | F1-LOWKP-10D      | 10                | 269                | 29 5     |
        | F2-LOWKP-20D      | 20                | 878                | 1024     |
        | F3-LOWKP-4D       | 4                 | 20                 | 35       |
        | F4-LOWKP-4D       | 4                 | 11                 | 23       |
        | F5-LOWKP-15D      | 15                | 375                | 48,10694 |
        | F6-LOWKP-10D      | 10                | 60                 | 52       |
        | F7-LOWKP-7D       | 7                 | 50                 | 107      |
        | F8-LOWKP-23D      | 23                | 10000              | 9767     |
        | F9-LOWKP-5D       | 5                 | 80                 | 130      |
        | F10-LOWKP-20D     | 20                | 879                | 1025     |
        """
        )
    elif selected_instance == "Custom":
        st.markdown("Faça o upload do seu arquivo abaixo:")
        uploaded_file = st.file_uploader("Selecione o arquivo", type=['txt', 'csv', 'json', 'xlsx'])
        if uploaded_file is not None:
            file_details = {
                "Filename": uploaded_file.name,
                "FileType": uploaded_file.type,
                "FileSize": uploaded_file.size
            }
            st.write(file_details)

            # Exibir o conteúdo do arquivo (assumindo que é um arquivo de texto)
            st.text(uploaded_file.getvalue())
    if st.button ("Play"):
        st.markdown(
        """
        Run algorithm
        """
        )
    else:
        pass
    st.markdown(
    """
    ## Report results
    ### etc...
    """
    )
def instance_setup():
    instance = ["","Instance 1", "Instance 2", "Instance 3", "Instance Custom"]
    selected_instance = st.selectbox("Selecione:", instance)

    if selected_instance == "Instance 1":
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

    elif selected_instance == "Instance 2":
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

    elif selected_instance == "Instance 3":
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

    elif selected_instance == "Instance Custom":

        df = pd.DataFrame(
            [
                {
                    "Objeto $i$": 1,
                    "Peso $P_i$": 55,
                    "Valor $V_i$": 95
                },
                {
                    "Objeto $i$": 2,
                    "Peso $P_i$": 10,
                    "Valor $V_i$": 4
                },
                {
                    "Objeto $i$": 3,
                    "Peso $P_i$": 47,
                    "Valor $V_i$": 60
                },
                {
                    "Objeto $i$": 4,
                    "Peso $P_i$": 5,
                    "Valor $V_i$": 32
                },
                {
                    "Objeto $i$": 5,
                    "Peso $P_i$": 4,
                    "Valor $V_i$": 23
                },
                {
                    "Objeto $i$": 6,
                    "Peso $P_i$": 50,
                    "Valor $V_i$": 72
                },
                {
                    "Objeto $i$": 7,
                    "Peso $P_i$": 8,
                    "Valor $V_i$": 80
                },
                {
                    "Objeto $i$": 8,
                    "Peso $P_i$": 61,
                    "Valor $V_i$": 62
                },
                {
                    "Objeto $i$": 9,
                    "Peso $P_i$": 85,
                    "Valor $V_i$": 65
                },
                {
                    "Objeto $i$": 10,
                    "Peso $P_i$": 87,
                    "Valor $V_i$": 46
                },
            ]
        )
        edited_df = st.experimental_data_editor(df, num_rows=0)
    text.selected_genetic_algorithms()