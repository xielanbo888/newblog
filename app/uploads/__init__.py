#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

uploads = Blueprint('uploads', __name__)

from . import views

