# -*- coding:utf-8 -*-
from app.config import secure

__author__ = 'gjw'
__date__ = '2018/1/26 15:46'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建一个新的应用
app = Flask(__name__)
# 连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = secure.SQLALCHEMY_DATABASE_URI
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 安全码
app.config["SECRET_KEY"] = secure.SECRET_KEY


db = SQLAlchemy(app)
db.init_app(app)

