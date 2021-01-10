from flask import Blueprint

api = Blueprint("class_teacher", __name__, url_prefix="/class_teacher")

from .class_teacher import *