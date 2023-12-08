# \src\user_interface\ui_functions\get_user_input.py

import streamlit as st

def get_user_input_url():
    url = st.text_input("Enter website URL")
    return url