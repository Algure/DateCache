
from app import *

def is_key_date(key: str) -> bool:
    for c in key:
        test = ord(c)
        if (test >= 97 and test <= 122) or (test >= 65 and test <= 90):
            return False
    return True


def test_base_route():
    app = Flask(__name__)
    client = app.test_client()

    redis_client = redis.StrictRedis(host=config('TEST_REDIS_HOST'), port=int(config('TEST_REDIS_PORT')), db=0,
                                     socket_timeout=20)
    configure_routes(app, redis_client)

    url = '/'
    response = client.get(url)

    assert response.status_code == 200

    data = response.get_data().decode("utf-8")
    data = json.loads(data)

    assert type(data) is dict

    dformat = "%Y-%m-%d %H:%M:%S"

    #Check if dates are returned from earliest to first
    presentdate = None
    pastdate  = None
    for date in data:
        if presentdate is None:
            continue
        pastdate = presentdate
        presentdate =  datetime.strptime(date, dformat)

        assert presentdate <= pastdate





