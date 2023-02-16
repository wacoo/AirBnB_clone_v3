#!/usr/bin/python3
""" create a view blueprint and import many modules """


from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')
from api.v1.views.index import *