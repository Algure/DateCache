import redis
from decouple import config

r = redis.StrictRedis(host=config('REDIS_HOST'), port=int(config('REDIS_PORT')), db=0)
