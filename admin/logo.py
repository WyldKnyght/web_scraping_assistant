# \admin\logo.py

import os
import base64
import streamlit as st

@st.cache_data(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    current_folder = os.path.dirname(__file__)
    project_folder = os.path.abspath(os.path.join(current_folder, '..'))
    image_path = os.path.join(project_folder, 'images', png_file)

    with open(image_path, "rb") as f:
        data = f.read()

    return base64.b64encode(data).decode()
def build_markup_for_logo(png_file, background_position="50% 10%", margin_top="10%", image_width="60%", image_height=""):
    binary_string = get_base64_of_bin_file(png_file)
    return """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url("data:image/png;base64,%s");
                    background-repeat: no-repeat;
                    background-position: %s;
                    margin-top: %s;
                    background-size: %s %s;
                }
            </style>
            """ % (binary_string, background_position, margin_top, image_width, image_height)

def add_logo(png_file):
    logo_markup = build_markup_for_logo(png_file)
    st.markdown(logo_markup, unsafe_allow_html=True)
