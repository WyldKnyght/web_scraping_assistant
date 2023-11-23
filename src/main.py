# /src/app/main.py

import streamlit as st
import subprocess

# Start the Streamlit web app
web_app_process = subprocess.Popen(['streamlit', 'run', 'src/user_interface/web_ui_app.py'])

# Wait for the Streamlit web app to finish
web_app_process.wait()
