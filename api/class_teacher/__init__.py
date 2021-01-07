from flask import Blueprint

api = Blueprint("class_teacher", __name__, url_prefix="/class")

from .class_teacher import *