#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os, random
from datetime import datetime
from math import ceil
from . import uploads
from flask import render_template, request, redirect, url_for
from .forms import PhotosForm
from ..models.uploadsdb import Photo
from .. import db, photos


# 生成随机32位的字符串
def random_string(length=32):
    base_str = 'qwertyuioplkjhgfdsazcxvbnm0123456789'
    filename = datetime.utcnow().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(base_str) for i in range(length))
    return filename

@uploads.route('/uploadsphoto', methods=['GET', 'POST'])
def uploadsphoto():
    form = PhotosForm()
    if form.validate_on_submit():
        # 生成随机的文件名
        suffix = os.path.splitext(form.PhotoName.data.filename)[1]
        filename = random_string() + suffix
        filename = photos.save(request.files['PhotoName'], name=filename)
        if filename:
            photo = Photo(PhotoInfo=form.PhotoInfo.data, PhotoName=filename, PhotoRemarks=form.PhotoRemarks.data)
            db.session.add(photo)
            db.session.commit()
        return redirect(url_for('uploads.showphotos'))
    return render_template('uploads/uploadsphoto.html', title='上传图片', form=form)

@uploads.route('/showphotos')
def showphotos():
    page = request.args.get('page', 1, type=int)
    max_pic = 6 #6张图片
    pagination = Photo.query.order_by(Photo.timestamp.desc()).paginate(page, per_page=max_pic, error_out=False)
    photos = pagination.items
    lsId = ['' for i in range(max_pic)]
    lsName = ['' for i in range(max_pic)]
    i = 0
    for photo in photos:
        lsId[i] = photo.id
        lsName[i] = photo.PhotoName
        i = i + 1
    return render_template('uploads/showphoto.html', title='显示图片', lsId=lsId, lsName=lsName, pagination=pagination)