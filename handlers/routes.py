import datetime
from flask import  jsonify
import hashlib
import json
from datetime import datetime

from decouple import config



def configure_routes(app, redis_client):

    SECRET_KEY = config('SECRET_KEY')

    def generate_uuid(date: str, salt=SECRET_KEY) -> str:
        encrypted = hashlib.md5(str(date + salt).encode()).hexdigest()
        return encrypted

    @app.route("/", methods=['GET', 'POST'])
    def get_record():
        date_key = str(datetime.now()).replace('T', ' ')
        uuid = generate_uuid(date_key)

        timedata = redis_client.get('timedata') if b'timedata' in redis_client.keys() else '{}'

        timedata = json.loads(timedata)
        timedata = {date_key: uuid, **timedata}
        redis_client.set('timedata', json.dumps(timedata))
        redis_client.save()

        return jsonify(timedata)
