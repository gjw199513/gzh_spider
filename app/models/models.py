# -*- coding:utf-8 -*-
__author__ = 'gjw'
__date__ = '2018/1/26 15:47'

from flask import Flask
from datetime import datetime
from app import db
import pymysql
from flask_sqlalchemy import SQLAlchemy


# 公众号文章
class GzhArticle(db.Model):
    __tablename__ = 'gzh_article'
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(200))  # 标题
    author = db.Column(db.String(100))  # 作者
    img_url = db.Column(db.String(400))  # 图片地址
    content_url = db.Column(db.String(400))  # 文章地址
    publish_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 发布时间
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    # 获得字典的键
    def keys(self):
        # 指明序列化的属性
        return ['id', 'title', 'author', 'img_url',
                'content_url', 'publish_time', 'create_time']

    # 获得字典的值
    def __getitem__(self, item):
        return getattr(self, item)
        # return "11111"


if __name__ == '__main__':
    # 创建数据表
    db.create_all()