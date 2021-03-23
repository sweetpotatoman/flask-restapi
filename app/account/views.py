from flask_restful import Resource, fields, marshal_with, request

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