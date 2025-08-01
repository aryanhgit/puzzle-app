from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import DevConfig
from models import Posts, User
from extension import db
from posts import post_ns
from auth import auth_ns

# Create Flask app and load config
app = Flask(__name__)
app.config.from_object(DevConfig)

# Initialize extensions
db.init_app(app)

migrate = Migrate(app, db)
jwt = JWTManager(app)

# Set up Flask-RESTX API 
api = Api(app) 
api.add_namespace(post_ns)
api.add_namespace(auth_ns)

# Shell context for Flask CLI
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Posts': Posts, 'User': User}