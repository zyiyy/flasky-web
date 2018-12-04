# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))    # 文件名->文件所在文件夹路径->文件所在文件夹绝对路径


class Config:

    # SECRET_KEY配置变量是通用密钥, 用于加密函数, 可在Flask和多个第三方扩展中使用
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hard to guess string"

    # 每次请求结束后自动提交数据库的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 邮件配置
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '1919191234@qq.com'

    # 通过注册邮箱设置管理员
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or "1919191234@qq.com"

    # 设置每页显示的记录数量
    FLASK_POSTS_PER_PAGE = 10
    FLASKY_COMMENTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):    # 声明一个子类, 继承自Config类
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                               'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


