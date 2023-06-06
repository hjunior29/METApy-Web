import streamlit as st
import UTILS
import CONTENT

st.set_page_config(layout="wide", page_icon="app/src/images/META_logo.png")

UTILS.STYLE_SETUP()

st.image("app/src/images/META_logo.png", width=150)

CONTENT.ABOUT()