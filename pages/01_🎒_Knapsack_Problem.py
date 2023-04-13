import random

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import Home

st.image("images/META_logo.png", width=150)
st.markdown("""

# Knapsack Problem

Imagine que você tenha uma mochila com capacidade limitada de peso e um conjunto de itens, cada um com seu próprio valor e peso. O objetivo do problema da mochila é determinar quais itens devem ser incluídos na mochila de forma que a soma total dos valores seja maximizada, sem exceder a capacidade de peso da mochila. Vale ressaltar que cada item pode ser incluído apenas uma vez na mochila.

## Fórmula

Dado um conjunto de n itens, cada um com peso p_i e valor v_i, e uma mochila com capacidade máxima W, nosso objetivo é encontrar uma solução x = (x_1, x_2, ..., x_n) que maximize a função objetivo:

$$f(x) = \sum_{i=1}^{n} v_i x_i$$
""")

st.markdown("## Escolha o algoritmo para resolver o problema:")

algorithms = ["Algoritmo Genético", "Algoritmo de Enxame de Partículas", "Otimização de Colônia de Formigas", "Simulated Annealing"]
selected_algorithm = st.selectbox("Algoritmo", algorithms)
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

if selected_algorithm == "Algoritmo de Enxame de Partículas":
    code = """
# Input
PARAMETERS = {'PERCENTAGE STD (SIGMA)': 10.0} # equal 10%

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

# OF statement
def OF_FUNCTION(X, NULL_DIC):
    X_0 = X[0]
    X_1 = X[1]
    X_2 = X[2]
    OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
    return OF

# Call algorithm
RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = HILL_CLIMBING_001(OF_FUNCTION, SETUP)
    """
    st.code(code, language="python")
    if st.button("Run"):
        random_number = random.randint(1, 100)
        st.write(f"Número gerado: {random_number}")
























# st.header("Exemplo Hill Climbing")
# code = """
# # import numpy as np
# from META_TOOLBOX import HILL_CLIMBING_001 # or from META_TOOLBOX import *
#
# # Input
# PARAMETERS = {'PERCENTAGE STD (SIGMA)': 10.0} # equal 10%
#
# SETUP = {
#         'N_REP': 10,
#         'N_POP': 1,
#         'N_ITER': 100,
#         'X_L': [-2, -2, -2],
#         'X_U': [2, 2, 2],
#         'D': 3,
#         'NULL_DIC': None,
#         'PARAMETERS': PARAMETERS
#         }
#
# # OF statement
# def OF_FUNCTION(X, NULL_DIC):
#     X_0 = X[0]
#     X_1 = X[1]
#     X_2 = X[2]
#     OF = X_0 ** 2 + X_1 ** 2 + X_2 ** 2
#     return OF
#
# # Call algorithm
# RESULTS_REP, BEST_REP, AVERAGE_REP, WORST_REP, STATUS_PROCEDURE = HILL_CLIMBING_001(OF_FUNCTION, SETUP)
# """
# st.code(code, language='python')
#
# # Carrega o arquivo XLSX em um DataFrame do Pandas
# arquivo_xlsx = "META_HC001_RESUME_20230412 015821.xlsx"
# dados = pd.read_excel(arquivo_xlsx)
#
# # Exibe a tabela na página
# st.dataframe(dados)


