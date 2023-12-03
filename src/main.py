# \src\main.py

from user_interface.web_ui import run_web_app
from model_handler.model_handler import initialize_model

if __name__ == "__main__":
    # Initialize the model
    initialize_model()

    # Run the web app
    run_web_app()
