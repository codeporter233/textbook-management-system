import hashlib
from functools import wraps
from flask import request
from redis_connect import redis_cache
import json


def cache(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = request.path
        for i in dict(request.args):
            if key == "token":
                continue
            key += i
        hash_key = hashlib.md5(key.encode()).hexdigest()
        cached = redis_cache.get(hash_key)
        if cached:
            print("命中缓存")
            return json.loads(cached)
        else:
            res = func(*args, **kwargs)
            redis_cache.set(hash_key, json.dumps(res), ex=3)
            return res
    return wrapper
