class Config:
    SECRET_KEY = 'onemoretime'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/weakee'
    # 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名 data_base
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SWAGGER_TITLE = "API"
    SWAGGER_DESC = "API接口"
    SWAGGER_HOST = "localhost:5000"