#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired, Length

class PhotosForm(FlaskForm):
    PhotoInfo = StringField('图片简介', validators=[DataRequired('图片简介不能为空'), Length(1, 64)])
    PhotoName = FileField('图片文件', validators=[DataRequired()])
    PhotoRemarks = TextAreaField('图片简介', validators=[DataRequired('图片备注不能为空'), Length(1, 128)])
    submit = SubmitField('上传图片')