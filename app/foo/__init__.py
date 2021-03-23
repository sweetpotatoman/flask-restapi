# from flask import Blueprint
# from flask_restful import Api
# from app.resources.views import *

# # 定义蓝图，main为蓝图名字
# main = Blueprint('main', __name__)
# # 实例化api
# api = Api(main)

# # 设置路由
# # api.add_resource(TODO, '/index')
# api.add_resource(UserView, '/user')
# api.add_resource(FooListApi, '/api/v1/foos')
# api.add_resource(FooApi, '/api/v1/foo', '/api/v1/foo/<int:id>')
