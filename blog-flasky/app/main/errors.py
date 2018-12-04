# coding=utf-8

from flask import render_template
from . import main


# 找不到页面
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 服务器错误
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# HTTP“禁止”错误
@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

