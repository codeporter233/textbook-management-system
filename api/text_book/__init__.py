from flask import Blueprint

api = Blueprint("text_book", __name__, url_prefix="/text_book")

from .text_book import *
