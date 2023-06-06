import streamlit as st
import os

def STYLE_SETUP():
    streamlit_style = """
    <style>
        html, body, [class*="css"]  {
            text-align: justify;
        }
        /* Selecionar a barra de rolagem vertical */
        ::-webkit-scrollbar {
            width: 12px;
        }
    </style>
    """
    st.markdown(streamlit_style, unsafe_allow_html=True)

def GET_LATEST_FILE(PATH):
    LIST_OF_FILE = [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]
    LATEST_FILE = max(LIST_OF_FILE, key=lambda x: os.path.getctime(os.path.join(PATH, x)))

    return LATEST_FILE