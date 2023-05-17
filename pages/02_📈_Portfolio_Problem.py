import streamlit as st
from datetime import date
st.image("images/META_logo.png", width=150)
st.title("Portfolio Problem")
st.write("O objetivo do Problema do Portfólio é construir uma carteira de investimentos composta por uma combinação de ativos financeiros, como ações, títulos, fundos imobiliários e commodities, de tal forma que o retorno esperado seja maximizado, considerando o nível de risco aceitável pelo investidor. Este problema envolve a análise de trade-offs entre risco e retorno, e a diversificação dos ativos é uma estratégia-chave para reduzir os riscos associados a flutuações de mercado e eventos econômicos adversos.")

st.markdown("Optimization menu:")

Optimization = ["Hill Climbing","Simulated Annealing","Firefly Algorithm","Particle Swarm Optimization","Differential Evolution","Genetic Algorithm"]
selected_Optimization = st.selectbox("Optimization", Optimization)

if selected_Optimization == "Hill Climbing":
    st.write('Hill Climbing foi um dos primeiros algoritmos de otimização estocástica existentes na literatura. O método Hill Climbing também é conhecido como método de busca local [1].')
    texto = "O procedimento iterativo é baseado na melhoria contínua da solução até que a melhor solução seja alcançada. O processo consiste em gerar vizinhos aleatórios da solução atual, conforme a equação (1), onde N indica uma distribuição Gaussiana onde a média x<sup>t</sup> é a solução atual e $\sigma$ é o desvio padrão inserido pelo usuário é a k-ésima componente do vetor variável de projeto X."
    st.write(texto, unsafe_allow_html=True)
    equacao = "x<sub>k</sub><sup>t+1</sup> = N(x<sub>k</sub><sup>t</sup>$\sigma$) vizinho aleatório (1)"
    st.write(equacao, unsafe_allow_html=True)
    st.markdown(
    """
    ## Setup
    """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Stocks Set 1", "Stocks Set 2", "Stocks Set 3", "Custom"]
    selected_instance = st.selectbox("Stocks Set", stocks_set)
    
    start_day = st.date_input("Selecione a data inicial", date.today())
    end_day = st.date_input("Selecione a data final", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Stocks Set 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Stocks Set 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Stocks Set 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("Digite o código dos ativos:")
        st.write(stocks)

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
    """
    )

elif selected_Optimization == "Simulated Annealing":
    st.write('O método Simulated Annealing foi introduzido por Kirkpatrick et al. [1,2] em 1983. Este algoritmo é inspirado no processo de recozimento de metais durante o processo de fabricação. O modelo Simulated Annealing baseia-se na geração de vizinhos aleatórios a partir de um ponto de partida, à semelhança do que ocorre no algoritmo Hill Climbing')
    texto = "No algoritmo Simulated Annealing, a aceitação da nova solução é dada por um critério que compara a energia do sistema dada pela equação (1). Neste algoritmo, os valores de E<sub>i</sub> são relativos ao valor da função objetivo para i<sub>particle</sub>, i.e., E<sub>i</sub> = OF<sub>i</sub>."
    st.write(texto, unsafe_allow_html=True)
    
    equacao = "$\Delta$E = E<sub>cur</sub> - E<sub>new</sub>  (1)"
    st.write(equacao, unsafe_allow_html=True)

    texto2 = "O valor que E<sub>new</sub> é o valor da função objetivo para o vizinho recém-gerado e E<sub>cur</sub> é o valor da função objetivo para a partícula atual."
    st.write(texto2, unsafe_allow_html=True)

    texto3 = "A solução será aceita se  E<sub>cur</sub> > E<sub>new</sub>(P($\Delta$E)= 1.00). Para soluções do tipo E<sub>cur</sub> < E<sub>new</sub> a aceitação seguirá uma certa probabilidade dada pela equação (2) onde T é a temperatura de recozimento. "
    st.write(texto3, unsafe_allow_html=True)

    equacao2 = "P($\Delta$E) = e<sup>$\Delta$E/T</sup>   (2)"
    st.write(equacao2, unsafe_allow_html=True)

    st.markdown(
    """
    ## Setup
    """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Stocks Set 1", "Stocks Set 2", "Stocks Set 3", "Custom"]
    selected_instance = st.selectbox("Stocks Set", stocks_set)
    
    start_day = st.date_input("Selecione a data inicial", date.today())
    end_day = st.date_input("Selecione a data final", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Stocks Set 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Stocks Set 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Stocks Set 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("Digite o código dos ativos:")
        st.write(stocks)

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
    """
    )
elif selected_Optimization == "Firefly Algorithm":
    texto = "O Firefly Algorithm (AF) foi introduzido por Xin-Shen Yang [1] em 2008 com base no sistema de comunicação dos vaga-lumes em função de sua bioluminescência [1]. Para tanto, Yang [1] simplificou o procedimento definindo os seguintes pressupostos: (a) Os indivíduos não são distinguíveis por gênero, portanto podem interagir por atratividade ($\beta$) (b) A atratividade é inversamente proporcional à distância euclidiana (r) e há um fator de permeabilidade $\gamma$ de luminosidade no meio, de forma a reduzir a intensidade da luz; (c) A luminosidade é definida através da Função Objetivo (FO)."
    st.write(texto, unsafe_allow_html=True)

    texto2 = "Portanto, cada vaga-lume se comporta como uma possível solução (k é a k-ésima componente do vetor variável de projeto x) ao problema dentro de um espaço de busca previamente definido. Assim, com base na atratividade do fator ($\beta$), permeabilidade ($\gamma$), e aleatoriedade ($\$alpha), cada nova geração é definida com base na equação (1):"
    st.write(texto2, unsafe_allow_html=True)

    equacao = "x<sup>t+1</sup><sub>i,k</sub> = x<sup>t</sup><sub>i,k</sub> + $\beta$ * (x<sup>t</sup><sub>j,k</sub> - x<sup>t</sup><sub>i,k</sub>) + $\alpha$ * sd<sub>k</sub> *(rand<sub>k</sub> - 0.50) (1) "
    st.write(equacao, unsafe_allow_html=True)

    texto3 = "Onde o vetor de atratividade ($\beta$), correspondente à atratividade do vaga-lume é entendida como o grau de percepção luminosa que uma partícula i tem de seus pares (x<sub>j</sub>) em função da distância euclidiana (r<sub>i,j</sub>) entre os indivíduos é fornecida pela equação (2). $\beta$<sub>0</sub> é o valor da distância nula (equação 3). Portanto, um baixo valor de $\beta$ seja devido a uma grande distância ou alta absorção de luz pelo meio $\gamma$, , afetará um modelo com um caráter aleatório maior. Quando o $\beta$ = 0 o movimento depende apenas do passeio aleatório [2]. Se $\gamma$ $\setadireita$ 0, a atratividade torna-se $\beta$ = $\beta$<sub>0</sub>. Ou seja, a atratividade é constante em qualquer lugar dentro do espaço de busca [2]. x<sup>t</sup><sub>i</sub> é a solução atual e x<sup>t</sup><sub>j</sub> é a solução vizinha atual x<sub>upper</sub> é o limite superior das variáveis e x<sub>lower</sub> é o limite inferior das variáveis. t é a iteração atual do algoritmo. sd é a escala de cada variável de projeto (x<sub>upper</sub> - x<sub>lower</sub>)"
    st.write(texto3, unsafe_allow_html=True)

    equacao2 = "r<sub>ij</sub> = $\sqrt{}$ $\sum_{i=1}^{Npop}$x<sub>ik</sub><sup>t</sup> - x<sub>jk</sub><sup>t</sup>         (2)"
    st.write(equacao2, unsafe_allow_html=True)

    equacao3 = ""
    st.write(equacao3, unsafe_allow_html=True)

    equacao4 = ""
    st.write(equacao4, unsafe_allow_html=True)

    st.markdown(
    """
    ## Setup
    """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Stocks Set 1", "Stocks Set 2", "Stocks Set 3", "Custom"]
    selected_instance = st.selectbox("Stocks Set", stocks_set)
    
    start_day = st.date_input("Selecione a data inicial", date.today())
    end_day = st.date_input("Selecione a data final", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Stocks Set 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Stocks Set 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Stocks Set 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("Digite o código dos ativos:")
        st.write(stocks)

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
    """
    )

elif selected_Optimization == "Particle Swarm Optimization":
    st.markdown(
    """
    O Particle Swarm Optimization (PSO) foi desenvolvido por James Kennedy e Russell Elberthart [1] em 1995 a partir de experiências comportamentais como cardumes e bandos de pássaros [2]. O processo ocorre através da cooperação (aprendizagem em grupo) e competição (aprendizagem individual) entre os membros de um grupo [3]. Assim, a tomada de decisão de um indivíduo dependerá de seu desempenho passado, bem como de partículas vizinhas.

    O algoritmo PSO não possui funções de crossover e mutação, portanto o funcionamento se dá pela evolução de um enxame aleatório de indivíduos dispostos em um espaço d-dimensional, que a cada iteração, são atualizados de acordo com a melhor Função Objetivo (OF) individual valor e grupo. Assim, o algoritmo PSO é estruturado em dois princípios para o movimento de partículas. A primeira refere-se à influência do grupo sobre cada indivíduo e a segunda cria um tipo de memória em cada indivíduo do enxame.   
    """
    )
    texto = "Portanto, um i partícula se moverá em uma certa direção de acordo com a equação (2). O movimento é dado em função da posição atual x<sub>i</sub><sup>t</sup> da velocidade definida na equação (1). pB indica a melhor posição encontrada até agora para a partícula i e gB indica a melhor posição encontrada até agora para o enxame. k é a k-ésima componente do vetor variável de projeto x.w<sup>t</sup> indica o peso de inércia.t é a iteração atual do algoritmo."
    st.write(texto, unsafe_allow_html=True)

    equacao = "v<sub>i,k</sub><sup>t+1</sup> = w<sup>t</sup> * v<sub>i,k</sub><sup>t</sup> + c<sub>1</sub>*r<sub>1</sub>(pB<sub>k</sub><sup>t</sup> - x<sub>i,k</sub><sup>t</sup>) + c<sub>2</sub> * r<sub>2</sub>(gB<sub>k</sub><sup>t</sup> - x<sub>i,k</sub><sup>t</sup>)  v<sub>k</sub> = $\epsilon$ {v<sub>min,k</sub>,v<sub>max,k</sub> } (1)"
    st.write(equacao, unsafe_allow_html=True)

    texto2 = "v<sub>max</sub> é o limite superior da velocidade e v<sub>min</sub> é o limite inferior da velocidade. r<sub>1</sub> e r<sub>2</sub> são números aleatórios entre (0,1), e c<sub>1</sub> e c<sub>2</sub> representam as constantes do termo cognitivo e do termo social."
    st.write(texto2, unsafe_allow_html=True)

    equacao2 = "x<sub>i,k</sub><sup>t+1</sup> = x<sub>i,k</sub><sup>t</sup> + v<sub>i,k</sub><sup>t+1</sup> (2) "
    st.write(equacao2, unsafe_allow_html=True)

    st.markdown(
    """
    ## Setup
    """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Stocks Set 1", "Stocks Set 2", "Stocks Set 3", "Custom"]
    selected_instance = st.selectbox("Stocks Set", stocks_set)
    
    start_day = st.date_input("Selecione a data inicial", date.today())
    end_day = st.date_input("Selecione a data final", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Stocks Set 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Stocks Set 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Stocks Set 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("Digite o código dos ativos:")
        st.write(stocks)

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
    """
    )
elif selected_Optimization == "Differential Evolution":
    st.markdown(
    """
    # 
    """
    )
    st.markdown(
    """
    ## Setup
    """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Stocks Set 1", "Stocks Set 2", "Stocks Set 3", "Custom"]
    selected_instance = st.selectbox("Stocks Set", stocks_set)
    
    start_day = st.date_input("Selecione a data inicial", date.today())
    end_day = st.date_input("Selecione a data final", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Stocks Set 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Stocks Set 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Stocks Set 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("Digite o código dos ativos:")
        st.write(stocks)

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
    """
    )
elif selected_Optimization == "Genetic Algorithm":
    st.markdown(
    """
    # 
    """
    )
    st.markdown(
    """
    ## Setup
    """
    )
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Stocks Set 1", "Stocks Set 2", "Stocks Set 3", "Custom"]
    selected_instance = st.selectbox("Stocks Set", stocks_set)
    
    start_day = st.date_input("Selecione a data inicial", date.today())
    end_day = st.date_input("Selecione a data final", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Stocks Set 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Stocks Set 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Stocks Set 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("Digite o código dos ativos:")
        st.write(stocks)

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
    """
    )

