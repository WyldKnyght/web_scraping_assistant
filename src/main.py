# \src\main.py

from flask import Flask, render_template, request
from web_ui import app

if __name__ == '__main__':
    app.run(debug=True)
