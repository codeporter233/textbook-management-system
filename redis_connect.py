import redis
from private_settings import redis_password, redis_host, redis_port

redis_cache = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password,
                                encoding='utf8', decode_responses=True, db=5)