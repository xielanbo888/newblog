#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

db = SQLAlchemy()

#
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)

    #配置文件初始化
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #数据库初始化
    db.init_app(app)
    db.app = app

    login_manager.init_app(app)
    bootstrap = Bootstrap(app)
    moment = Moment(app)

    #注册蓝图
    from app.main import main
    app.register_blueprint(main, url_prefix='')   #默认首页
    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app