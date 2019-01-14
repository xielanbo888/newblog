#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_C0MMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flask>@example.com'
    FLASKY_ADMIN = os.environ.get('FLASK_ADMIN')

    #图片上传参数
    UPLOADED_PHOTO_DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app/static/photos")
    UPLOADED_PHOTO_ALLOW = ['jpg', 'jpeg', 'png']  # 配置允许的扩展名，其他的都是不允许
    MAX_CONTENT_LENGTH =  4 * 1024 * 1024

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUE = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'prodection': ProductionConfig,
    'default': DevelopmentConfig
}