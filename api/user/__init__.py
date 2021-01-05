from flask import Blueprint

api = Blueprint("user", __name__, url_prefix="/user")

from .user import *
