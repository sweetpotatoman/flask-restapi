from exts import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))

class Foo(db.Model):
    __tablename__ = 'foo'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.INTEGER)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128))

class ApiToken(db.Model):
    __tablename__= 'api_token'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    token = db.Column(db.String(128), nullable=False)