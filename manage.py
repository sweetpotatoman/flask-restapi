import click

from apps import create_app
from flask_script import Manager
from models import *


app = create_app()
manager = Manager(app)


@manager.command
def initdb():
    # db.drop_all()
    db.create_all()
    click.echo('初始化数据库')


# @manager.command
# def insert():
#     category = Category(name='4321')
#     db.session.add(category)
#     db.session.commit()
#     click.echo('添加一个类别')


if __name__ == '__main__':
    manager.run()
