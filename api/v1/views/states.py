#!/usr/bin/python3
""" """
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify


@app_views.route('/states', strict_slashes=False)
def states():
    stts = []
    for st in storage.all(State).values():
        stts.append(st.to_dict())
    return jsonify(stts)
