from flask import Blueprint


app1 = Blueprint('app1', __name__)

from . import views_demo1
