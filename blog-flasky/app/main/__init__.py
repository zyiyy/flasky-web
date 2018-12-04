# coding=utf-8

from flask import Blueprint

main = Blueprint('main', __name__)


# 使用上下文处理器让变量在所有模板中全局可访问
from ..models import Permission


# 把Permission类加入模板上下文
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


from . import views, errors

