import streamlit as st
from datetime import date
import datetime
import func
import streamlit.components.v1 as components

func.style_setup()

st.image("app/src/images/META_logo.png", width=150)
st.title("Portfolio Problem")
#st.write("O objetivo do Problema do Portfólio é construir uma carteira de investimentos composta por uma combinação de ativos financeiros, como ações, títulos, fundos imobiliários e commodities, de tal forma que o retorno esperado seja maximizado, considerando o nível de risco aceitável pelo investidor. Este problema envolve a análise de trade-offs entre risco e retorno, e a diversificação dos ativos é uma estratégia-chave para reduzir os riscos associados a flutuações de mercado e eventos econômicos adversos.")

st.write("""
    <div style='text-align: justify'>
        <p>O Problema do Portfólio consiste em selecionar diferentes ativos financeiros para compor uma carteira de investimentos, com o intuito de maximizar o retorno esperado e reduzir os riscos associados à flutuações do mercado. O modelo de Markowitz é aplicado para determinar os pesos ideais de cada ativo na carteira, por meio da diversificação e da otimização, a fim de alcançar uma combinação ótima que satisfaça os objetivos financeiros do investidor.</p>
    </div>
""", unsafe_allow_html=True)

st.write("""
    <div style='text-align: justify'>
A implementação da uma otimização de portfólio é feita utilizando o algoritmo Firefly. O objetivo é encontrar a alocação ótima de um portfólio, que maximize o índice de Sharpe, que relaciona o retorno do portfólio com o seu risco, com a introdução de restrições de limites de investimento em cada ativo do portfólio.
A implementação está estruturada da seguinte forma:
</div>
""", unsafe_allow_html=True)


st.write("""
    <div style='text-align: justify'>
    <ul>
        <li>A função STOCKS_DATASET carrega as informações de retorno e covariância diários de cada ativo do portfólio em um intervalo de tempo definido pelo usuário. Para fazer o calculo do retorno e covariância é usado as seguintes equações:</li>
    </ul>
 </div>
""", unsafe_allow_html=True)

equacao_ret = "**Return = ['Close'][J + 1] $\div$ ['Close'][J] - 1**"
st.markdown(equacao_ret, unsafe_allow_html=True)

st.write("""
Onde:

['Close'][J + 1]: preço de fechamento do dia atual.

['Close'][J] - 1: preço de fechamento do dia anterior.
""")
equacao_cov = "**COVARIANCE = RETURN.cov()**"
st.write(equacao_cov, unsafe_allow_html=True)

st.write("""
    <div style='text-align: justify'>
    <ul>
        <li>A função PORTIFOLIO_RETURN_RISK calcula o retorno e risco anualizados do portfólio, dado um determinado vetor de pesos X, utilizando a matriz de covariância e o vetor de retornos, definidos no dicionário NULL_DIC. O cálculo do retorno e risco anualizado do portfolio é feito usando as seguintes equações:</li>
    </ul>
</div>
""", unsafe_allow_html=True)

eq_pot_ret = "**Retorno <sub>carteira</sub> = $\sum$ X[I] * RETURN[I] * T_Y**"
st.write(eq_pot_ret, unsafe_allow_html=True)

st.write("""
Onde:

X[I]: é a lista de pesos para os ativos.

RETURN: é a lista de retorno dos ativos.

T_Y: é o número de dias que a bolsa  opera em 1 ano.
""")

eq_pot_var = "***VAR = $\sum$ X[I] * X[J] * COVARIANCE[I, J] *T_Y***"

st.write(eq_pot_var, unsafe_allow_html=True)

st.write("""
Onde: 

X[I]: é a lista de pesos para os ativos.

COVARIANCE[I,J]: é a matriz de covariância.

T_Y: é o número de dias que a bolsa  opera em 1 ano.
""")

eq_risco = "**Risco<sub>carteira</sub> = $\sqrt{Var}$**"
st.write(eq_risco, unsafe_allow_html=True)


st.write("""
    <div style='text-align: justify'>
        <ul>
        <li>A função objetiva do problema de otimização, definida como o índice de Sharpe negativo do portfólio (de forma a transformar o problema de maximização em minimização), acrescido de uma penalização às violações da restrição de investimento em cada ativo do portfólio.</li>  
        </ul>
    </div>
""", unsafe_allow_html=True)
st.write("""
    <div style='text-align: justify'>
    Por fim, o código define os limites de investimento (X_L e X_U), o dicionário NULL_DIC, contendo as informações necessárias para a resolução do problema de otimização, e os parâmetros do algoritmo Firefly (PARAMETERS). A função OF_FUNCTION é utilizada como a função objetivo do algoritmo, e a função PORTIFOLIO_RETURN_RISK é utilizada para calcular o retorno e risco do portfólio em cada iteração do algoritmo.
</div>
""", unsafe_allow_html=True)



#Escolher metodo de otimizacao
Optimization = ["Selecione o metodo de otimização","Firefly Algorithm"]

selected_Optimization = st.selectbox("**Optimization:**", Optimization)
   
if selected_Optimization == "Firefly Algorithm":

    #seleciona o conjuntos de ativo
    stocks_set = ["Selecione o conjunto de ativos","Conjunto de ativos 1", "Conjunto de ativos 2", "Conjunto de ativos 3", "Custom"]
    selected_instance = st.selectbox("**Conjunto de Ativos**", stocks_set)
    
    if selected_instance == "Conjunto de ativos 1":
        st.markdown(
        """
        | Empresa                 | Símbolo   |
        |-------------------------|-----------|
        |WEG S.A.                 | WEGE3.SA  |
        |Lojas Renner S.A.        | LREN3.SA  | 
        |Vale S.A.                | VALE3.SA  | 
        |Petróleo Brasileiro S.A. | PETR4.SA  |
        |Equatorial Energia S.A.  | EQTL3.SA  |
   
        """
        )
        stocks_set_1 = ["WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"]

        start_day = datetime.date.today()
        start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        end_day = date.today()
        end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        if end_day < start_day:
            st.error("A data final deve ser posterior à data inicial.")
        
#Setup e parametros
        st.markdown("**Design space**")
        st.markdown(
        """
        X_L = [0.00001] * D

        X_U = [0.99999] * D
        """)
        st.markdown("**Setup FA method**")
        st.markdown(
        """" 
        
        GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)
        PARAMETERS = {
                   'ATTRACTIVENESS (BETA_0)': 0.98,
                   'MIN. RANDOM FACTOR (ALPHA_MIN)': 0.20,
                   'MAX. RANDOM FACTOR (ALPHA_MAX)': 0.95,
                   'LIGHT ABSORPTION (GAMMA)': GAMMA,
                   'THETA': 0.98,
                   'TYPE ALPHA UPDATE': 'YANG 0',
                    'SCALING (S_D)': True
        }""")
        
        st.markdown("**Setup optimization**")
        st.markdown("{")
        N_REP = st.number_input("N_REP", format="%0.0f")
        N_POP = st.number_input("N_ITER", format="%0.0f")
        N_ITER = st.number_input("N_POP", format="%0.0f")
        st.markdown(
        """
        'D':   D,                                                                                                 
        'X_L': X_L,                                                                                              
        'X_U': X_U,                                                                                              
        'PARAMETERS': PARAMETERS,                                                                                   
        'NULL_DIC':{'RETURN': PORTIFOLIO_RETURNS, 'RISK': PORTIFOLIO_RISKS, 'RISK_FREE': RISK_FREE_ASSET, 'RP': 1E6}
        } 
        """)

        if st.button ("**Play**"):
            st.markdown("Resultado")

    elif selected_instance == "Conjunto de ativos 2":
        st.markdown(
        """
        | Empresa                  | Símbolo   |
        |--------------------------|-----------|
        |Engie Brasil Energia S.A. | EGIE3.SA  |
        |Magazine Luiza S.A.       | MGLU3.SA  | 
        |Ambev S.A.                | ABEV3.SA  | 
        |Banco Bradesco S.A.       | BBDC3.SA  |
        |NIKE, Inc.                | NIKE34.SA |
        """
        )
        stocks_set_2 = ["EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"]

        start_day = datetime.date.today()
        start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        end_day = date.today()
        end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        if end_day < start_day:
            st.error("A data final deve ser posterior à data inicial.")
        
#Setup e parametros
        st.markdown("**Design space**")
        st.markdown(
        """
        X_L = [0.00001] * D

        X_U = [0.99999] * D
        """)
        st.markdown("**Setup FA method**")
        st.markdown(
        """" 
        
        GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)
        PARAMETERS = {
                   'ATTRACTIVENESS (BETA_0)': 0.98,
                   'MIN. RANDOM FACTOR (ALPHA_MIN)': 0.20,
                   'MAX. RANDOM FACTOR (ALPHA_MAX)': 0.95,
                   'LIGHT ABSORPTION (GAMMA)': GAMMA,
                   'THETA': 0.98,
                   'TYPE ALPHA UPDATE': 'YANG 0',
                    'SCALING (S_D)': True
        }""")
        
        st.markdown("**Setup optimization**")
        st.markdown("{")
        N_REP = st.number_input("N_REP", format="%0.0f")
        N_POP = st.number_input("N_ITER", format="%0.0f")
        N_ITER = st.number_input("N_POP", format="%0.0f")
        st.markdown(
        """
        'D':   D,                                                                                                 
        'X_L': X_L,                                                                                              
        'X_U': X_U,                                                                                              
        'PARAMETERS': PARAMETERS,                                                                                   
        'NULL_DIC':{'RETURN': PORTIFOLIO_RETURNS, 'RISK': PORTIFOLIO_RISKS, 'RISK_FREE': RISK_FREE_ASSET, 'RP': 1E6}
        } 
        """)

        if st.button ("**Play**"):
            st.markdown("Resultado")


    if selected_instance == "Conjunto de ativos 3":
        st.markdown(
        """
        | Empresa                  | Símbolo   |
        |--------------------------|-----------|
        |C&A Modas S.A.            | CEAB3.SA  |
        |Itaúsa S.A.               | ITSA4.SA  | 
        |Atacadão S.A.             | CRFB3.SA  | 
        |Sony Group Corporation    | SNEC34.SA |
        |Nu Holdings Ltd.          | NUBR33.SA |
        """
        )
        stocks_set_3 = ["NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"]

        start_day = datetime.date.today()
        start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        end_day = date.today()
        end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        if end_day < start_day:
            st.error("A data final deve ser posterior à data inicial.")
        
#Setup e parametros
        st.markdown("**Design space**")
        st.markdown(
        """
        X_L = [0.00001] * D

        X_U = [0.99999] * D
        """)
        st.markdown("**Setup FA method**")
        st.markdown(
        """" 
        
        GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)
        PARAMETERS = {
                   'ATTRACTIVENESS (BETA_0)': 0.98,
                   'MIN. RANDOM FACTOR (ALPHA_MIN)': 0.20,
                   'MAX. RANDOM FACTOR (ALPHA_MAX)': 0.95,
                   'LIGHT ABSORPTION (GAMMA)': GAMMA,
                   'THETA': 0.98,
                   'TYPE ALPHA UPDATE': 'YANG 0',
                    'SCALING (S_D)': True
        }""")
        
        st.markdown("**Setup optimization**")
        st.markdown("{")
        N_REP = st.number_input("N_REP", format="%0.0f")
        N_POP = st.number_input("N_ITER", format="%0.0f")
        N_ITER = st.number_input("N_POP", format="%0.0f")
        st.markdown(
        """
        'D':   D,                                                                                                 
        'X_L': X_L,                                                                                              
        'X_U': X_U,                                                                                              
        'PARAMETERS': PARAMETERS,                                                                                   
        'NULL_DIC':{'RETURN': PORTIFOLIO_RETURNS, 'RISK': PORTIFOLIO_RISKS, 'RISK_FREE': RISK_FREE_ASSET, 'RP': 1E6}
        } 
        """)

        if st.button ("**Play**"):
            st.markdown("Resultado")


    elif selected_instance == "Custom":
        #Conjunto de ativos
        custom = st.text_input("**Digite os símbolos dos ativos:**")
        stocks_custom = []
        stocks_custom = custom.split(",")
        stocks_custom = [stocks_custom.strip() for stocks_custom in stocks_custom]
        
        #Data
        start_day = datetime.date.today()
        start_day = st.date_input("**Selecione a data inicial**", max_value=start_day)
        
        end_day = date.today()
        end_day = st.date_input("Selecione a data final",max_value=end_day)
        
        if end_day < start_day:
            st.error("A data final deve ser posterior à data inicial.")
        
        #Setup e parametros
        st.markdown("**Design space**")
        st.markdown(
        """
        X_L = [0.00001] * D

        X_U = [0.99999] * D
        """)
        st.markdown("**Setup FA method**")
        st.markdown(
        """" 
        
        GAMMA = GAMMA_ASSEMBLY(X_L, X_U, D, 2)
        PARAMETERS = {
                   'ATTRACTIVENESS (BETA_0)': 0.98,
                   'MIN. RANDOM FACTOR (ALPHA_MIN)': 0.20,
                   'MAX. RANDOM FACTOR (ALPHA_MAX)': 0.95,
                   'LIGHT ABSORPTION (GAMMA)': GAMMA,
                   'THETA': 0.98,
                   'TYPE ALPHA UPDATE': 'YANG 0',
                    'SCALING (S_D)': True
        }""")
        
        st.markdown("**Setup optimization**")
        st.markdown("{")
        N_REP = st.number_input("N_REP", format="%0.0f")
        N_POP = st.number_input("N_ITER", format="%0.0f")
        N_ITER = st.number_input("N_POP", format="%0.0f")
        st.markdown(
        """
        'D':   D,                                                                                                 
        'X_L': X_L,                                                                                              
        'X_U': X_U,                                                                                              
        'PARAMETERS': PARAMETERS,                                                                                   
        'NULL_DIC':{'RETURN': PORTIFOLIO_RETURNS, 'RISK': PORTIFOLIO_RISKS, 'RISK_FREE': RISK_FREE_ASSET, 'RP': 1E6}
        } 
        """)
        if st.button ("**Play**"):
            st.markdown("Resultado")
