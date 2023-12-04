import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_blog2.config import Config


basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def  create_app(config_config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    template_dir = os.path.join(basedir, 'templates')
    app.template_folder = template_dir

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Blueprint
    from flask_blog2.users.routes import users
    from flask_blog2.posts.routes import posts
    from flask_blog2.main.routes import main
    from flask_blog2.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app