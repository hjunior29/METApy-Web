import streamlit as st
from datetime import date
st.image("images/META_logo.png", width=150)
st.title("Portfolio Problem")
st.write("O objetivo do Problema do Portfólio é construir uma carteira de investimentos composta por uma combinação de ativos financeiros, como ações, títulos, fundos imobiliários e commodities, de tal forma que o retorno esperado seja maximizado, considerando o nível de risco aceitável pelo investidor. Este problema envolve a análise de trade-offs entre risco e retorno, e a diversificação dos ativos é uma estratégia-chave para reduzir os riscos associados a flutuações de mercado e eventos econômicos adversos.")

Optimization = ["Hill Climbing","Simulated Annealing","Firefly Algorithm","Particle Swarm Optimization"]
selected_Optimization = st.selectbox("**Optimization:**", Optimization)

if selected_Optimization == "Hill Climbing":
    st.markdown("**Setup**")
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks = ["Conjunto de ativos 1", "Conjunto de ativos 2", "Conjunto de ativos 3", "Custom"]
    selected_instance = st.selectbox("**Conjunto de Ativos**", stocks)
    
    start_day = st.date_input("**Selecione a data inicial**", date.today())
    end_day = st.date_input("**Selecione a data final**", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Conjunto de ativos 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Conjunto de ativos 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Conjunto de ativos 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("**Digite o código dos ativos:**")
        st.write(stocks)

    if st.button ("**Play**"):
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
    st.markdown("**Setup**")
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Conjunto de ativos 1", "Conjunto de ativos 2", "Conjunto de ativos 3", "Custom"]
    selected_instance = st.selectbox("**Conjunto de Ativos**", stocks_set)
    
    start_day = st.date_input("**Selecione a data inicial**", date.today())
    end_day = st.date_input("**Selecione a data final**", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Conjunto de ativos 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Conjunto de ativos 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Conjunto de ativos 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("**Digite o código dos ativos:**")
        st.write(stocks)

    if st.button ("**Play**"):
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
    st.markdown("**Setup**")
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Conjunto de ativos 1", "Conjunto de ativos 2", "Conjunto de ativos 3", "Custom"]
    selected_instance = st.selectbox("**Conjunto de Ativos**", stocks_set)
    
    start_day = st.date_input("**Selecione a data inicial**", date.today())
    end_day = st.date_input("**Selecione a data final**", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Conjunto de ativos 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Conjunto de ativos 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Conjunto de ativos 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("**Digite o código dos ativos:**")
        st.write(stocks)

    if st.button ("**Play**"):
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
    st.markdown("**Setup**")
    N_REP = st.number_input("N_REP", format="%0.0f")
    N_POP = st.number_input("N_POP", format="%0.0f")
    N_ITER = st.number_input("N_ITER", format="%0.0f")

    stocks_set = ["Conjunto de ativos 1", "Conjunto de ativos 2", "Conjunto de ativos 3", "Custom"]
    selected_instance = st.selectbox("**Conjunto de Ativos**", stocks_set)
    
    start_day = st.date_input("**Selecione a data inicial**", date.today())
    end_day = st.date_input("**Selecione a data final**", date.today())
    if end_day < start_day:
        st.error("A data final deve ser posterior à data inicial.")

    if selected_instance == "Conjunto de ativos 1":
        st.markdown(
        """
        "WEGE3.SA", "LREN3.SA", "VALE3.SA", "PETR4.SA", "EQTL3.SA"
   
        """
        )
    elif selected_instance == "Conjunto de ativos 2":
        st.markdown(
        """
        "EGIE3.SA","NIKE34.SA", "ABEV3.SA","BBDC3.SA","MGLU3.SA"
        """
        )
    if selected_instance == "Conjunto de ativos 3":
        st.markdown(
        """
        "NUBR33.SA","ITSA4.SA", "CEAB3.SA","SNEC34.SA","CRFB3.SA"
        """
        )

    elif selected_instance == "Custom":
        stocks = st.text_input("**Digite o código dos ativos:**")
        st.write(stocks)

    if st.button ("**Play**"):
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
