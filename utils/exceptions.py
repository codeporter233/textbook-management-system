class CustomHTTPException(Exception):
    def __init__(self, code: int, message: str = None):
        self.code = code
        self.message = message


_code_message = {
    -1: "token失效",
    -2: "账户名或密码错误",
    -3: "参数错误",
    -4: "无此用户",
    -5: "访问过快",
    -6: "查询失败",
    -7: "查询失败",
}


def custom_abort(code: int, message: str = None):
    if not message:
        message = _code_message.get(code, '未知错误')
    raise CustomHTTPException(code, message)
