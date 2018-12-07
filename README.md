# flasky-web
Flask Web应用开发实战

1.项目简介

这是根据Flasky Web应用开发实战一书写的博客系统, 跟原来的系统比增加了删除评论功能, 删减了修改密码和修改邮箱地址功能.

注释中包含个人学习中遇到的坑, 以及需要注意的地方. 

浏览器地址栏输入58.87.77.210预览网站.

2.如何在本地运行

2.1 下载源码后，进入venv文件夹，执行以下命令安装相关库：pip install -r requirements.txt.

2.2 找到config.py 修改配置文件, 需要修改的有:

FLASK_MAIL_SENDER, 这是你给用户发邮件使用的邮箱地址.

FLASK_ADMIN, 这是管理员的邮箱地址, 如果使用这个邮箱注册系统默认分配的用户角色就是Admin.

MAIL_USERNAME和MAIL_PASSWORD, 这两个配置项是你发邮箱使用的邮箱地址和你的smtp协议的授权码, 注意不是邮箱的密码. 出于安全考虑,
这两个从环境变量中读取, 你需要在环境变量中设置这两个配置项.

2.3 这些都配置好了之后, 进入包含manage.py的文件夹, 执行命令 python manage.py deploy 初始化数据库

执行python manage.py runserver, 项目就可以成功在你本地运行起来啦

有任何问题, 欢迎联系我, 邮箱: 1919191234@qq.com
