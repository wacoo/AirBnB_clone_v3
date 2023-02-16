#!/usr/bin/python3

""" create a route that returns OK status code """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def index():
    """ return status code OK """
    return jsonify({'status': 'OK'})
