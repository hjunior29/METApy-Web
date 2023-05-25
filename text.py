import pandas as pd
import streamlit as st
import numpy as np
import streamlit.components.v1 as components
import func

# func.style_setup()

def selected_genetic_algorithms():
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
    df_parameters = pd.DataFrame(
        [
            {
                "ATTRACTIVENESS (BETA_0)": 0.98,
                "MIN. RANDOM FACTOR (ALPHA_MIN)": 0.20,
                "MAX. RANDOM FACTOR (ALPHA_MAX)": 0.95,
                "LIGHT ABSORPTION (GAMMA)": "GAMMA",
                "THETA": 0.98,
                "TYPE ALPHA UPDATE": "YANG 0",
                "SCALING (S_D)": True
            }
        ]
    )
    edited_df_parameters = st.experimental_data_editor(df_parameters, num_rows=0)

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

    df_setup = pd.DataFrame(
        [
            {
                "N_REP":10,
                "N_ITER":100,
                "N_POP":1
            }
        ]
    )
    edited_df_setup = st.experimental_data_editor(df_setup, num_rows=0)

    if st.button ("Play"):
        st.write(edited_df_setup['N_REP'].values[0])
        st.write(edited_df_setup['N_ITER'].values[0])
        st.write(edited_df_setup['N_POP'].values[0])
        st.write(edited_df_parameters['ATTRACTIVENESS (BETA_0)'].values[0])
        st.write(edited_df_parameters['MIN. RANDOM FACTOR (ALPHA_MIN)'].values[0])
        st.write(edited_df_parameters['MAX. RANDOM FACTOR (ALPHA_MAX)'].values[0])
def knapsack_theory():
    st.markdown("""
    # Knapsack Problem
    O Problema da Mochila é um desafio em otimização combinatória que busca encontrar a melhor combinação de objetos a serem alocados em uma mochila, considerando que cada objeto possui um valor monetário e um peso, e que a mochila possui uma capacidade máxima de armazenamento representada por $c_{max}$.
    
    Para entender melhor este problema, vamos considerar um conjunto de $N$ objetos, onde cada objeto i tem um valor monetário $V_i$ e um peso $P_i$ . A solução ótima do Problema da Mochila consiste em selecionar um subconjunto desses objetos de tal forma que o valor total dos itens na mochila seja maximizado, sem exceder a capacidade máxima de armazenamento. O problema é descrito por meio da equação $(1)$ .
    Função objetivo:
    """)
    st.latex("""
    FO(x_i) = \sum_{i=1}^{N} x_i V_i \\tag{1}
    """)
    st.markdown("""
    A função objetivo $(1)$ busca maximizar o valor total dos itens selecionados para a mochila. A variável binária $x_i$ indica se o objeto $i$ foi selecionado (1) ou não (0).
    Restrições:
    """)
    st.latex("""
    \sum_{i=1}^{N} x_i P_i \leq c_{max} \\tag{2}
    """)
    st.markdown("""
    A restrição $(2)$ garante que a capacidade máxima da mochila não seja excedida. O peso total dos objetos selecionados não pode ser maior que a capacidade máxima de armazenamento $c_{max}$.
    """)
    st.latex("""
    x_i \in \{0, 1\} \quad \\forall i \in \{1, 2, ..., N\} \\tag{3}
    """)
    st.markdown("""
    Devido à sua natureza combinatória e à quantidade de variações possíveis, o Problema da Mochila é classificado como um problema NP-difícil, ou seja, um problema cuja solução exata pode ser difícil de ser encontrada em tempo hábil, especialmente para grandes conjuntos de dados. Como resultado, várias abordagens heurísticas e metaheurísticas foram desenvolvidas para encontrar soluções aproximadas e eficientes para este problema, como algoritmos genéticos, busca tabu e otimização por colônia de formigas.
    
    Além disso, o Problema da Mochila possui diversas variações, como o problema da mochila fracionária, no qual é permitido dividir os objetos e incluir apenas uma fração deles na mochila, e o problema da mochila multidimensional, que considera múltiplas restrições além do peso, como volume e quantidade disponível de cada item. Estas variações ampliam ainda mais a aplicabilidade do Problema da Mochila e o tornam uma importante área de estudo na pesquisa de otimização combinatória.
    
    As instâncias do Problema da Mochila são conjuntos de dados específicos que representam casos particulares desse problema. Cada instância é composta por um conjunto de objetos, com seus respectivos pesos e valores monetários, e uma capacidade máxima da mochila. Ao utilizar diferentes instâncias, é possível analisar o desempenho e a eficácia de diversos algoritmos de solução, incluindo heurísticas e metaheurísticas, em diferentes cenários e tamanhos de problema. Para facilitar o acesso a essas instâncias, disponibilizamos uma tabela geral com o [links de download](http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/instances_01_KP.zip). A tabela apresenta detalhes sobre cada instância, como o número de objetos, a capacidade máxima $c_{max}$ da mochila e outras informações relevante como pode ser visto abaixo:
    
    **Tabela 1**: Low-dimensional 0/1 knapsack problems.
    | Nome da Instância | Número de Objetos | Capacidade $c_{max}$ | Ótimo    |
    |-------------------|-------------------|----------------------|----------|
    | F1-LOWKP-10D      | 10                | 269                  | 29.5     |
    | F2-LOWKP-20D      | 20                | 878                  | 1024     |
    | F3-LOWKP-4D       | 4                 | 20                   | 35       |
    | F4-LOWKP-4D       | 4                 | 11                   | 23       |
    | F5-LOWKP-15D      | 15                | 375                  | 481.0694 |
    | F6-LOWKP-10D      | 10                | 60                   | 52       |
    | F7-LOWKP-7D       | 7                 | 50                   | 107      |
    | F8-LOWKP-23D      | 23                | 10000                | 9767     |
    | F9-LOWKP-5D       | 5                 | 80                   | 130      |
    | F10-LOWKP-20D     | 20                | 879                  | 1025     |

    # Example
    No exemplo dado, temos a instância **F1-LOWKP-10D**, que consiste em um conjunto de 10 objetos com seus respectivos valores e pesos. A variável de decisão x indica se cada objeto é selecionado (x = 1) ou não (x = 0).
    **Tabela 2**: F1-LOWKP-10D
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
    
    Dado a instância **F1-LOWKP-10D** descrita na Tabela 2 com 10 objetos conforme descrito na Tabela 1 e considerando que o vetor de variáveis de decisão é dado por $x={1,0,1,1,0,0,0,1,1,0}$.
    
    A função objetivo $(1)$ que soma apenas os itens escolhidos com base na variável binária $x_i$.Substituindo os valores de $x_i$ e $V_i$:
    """)
    st.latex("""
    f(x) = (1 \\times 95) + (0 \\times 4) + (1 \\times 60) + (1 \\times 32) + (0 \\times 23) + (0 \\times 72) + (0 \\times 80) + (1 \\times 62) + (1 \\times 65) + (0 \\times 46)
    """)
    st.markdown("""
    A restrição $(2)$ deve ser menor ou igual à capacidade máxima da mochila $c_{max}$. Substituindo os valores de $x_i$ e $P_i$:
    """)
    st.latex("""
    r(x) = (1 \\times 55) + (0 \\times 10) + (1 \\times 47) + (1 \\times 5) + (0 \\times 4) + (0 \\times 50) + (0 \\times 8) + (1 \\times 61) + (1 \\times 85) + (0 \\times 87)
    """)
    st.markdown("""
    Assim, a função objetivo e a restrição são:
    """)
    st.latex("""
    f(x) = - (95 + 0 + 60 + 32 + 0 + 0 + 0 + 62 + 65 + 0) = - 314
    """)
    st.latex("""
    r(x) = - (55 + 0 + 47 + 5 + 0 + 0 + 0 + 61 + 85 + 0) = - 253
    """)
    st.markdown("""
    Ao aplicar a equação (1), que calcula o valor da FO, utilizando o vetor de variáveis de decisão dado x = {1, 0, 1, 1, 0, 0, 0, 1, 1, 0}, obtemos o valor de -110, ou seja, a função objetivo é de minimização. É importante ressaltar que, na plataforma Meta, que é utilizada para a resolução deste problema, a FO é sempre de minimização, portanto, quando se faz otimização para maximização, a função objetivo fica negativa.
    """)
    st.latex("""
    value = -\left(55x_1 + 10x_2 + 47x_3 + 5x_4 + 4x_5 + 50x_6 + 8x_7 + 61x_8 + 85x_9 + 87x_{10}\\right) \\tag{1}
    """)
    st.markdown("""
    Além disso, é necessário verificar as restrições do problema, que neste caso são a restrição de capacidade da mochila. Na instância **F1-LOWKP-10D**, a capacidade da mochila é de 269, e a soma dos pesos dos objetos selecionados (55 + 10 + 47 + 8 + 61 + 85 + 87) é igual a 353, portanto, a restrição de capacidade não é atendida e a solução não é viável.
    """)
    st.latex("""
    w = 55x_1 + 10x_2 + 47x_3 + 5x_4 + 4x_5 + 50x_6 + 8x_7 + 61x_8 + 85x_9 + 87x_{10} \leq w_{max} \\tag{2}
    """)