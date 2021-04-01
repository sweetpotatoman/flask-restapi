from flask import Flask, Blueprint
from flask_restful import Api
from exts import db
from config import Config
from apps.foo.views import FooApi, FooListApi
from apps.account.views import UserView, UserLogin, UserRegister
from apps.cloud.views import CloudObjectList, CloudObjectNode
from flasgger import Swagger



# 定义蓝图，main为蓝图名字
main = Blueprint('main', __name__)
# 实例化api
api = Api(main)

# 设置路由
api.add_resource(UserView, '/user/info')
api.add_resource(UserLogin, '/user/login')
api.add_resource(UserRegister, '/user/register')
api.add_resource(FooListApi, '/api/v1/foos')
api.add_resource(FooApi, '/api/v1/foo', '/api/v1/foo/<int:id>')
api.add_resource(CloudObjectList, '/api/cloud/object')
api.add_resource(CloudObjectNode, '/api/cloud/object/node')
# api.add_resource(Cloudapi,)


# 函数工厂
def create_app():
    # 初始化 flask
    app = Flask(__name__)
    # 从对象设置配置信息
    app.config.from_object(Config)
    # 第三方扩展初始化
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(main)

    # 添加 swagger 支持
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = Config.SWAGGER_TITLE    # 配置大标题
    swagger_config['description'] = Config.SWAGGER_DESC    # 配置公共描述内容
    swagger_config['host'] = Config.SWAGGER_HOST    # 请求域名
    swagger = Swagger(app, config=swagger_config)

    return app
