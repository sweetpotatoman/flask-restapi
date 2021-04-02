class Config:
    SECRET_KEY = 'onemoretime'
    
    
    
    # database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/weakee'
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    # swagger
    SWAGGER_TITLE = "API"
    SWAGGER_DESC = "API接口"
    SWAGGER_HOST = "localhost:5000"

    # loggin
    LOG = {
        "LEVEL": "DEBUG",
        "DIR": "logs",
        "SIZE_LIMIT": 1024 * 1024 * 5,
        "REQUEST_LOG": True,
        "FILE": True,
    }