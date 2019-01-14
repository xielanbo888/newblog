#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from .. import db

class Photo(db.Model):
    '''存储图片信息的数据库表'''
    __tablename__ = 'photos' #表名

    id = db.Column(db.Integer, primary_key=True)
    PhotoInfo = db.Column(db.String(64), unique=True) #图片简介
    PhotoName = db.Column(db.String(128), unique=True) #图片名称
    PhotoRemarks = db.Column(db.Text) #图片备注
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow()) #上传时间戳

    def __repr__(self):
        return '<PhotoInfo %r>' % self.PhotoInfo
