import streamlit as st
import INSTANCES
import UTILS
import CONTENT

UTILS.STYLE_SETUP()

st.image("app/src/images/META_logo.png", width=150)

CONTENT.PORTFOLIO_THEORY()

st.markdown("### Escolha o algoritmo para resolver o problema:")
ALGORITHMS = ["Selecione o metodo de otimização", "Firefly", "Outro"]
SELECTED_ALGORITHM = st.selectbox("Selecione:", ALGORITHMS)

if SELECTED_ALGORITHM == "Firefly":
    st.markdown("""
    ### Selecione a instância:
    """)
    INSTANCES.PORTFOLIO_INSTANCES_SETUP(SELECTED_ALGORITHM)

elif SELECTED_ALGORITHM == "Outro":
    st.markdown("""
    ### Selecione a instância:
    """)
    INSTANCES.PORTFOLIO_INSTANCES_SETUP(SELECTED_ALGORITHM)