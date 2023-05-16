import random
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.image("images/META_logo.png", width=150)

st.markdown("""

# Knapsack Problem

Imagine que você tenha uma mochila com capacidade limitada de peso e um conjunto de itens, cada um com seu próprio valor e peso. O objetivo do problema da mochila é determinar quais itens devem ser incluídos na mochila de forma que a soma total dos valores seja maximizada, sem exceder a capacidade de peso da mochila. Vale ressaltar que cada item pode ser incluído apenas uma vez na mochila.

## Fórmula

Dado um conjunto de n itens, cada um com peso p_i e valor v_i, e uma mochila com capacidade máxima W, nosso objetivo é encontrar uma solução x = (x_1, x_2, ..., x_n) que maximize a função objetivo:

""")

st.markdown("## Escolha o algoritmo para resolver o problema:")

algorithms = ["Algoritmo Genético", "Algoritmo de Enxame de Partículas", "Otimização de Colônia de Formigas", "Simulated Annealing"]
selected_algorithm = st.selectbox("Algoritmo", algorithms)

if selected_algorithm == "Algoritmo Genético":
    st.markdown(
    """
    # Algoritmo Genético
    """
    )

elif selected_algorithm == "Algoritmo de Enxame de Partículas":
    st.markdown(
    """
    # Algoritmo de Enxame de Partículas
    Particle Swarm Optimization:
     O funcionamento se dá pela evolução de um enxame aleatório de indivíduos dispostos em um espaço d-dimensional, que a cada iteração, são atualizados de acordo com a melhor Função Objetivo (OF) individual valor e grupo. Assim, o algoritmo PSO é estruturado em dois princípios para o movimento de partículas. A primeira refere-se à influência do grupo sobre cada indivíduo e a segunda cria um tipo de memória em cada indivíduo do enxame.
    """
    )
    st.markdown(
    """
    ## Setup
    O funcionamento se dá pela evolução de um enxame aleatório de indivíduos dispostos em um espaço d-dimensional, que a cada iteração, são atualizados de acordo com a melhor Função Objetivo (OF) individual valor e grupo. Assim, o algoritmo PSO é estruturado em dois princípios para o movimento de partículas. A primeira refere-se à influência do grupo sobre cada indivíduo e a segunda cria um tipo de memória em cada indivíduo do enxame.
    """
    )
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
elif selected_algorithm == "Otimização de Colônia de Formigas":
    st.markdown(
    """
    # Otimização de Colônia de Formigas
    """
    )
elif selected_algorithm == "Simulated Annealing":
    st.markdown(
    """
    # Simulated Annealing
    """
    )


















# st.markdown("Faça o upload do seu arquivo abaixo:")
# uploaded_file = st.file_uploader("Selecione o arquivo", type=['txt', 'csv', 'json', 'xlsx'])
# if uploaded_file is not None:
#     file_details = {
#         "Filename": uploaded_file.name,
#         "FileType": uploaded_file.type,
#         "FileSize": uploaded_file.size
#     }
#     st.write(file_details)
#
#     # Exibir o conteúdo do arquivo (assumindo que é um arquivo de texto)
#     st.text(uploaded_file.getvalue())

