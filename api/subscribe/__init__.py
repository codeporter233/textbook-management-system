from flask import Blueprint

api = Blueprint("subscribe", __name__, url_prefix="/subscribe")

from .subscribe import *
