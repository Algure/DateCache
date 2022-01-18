
import hashlib
import json
from datetime import datetime
import redis

from decouple import config
from flask import Flask, jsonify, session

from handlers.routes import configure_routes

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
redis_client = redis.StrictRedis(host=config('REDIS_HOST'), port=int(config('REDIS_PORT')), db=0, socket_timeout=20)

configure_routes(app, redis_client)

if __name__ == "__main__":
    app.run( host="0.0.0.0")