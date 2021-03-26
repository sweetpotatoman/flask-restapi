from flask_restful import Resource, fields, marshal_with, request
from werkzeug.security import check_password_hash, generate_password_hash
from exts import db
import functools
import json

datas = [{'id': 1, 'name': 'xag', 'age': 18}, {'id': 2, 'name': 'xingag', 'age': 19}]

class UserView(Resource):
    """
    通过继承 Resource 来实现调用 GET/POST 等动作方法
    """
    def get(self):
        return {'code': 200, 'msg': 'success', 'data': datas}


    def post(self):
        # 参数数据
        json_data = request.get_json()

        # 追加数据到列表中
        new_id = len(datas)+1
        datas.append({'id':new_id,**json_data})

        # 返回新增的最后一条数据
        return {'code': 200, 'msg': 'ok', 'success': datas[new_id - 1]}


class UserLogin(Resource):
    def post(self):
        resource_fields = {
            'id': fields.Integer,
            'name': fields.String,
            'age': fields.String
        }
        json_data = request.get_json()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view