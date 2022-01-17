from random import random

import redis
from flask import Flask, request, jsonify
import requests
from flask_caching import Cache

app = Flask(__name__)

app.config.from_object('config.Config')
# Create and initialize the Flask-Session object AFTER `app` has been configured
cache = Cache(app)


def generate_random_code(str_size):
    allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

@app.route("/", methods = ['GET','POST'])
def get_saved_times():

    search = request.args.get('country')
    r = requests.get(f"{API_URL}{search}")
    return jsonify(r.json())



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)