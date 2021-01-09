from functools import wraps

from flask import request
from jwt import ExpiredSignatureError

from utils import jwt_utils
from utils.exceptions import custom_abort


def token_required(func):
    """
    检查token, 并刷新token
    :param func: 被装饰函数
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        if token:
            try:
                payload = jwt_utils.verify_jwt(token)
                user_id = request.args.get('user_id')
                if user_id != payload['user_id']:
                    custom_abort(-2, '未知用户')
                res = func(*args, **kwargs)
                res['token'] = jwt_utils.generate_jwt(payload)
                return res
            except ExpiredSignatureError:
                custom_abort(-1, "token失效")
        else:
            custom_abort(-1, '未携带token')

    return wrapper

