import hashlib
import json
from datetime import datetime
import redis

from decouple import config
from flask import Flask, jsonify, session

SECRET_KEY = config('SECRET_KEY')

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


r = redis.StrictRedis(host= config('REDIS_HOST'), port=int(config('REDIS_PORT')), db=0)


def generate_uuid(date:str, salt = SECRET_KEY) -> str:
    encrypted = hashlib.md5(str(date + salt).encode()).hexdigest()
    return encrypted


def is_key_date(key:str) -> bool:
    for c in key:
        test = ord(c)
        if (test >= 97 and test <= 122 ) or (test >= 65 and test <= 90):
            return False
    return True


@app.route("/", methods = ['GET','POST'])
def get_record():
    date_key = str(datetime.now()).replace('T', ' ')
    uuid = generate_uuid(date_key)

    timedata = r.get('timedata') if b'timedata' in r.keys() else '{}'

    timedata = json.loads(timedata)
    timedata = {date_key:uuid, **timedata }
    r.set('timedata', json.dumps(timedata))
    r.save()

    print(f'timedata: {timedata}')
    return jsonify(timedata)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)