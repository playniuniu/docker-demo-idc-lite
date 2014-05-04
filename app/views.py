# coding: utf-8

from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'客户概览',
        user_name=u'于旸',
        user_role=u'金石IDC客户')


@app.route('/maintain')
def maintain():
    return render_template('pages/maintain.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'设备维护',
        user_name=u'于旸',
        user_role=u'金石IDC客户')


@app.route('/safe')
def safe():
    return render_template('pages/safe.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'安全服务',
        user_name=u'于旸',
        user_role=u'金石IDC客户')


@app.route('/device')
def device():
    return render_template('pages/device.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'机房资产',
        user_name=u'于旸',
        user_role=u'金石IDC客户')


@app.route('/flow')
def flow():
    return render_template('pages/flow.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'流量统计',
        user_name=u'于旸',
        user_role=u'金石IDC客户')


@app.route('/billing')
def billing():
    return render_template('pages/billing.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'费用查询',
        user_name=u'于旸',
        user_role=u'金石IDC客户')


@app.route('/buy')
def buy():
    return render_template('pages/buy.html',
        web_title=app.config['WEB_TITLE'],
        content_title=u'增值业务',
        user_name=u'于旸',
        user_role=u'金石IDC客户')
