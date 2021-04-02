import requests
import json

from flask_restful import Resource, fields, marshal_with, request
from exts import db
from models import ApiToken
from utils.restful_utils import success, params_error


class CloudObjectList(Resource):
    # resource_fields = {
    #     'id': fields.Integer,
    #     'username': fields.String,
    # }

    # @login_required
    # @marshal_with(resource_fields)
    def get(self):
        token_pre = db.session.query(ApiToken).get(1)
        token = token_pre.token

        logUrl = 'http://192.168.20.92:9094/console/api/v1/object/list'
        params = {
            "kind": ["SERVICE"],
            "nameSpace": "fxcore",
            "opStatus": "UNLOCK",
            "statues": ["RUNNING","PENDING","READY"],
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token,
        }
        res = requests.post(logUrl, data=json.dumps(params), headers=headers)
        result = json.loads(res.text)
        # print(result["data"])
        context = {}
        context["data"] = result["data"]
        return success("查询列表", data=context)


class CloudObjectNode(Resource):
    def get(self):
        token = db.session.query(ApiToken).first().token
        
        logUrl = 'http://192.168.20.92:9094/console/api/v1/object/node/info'
        params = {
            "kind": "NODE",
            "nameSpace": "test",
            "name": "seed-node"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token,
        }
        res = requests.post(logUrl, data=json.dumps(params), headers=headers)
        result = json.loads(res.text)
        # print(result["data"])
        context = {}
        context["data"] = result["data"]
        return success("查询 node 列表", data=context)

class CloudObjectNode(Resource):
    def get(self):
        token = db.session.query(ApiToken).first().token
        
        logUrl = 'http://192.168.20.92:9094/console/api/v1/object/node/info'
        params = {
            "kind": "NODE",
            "nameSpace": "test",
            "name": "seed-node"
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token,
        }
        res = requests.post(logUrl, data=json.dumps(params), headers=headers)
        result = json.loads(res.text)
        # print(result["data"])
        context = {}
        context["data"] = result["data"]
        return success("查询 node 列表", data=context)