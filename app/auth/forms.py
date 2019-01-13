#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models.user import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('账号不能为空'), Length(1,64), Email()])
    password = PasswordField('password', validators=[DataRequired('密码不能为空')])
    remember_me = BooleanField('Keep me login in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('email不能为空'), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired('用户名不能为空'), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField('Confirm password', validators=[DataRequired('密码不能为空'), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')