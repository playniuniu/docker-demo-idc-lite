# coding: utf-8

from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html',
        web_title=app.config['WEB_TITLE'],
        content_title='客户概览',
        user_name='北京蓝汛',
        user_role='金石IDC客户')


@app.route('/maintain')
def maintain():
    return render_template('pages/maintain.html',
        web_title=app.config['WEB_TITLE'],
        content_title='设备维护',
        user_name='北京蓝汛',
        user_role='金石IDC客户')


@app.route('/safe')
def safe():
    return render_template('pages/safe.html',
        web_title=app.config['WEB_TITLE'],
        content_title='安全服务',
        user_name='北京蓝汛',
        user_role='金石IDC客户')

@app.route('/seo')
def seo():
    return render_template('pages/iframe.html',
        web_title=app.config['WEB_TITLE'],
        content_title='SEO服务',
        user_name='北京蓝汛',
        user_role='金石IDC客户',
        web_url="http://cn.majesticseo.com/")

@app.route('/data')
def data():
    return render_template('pages/data.html',
        web_title=app.config['WEB_TITLE'],
        content_title='数据服务',
        user_name='北京蓝汛',
        user_role='金石IDC客户')

@app.route('/report')
def report():
    return render_template('pages/report.html',
        web_title=app.config['WEB_TITLE'],
        content_title='月度报表',
        user_name='北京蓝汛',
        user_role='金石IDC客户')

@app.route('/device')
def device():
    return render_template('pages/device.html',
        web_title=app.config['WEB_TITLE'],
        content_title='机房资产',
        user_name='北京蓝汛',
        user_role='金石IDC客户')


@app.route('/flow')
def flow():
    return render_template('pages/flow.html',
        web_title=app.config['WEB_TITLE'],
        content_title='流量统计',
        user_name='北京蓝汛',
        user_role='金石IDC客户')


@app.route('/billing')
def billing():
    return render_template('pages/billing.html',
        web_title=app.config['WEB_TITLE'],
        content_title='费用查询',
        user_name='北京蓝汛',
        user_role='金石IDC客户')


@app.route('/buy')
def buy():
    return render_template('pages/buy.html',
        web_title=app.config['WEB_TITLE'],
        content_title='企业套餐',
        user_name='北京蓝汛',
        user_role='金石IDC客户')

