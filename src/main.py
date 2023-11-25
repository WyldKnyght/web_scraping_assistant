# /src/app/main.py

import subprocess

# Start the Streamlit web app
web_app_process = subprocess.Popen(['streamlit', 'run', 'src/user_interface/web_ui.py'])

# Wait for the Streamlit web app to finish
web_app_process.wait()
