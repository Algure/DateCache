import unittest

import app

from app import app

def test_endpoint():
    rv = app.get('/',)
    # json_data = rv.get_json()

    print(f'rv: {rv}')
    # assert


if __name__ == "__main__":
    test_endpoint()