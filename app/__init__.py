#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_uploads import UploadSet, configure_uploads, patch_request_class

#数据库对象
db = SQLAlchemy()
#图片对象
photos = UploadSet('PHOTO')

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

    #将 app 的 config 配置注册到 UploadSet 实例 photos
    configure_uploads(app, photos)
    # 配置上传文件大小，默认64M，设置None则会采用MAX_CONTENT_LENGTH配置选项
    patch_request_class(app, size=None)

    #注册蓝图
    from app.main import main
    app.register_blueprint(main, url_prefix='')   #默认首页
    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    from app.uploads import uploads
    app.register_blueprint(uploads, url_prefix='/uploads')

    return app