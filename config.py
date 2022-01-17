
import os
import redis
from decouple import config


class BaseConfig(object):
    SESSION_TYPE = config('SESSION_TYPE')
    SESSION_PERMANENT = config('SESSION_PERMANENT')
    SESSION_USE_SIGNER = config('SESSION_USE_SIGNER')
    SESSION_REDIS = redis.from_url(config('REDIS_URL'))



