#\src\routes\__init__.py

from flask import Blueprint
from .home import home_bp

routes = Blueprint('routes', __name__)

# Import additional route files here
# from .other_route import *
