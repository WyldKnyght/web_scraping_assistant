from flask import Blueprint

routes = Blueprint('routes', __name__)

from .home import *

# Import additional route files here
# from .other_route import *
