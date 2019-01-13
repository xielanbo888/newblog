#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, redirect, url_for, request
from . import main
from flask_login import login_required,current_user
from .forms import PostForm
from ..models.post import Post
from .. import db

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, User=current_user._get_current_object())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    #posts = Post.query.order_by(Post.timestamp.desc()).all()
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=5, error_out=False)
    posts = pagination.items
    return render_template('main/index.html', form=form, posts=posts, pagination=pagination, title='首页')
    #return render_template('main/main.html', title='首页')

@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

# @main.route('/guanli', methods=['GET', 'POST'])
# def guanli():
#     return render_template('main/guanli.html', title='管理')
