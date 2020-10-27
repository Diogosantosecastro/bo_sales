from flask import Blueprint
artigos = Blueprint('artigos', __name__)

from . import views
