#!/usr/bin/python3
""" create a simple api that returns the status ok """


from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_request(self):
    """ close storage """
    return storage.close()


if __name__ == "__main__":
    h = os.getenv('HBNB_API_HOST')
    p = os.getenv('HBNB_API_PORT')
    if not p and not h:
        app.run(host=h, port=p, threaded=True)
    else:
        app.run(host='0.0.0.0', port='5000', threaded=True)
