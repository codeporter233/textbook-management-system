from flask import Blueprint

api = Blueprint("attribution", __name__, url_prefix="/attribution")

from .attribution import *
