import hashlib
import json
from datetime import datetime
from collections import OrderedDict

from decouple import config
from flask import Flask, jsonify, session
from flask_session import Session

SECRET_KEY = config('SECRET_KEY')

app = Flask(__name__)

app.secret_key = SECRET_KEY

app.config.from_object('config.BaseConfig')

server_session = Session(app)

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

    timedata = session['timedata'] if 'timedata' in session.keys() else {}
    timedata = {date_key:uuid, **timedata }
    session['timedata'] = timedata

    return jsonify(timedata, sort_keys=False)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)