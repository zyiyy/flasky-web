import os
from app import create_app, db
from app.models import User, Role, Post
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def deploy():
    from app import db
    from app.models import User, Role, Post

    db.drop_all()
    db.create_all()

    Role.insert_roles()

    u = User(email="1919191234@qq.com", username="zouyi", password="zyywan", confirmed=True)
    db.session.add(u)
    uu = User(email="test@qq.com", username="test", password="test", confirmed=True)
    db.session.add(uu)

    User.generate_fake(100)
    Post.generate_fake(100)

    User.add_self_follows()

    db.session.commit()


if __name__=="__main__":
    manager.run()