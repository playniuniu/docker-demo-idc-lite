# coding: utf-8

from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'机房状态',
        user_name=u'于旸',
        user_role=u'客户')
