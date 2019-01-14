#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from .. import db

class Post(db.Model):
    '''存放留言信息的数据库表'''
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    author_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __repr__(self):
        return '<body %r>' % self.body
