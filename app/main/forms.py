#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[DataRequired('输入不能为空!')])
    submit = SubmitField('Submit')