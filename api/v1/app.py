#!/usr/bin/python3
""" create a simple api that returns the status ok """


from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ close storage file or database """
    return storage.close()


if __name__ == "__main__":
    h = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    p = os.getenv('HBNB_API_PORT', default='5000')
    app.run(host=h, port=int(p), threaded=True)
