from exts import db
from passlib.apps import custom_app_context as pwd_context

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

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

class ApiToken(db.Model):
    __tablename__= 'api_token'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    token = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return self.token