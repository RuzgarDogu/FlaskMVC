import os
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

# Uygulamamızda kullandığımız eklentileri init ediyoruz.
# Alttakiler eklentilerin instance'ı
db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()
# account route'ında login_required verdik, ama eğer login değillerse nereye gideceğini
# söylemek için aşağıdaki login_view rotasını belirtmemiz lazım. >> Eklenti fonksiyonu
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

# Circular hatasına düşmemek için route'ları en sonda tanımladık.
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    for root, dirs, files in os.walk("./flaskblog/controllers", topdown=True):
        for name in dirs:
            if name != '__pycache__':
                package = f'flaskblog.controllers.{name}.routes'
                imported = getattr(__import__(package, fromlist=[name]), name)
                print(imported)
                app.register_blueprint(imported)

    for root, dirs, files in os.walk("./flaskblog/api", topdown=True):
        for name in dirs:
            if name != '__pycache__':
                package = f'flaskblog.api.{name}.routes'
                imported = getattr(__import__(package, fromlist=[name]), name)
                app.register_blueprint(imported)

    return app
