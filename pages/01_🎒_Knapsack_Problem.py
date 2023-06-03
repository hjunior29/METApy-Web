import streamlit as st
import func
import text

st.image("images/META_logo.png", width=150)

func.style_setup()

text.knapsack_theory()

st.markdown("### Escolha o algoritmo para resolver o problema:")
algorithms = ["Selecione o metodo de otimização","Firefly"]
selected_algorithm = st.selectbox("Selecione:", algorithms)

if selected_algorithm == "Firefly":
    st.markdown("""
    ### Selecione a instância
    """)
    func.instance_setup()