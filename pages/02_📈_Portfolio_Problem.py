import streamlit as st
from datetime import date
import datetime
import FA_PORTIFOLIO

st.image("images/META_logo.png", width=150)
st.title("Portfolio Problem")
#st.write("O objetivo do Problema do Portfólio é construir uma carteira de investimentos composta por uma combinação de ativos financeiros, como ações, títulos, fundos imobiliários e commodities, de tal forma que o retorno esperado seja maximizado, considerando o nível de risco aceitável pelo investidor. Este problema envolve a análise de trade-offs entre risco e retorno, e a diversificação dos ativos é uma estratégia-chave para reduzir os riscos associados a flutuações de mercado e eventos econômicos adversos.")

st.write("""
    <div style='text-align: justify'>
        <p>O Problema do Portfólio consiste em selecionar diferentes ativos financeiros para compor uma carteira de investimentos, com o intuito de maximizar o retorno esperado e reduzir os riscos associados à flutuações do mercado. O modelo de Markowitz é aplicado para determinar os pesos ideais de cada ativo na carteira, por meio da diversificação e da otimização, a fim de alcançar uma combinação ótima que satisfaça os objetivos financeiros do investidor.</p>
    </div>
""", unsafe_allow_html=True)

st.write("""
    <div style='text-align: justify'>
A implementação da otimização de portfólio é feita utilizando o algoritmo Firefly. O objetivo é encontrar a alocação ótima de um portfólio, que maximize o índice de Sharpe, que relaciona o retorno do portfólio com o seu risco, com a restrição de que o somatório do conjunto de ativos do portfólio tem que ser igual a 100%.
A implementação está estruturada da seguinte forma:
</div>
""", unsafe_allow_html=True)


st.write("""
    <div style='text-align: justify'>
    <ul>
        <li>Uma função é empregada para carregar informações sobre os preços de cada ativo da carteira durante um determinado período de tempo pré-estabelecido, assim como fazer os cálculos de retorno e covariância desses ativos, as informações são obtidas através do Yahoo! Finance. Para fazer o calculo do retorno e covariância é usado as seguintes equações:</li>
    </ul>
 </div>
""", unsafe_allow_html=True)


st.latex("""Retorno = {['Close'][J + 1]}{['Close'][J] - 1}""")

st.write("""
Onde:

['Close'][J + 1]: preço de fechamento do dia atual.

['Close'][J] - 1: preço de fechamento do dia anterior.
""")

st.latex("""Covariance = Retorno.cov() """)

st.write("""
    <div style='text-align: justify'>
    <ul>
        <li>Uma função responsável por calcula o retorno e risco anualizados do portfólio, dado um determinado vetor de pesos , utilizando a matriz de covariância e o vetor de retornos, definidos em um dicionário. O cálculo do retorno e risco anualizado do portfolio é feito usando as seguintes equações:</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.latex("""Retorno_{carteira} = \sum X[I] * Retorno[I] * T_Y""")

st.write("""
Onde:

X[I]: é a lista de pesos para os ativos.

RETURN: é a lista de retorno dos ativos.

T_Y: é o número de dias que a bolsa  opera em 1 ano.
""")

st.latex("""Var = \sum X[I] * X[J] * Covariance[I, J] *T_Y """)

st.write("""
Onde: 

X[I]: é a lista de pesos para os ativos.

Covariance[I,J]: é a matriz de covariância.

T_Y: é o número de dias que a bolsa  opera em 1 ano.
""")

st.latex("""Risco_{carteira} = \sqrt{Var}""")


st.write("""
    <div style='text-align: justify'>
        <ul>
        <li>A função objetiva do problema de otimização, definida como o índice de Sharpe negativo do portfólio (de forma a transformar o problema de maximização em minimização), acrescido de uma penalização às violações da restrição de investimento em cada ativo do portfólio.</li>  
        </ul>
    </div>
""", unsafe_allow_html=True)
st.write("""
    <div style='text-align: justify'>
    Por fim, o código define os limites de investimento, o dicionário, contendo as informações necessárias para a resolução do problema de otimização, e os parâmetros do algoritmo Firefly. Uma função é utilizada para calcular o retorno e risco do portfólio em cada iteração do algoritmo.
</div>
""", unsafe_allow_html=True)

st.write("""
    <div style='text-align: justify'>
    De forma resumida, o algoritmo é responsável por selecionar um conjunto de n ativos, obter as informações referentes a um período específico e, com base na Teoria de Markowitz, realizar cálculos e um processo de otimização a fim de retornar uma solução ideal de distribuição do investimento percentual em cada ativo.
    </div>
""", unsafe_allow_html=True)

#Escolher metodo de otimizacao
Optimization = ["Selecione o metodo de otimização","Firefly Algorithm"]

selected_Optimization = st.selectbox("**Optimization:**", Optimization)
   
if selected_Optimization == "Firefly Algorithm":

    #seleciona o conjuntos de ativo
    stocks_set = ["Selecione a Instância","USA-1", "USA-2", "USA-3", "USA-4"]
    selected_instance = st.selectbox("**Instância**", stocks_set)
    
    if selected_instance == "USA-1":
        st.markdown(
        """
        | Empresa         | Símbolo   | Parâmetros da Otimização  | Data Inicial | Data Final |
        |-----------------|-----------|---------------------------|--------------|------------|
        |Apple            | AAPL      | Número de Repetições: 30  | 01/01/2016   | 31/12/2017 |
        |Amazon           | AMZN      | Número de Interações: 500 |
        |Meta Platforms   | META      | Número da População:  20  |
        |Google           | GOOGL     |
        
        """
        )
        if st.button ("**Play**"):
            FA_PORTIFOLIO.FIREFLY()
    
    elif selected_instance == "USA-2":
        st.markdown(
        """
        | Empresa                 | Símbolo   | Parâmetros da Otimização  | Data Inicial | Data Final |
        |-------------------------|-----------|---------------------------|--------------|------------|
        |WEG S.A.                 | WEGE3.SA  | Número de Repetições: 30  | 01/01/2016   | 31/12/201  |
        |Lojas Renner S.A.        | LREN3.SA  | Número de Interações: 500 |
        |Vale S.A.                | VALE3.SA  | Número da População:  20  |
        |Petróleo Brasileiro S.A. | PETR4.SA  |
        |Equatorial Energia S.A.  | EQTL3.SA  |
   
        """
        )
        stocks_set_2 = ["WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"]

        #start_day = datetime.date.today()
        #start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        #end_day = date.today()
        #end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        #if end_day < start_day:
         #   st.error("A data final deve ser posterior à data inicial.")
        
#Setup e parametros
    
        # N_REP = st.number_input("N_REP", format="%0.1f")
        # N_POP = st.number_input("N_ITER", format="%0.1f")
        # N_ITER = st.number_input("N_POP", format="%0.1f")

        if st.button ("**Play**"):
            FA_PORTIFOLIO.FIREFLY()

    if selected_instance == "USA-3":
        st.markdown(
        """
        | Empresa                  | Símbolo   | Parâmentros da Otimização  | Data Inicial | Data Final |
        |--------------------------|-----------|----------------------------|--------------|------------|
        |Engie Brasil Energia S.A. | EGIE3.SA  | Número de Repetições: 30   |01/01/2016    | 31/12/2017 |
        |Magazine Luiza S.A.       | MGLU3.SA  | Número de Interações: 500  |
        |Ambev S.A.                | ABEV3.SA  | Número da População:  20   |
        |Banco Bradesco S.A.       | BBDC3.SA  |
        |NIKE, Inc.                | NIKE34.SA |
        """
        )
        stocks_set_3 = ["EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"]

        #start_day = datetime.date.today()
        #start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        #end_day = date.today()
        #end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        #if end_day < start_day:
        #    st.error("A data final deve ser posterior à data inicial.")
        
#Setup e parametros
        # N_REP = st.number_input("N_REP", format="%0.1f")
        # N_POP = st.number_input("N_ITER", format="%0.1f")
        # N_ITER = st.number_input("N_POP", format="%0.1f")

        if st.button ("**Play**"):
            FA_PORTIFOLIO.FIREFLY()


    elif selected_instance == "USA-4":
        st.markdown(
        """
        | Empresa               | Símbolo   | Parâmetros da Otimização  | Data Inicial | Data Final | 
        |-----------------------|-----------|---------------------------|--------------|------------|
        |C&A Modas S.A.         | CEAB3.SA  | Número de Repetições: 30  | 01/01/2016   | 31/12/2017 | 
        |Itaúsa S.A.            | ITSA4.SA  | Número de Interações: 500 |              |            | 
        |Atacadão S.A.          | CRFB3.SA  | Número da População:  20  |              |            | 
        |Sony Group Corporation | SNEC34.SA |
        |Nu Holdings Ltd.       | NUBR33.SA |
        """
        )
        stocks_set_4 = ["NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"]

        #start_day = datetime.date.today()
        #start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        #end_day = date.today()
        #end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        #if end_day < start_day:
         #   st.error("A data final deve ser posterior à data inicial.")
        
#Setup e parametros
        
        # N_REP = st.number_input("N_REP", format="%0.1f")
        # N_POP = st.number_input("N_ITER", format="%0.1f")
        # N_ITER = st.number_input("N_POP", format="%0.1f")

        if st.button ("**Play**"):
            FA_PORTIFOLIO.FIREFLY()


    # elif selected_instance == "Custom":
    #     #Conjunto de ativos
    #     custom = st.text_input("**Digite os símbolos dos ativos:**")
    #     stocks_custom = []
    #     stocks_custom = custom.split(",")
    #     stocks_custom = [stocks_custom.strip() for stocks_custom in stocks_custom]
        
    #     #Data
    #     start_day = datetime.date.today()
    #     start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        
    #     end_day = date.today()
    #     end_day = st.date_input("Selecione a data final",max_value=end_day)
        
    #     if end_day < start_day:
    #         st.error("A data final deve ser posterior à data inicial.")
        
    #     #Setup e parametros
        
    #     N_REP = st.number_input("N_REP", format="%0.0f")
    #     N_POP = st.number_input("N_ITER", format="%0.0f")
    #     N_ITER = st.number_input("N_POP", format="%0.0f")

    #     if st.button ("**Play**"):
    #         FA_PORTIFOLIO.FIREFLY()
