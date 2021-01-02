from . import api


@api.route("/books/all", methods=["GET"])
def handle_ningkangyun():
    sql = "select * from ....."
    # 这里执行sql，并返回相应的结果
    return {
        "code": 0,
        "books": ["高等数学", "线性代数"]
    }
