from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options,DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect




#Initiating app extensions
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app(config_name):
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://brian:12345 @localhost/book'
    
    
      # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    
    
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    
    
    #Registering the auth Blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    
    # Registering the  main Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Setting config
    # from .request import configure_request
    # configure_request(app)
    app.config.from_object(DevConfig)
    app.config['SECRET_KEY'] = 'online5'
    app.config['WTF_CSRF_SECRET_KEY'] = 'online5'
    
    
    return app