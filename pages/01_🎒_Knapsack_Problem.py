import random
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import func
import text

st.image("images/META_logo.png", width=150)

func.style_setup()

text.knapsack_theory()

st.markdown("### Escolha o algoritmo para resolver o problema:")
algorithms = ["Selecione o metodo de otimização","Algoritmo Genético", "Algoritmo de Enxame de Partículas", "Otimização de Colônia de Formigas", "Simulated Annealing"]
selected_algorithm = st.selectbox("Selecione:", algorithms)

if selected_algorithm == "Algoritmo Genético":
    st.markdown("""
    ### Selecione a instância
    """)
    func.instance_setup()
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
elif selected_algorithm == "Otimização de Colônia de Formigas":
    st.markdown(
    """
    # Otimização de Colônia de Formigas
    """
    )
    st.markdown(
    """
    ## Setup
    """
    )

    func.algorithms_setup()
elif selected_algorithm == "Simulated Annealing":
    st.markdown(
    """
    # Simulated Annealing
    """
    )
    st.markdown(
    """
    ## Setup
    """
    )

    func.algorithms_setup()