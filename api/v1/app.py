#!/usr/bin/python3
""" create a simple api that returns the status ok """


from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ close storage file or database """
    return storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ return not found message """
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    h = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    p = os.getenv('HBNB_API_PORT', default='5000')
    app.run(host=h, port=int(p), threaded=True)
