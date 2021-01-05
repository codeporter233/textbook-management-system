from datetime import datetime, timedelta

import jwt

jwt_secret = "bu8X4q51fi7KnDSRWk3OjCx46Dqb1RBL"


def generate_jwt(payload: dict, expiry: datetime = datetime.utcnow() + timedelta(days=0, seconds=60 * 10)):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :return: jwt
    """
    payload.update({'exp': expiry})
    token = jwt.encode(payload, jwt_secret)
    return token.decode()


def verify_jwt(token):
    """
    验证jwt
    :param token: jwt
    :return: dict: payload
    """

    payload = jwt.decode(token, jwt_secret)
    return payload
