import functools
import json
import requests
# import jwt
from flask_restful import Resource, fields, marshal_with, request, abort
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from exts import db
from models import User, ApiToken
from utils.restful_utils import success, params_error, un_auth_error
# from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth


# auth = HTTPBasicAuth()
# token_m = HTTPTokenAuth()


class UserView(Resource):
    """
    通过继承 Resource 来实现调用 GET/POST 等动作方法
    """
    resource_fields = {
        'id': fields.Integer,
        'username': fields.String,
    }

    # @login_required
    @marshal_with(resource_fields)
    def get(self):
        users = db.session.query(User).all()
        return users

class UserLogin(Resource):
    def post(self):
        params = request.get_json()
        username = params.get("username")
        password = params.get("password")
        if username is None or password is None:
            return un_auth_error("Incorrect username or password.")

        user = User.query.filter_by(username=username, password=password).all()
        if user:
            logUrl = 'http://192.168.20.92:9094/console/api/v1/user/login'
            # request = requests.session()
            params = {
                "username": 'linjiale',
                "password": '123456',
            }
            headers = {
                'Content-Type': 'application/json',
            }

            r = requests.post(logUrl, data=json.dumps(params), headers=headers)
            r_dict = json.loads(r.text)
            token = r_dict['data']['token']
            ApiToken.query.filter_by(id='1').update({'token':token})
            db.session.commit()
            
            session.clear()
            session['user_id'] = user[0].id
            return success("登陆成功")
        else:
            return un_auth_error("账号或者密码不正确")

class UserRegister(Resource):
    def post(self):
        params = request.get_json()
        username = params.get("username")
        password = params.get("password")
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return success("注册成功！", data=user.id)


# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         user_id = session.get('user_id')

#         if user_id is None:
#             return un_auth_error("请登录")
#         else:
#             guser = User.query.filter_by(id=user_id).all()

#         return view(**kwargs)

#     return wrapped_view


# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))

#         return view(**kwargs)

#     return wrapped_view