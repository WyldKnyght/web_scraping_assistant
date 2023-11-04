# \src\main.py

# Importing only required function from web_ui module
from web_ui import app

# Applying nest_asyncio to allow asyncio to work with Flask
import nest_asyncio

# Applying nest_asyncio only when the script is run as the main program
if __name__ == '__main__':
    nest_asyncio.apply()

    # Running the Flask app in debug mode
    app.run(debug=True)