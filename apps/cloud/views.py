from flask_restful import Resource, fields, marshal_with, request
from exts import db


class (Resource):
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
