#!/usr/bin/python3

""" create a route that returns OK status code """

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', strict_slashes=False)
def index():
    """ return status code OK """
    return jsonify({'status': 'OK'})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """ list objects and their counts in storage """
    st_dict = {}
    objects = ["Amenity", "City", "Place", "Review", "State", "User"]
    for obj in objects:
        if obj == "Amenity":
            st_dict["amenities"] = storage.count(obj)
        elif obj == "City":
            st_dict["cities"] = storage.count(obj)
        elif obj == "Place":
            st_dict["places"] = storage.count(obj)
        elif obj == "Review":
            st_dict["reviews"] = storage.count(obj)
        elif obj == "State":
            st_dict["states"] = storage.count(obj)
        elif obj == "User":
            st_dict["users"] = storage.count(obj)
    return jsonify({"stats": st_dict}) 
