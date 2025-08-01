from flask_restx import Api, Resource, Namespace, fields
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import Posts, User
from extension import db

auth_ns = Namespace('auth', description='Authentication related operations')


signup_model = auth_ns.model(
    'SignUp',
    {
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "password_hash": fields.String(required=True),
    }
)

login_model = auth_ns.model(
    'Login',
    {
        "username": fields.String(required=True),
        "password": fields.String(required=True),
    }
)

@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(signup_model, validate=True)
    def post(self):
        data = auth_ns.payload

        # Check if user already exists by username or email
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()

        if existing_user:
            return ({'message': f"User '{data['username']}' already exists"}), 200

        # Create new user with hashed password
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=generate_password_hash(data['password_hash']) 
        )
        new_user.save()

        return ({'message': f"User '{data['username']}' created successfully"}), 201 


@auth_ns.route("/login")
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self):
        data = auth_ns.payload

        username = data.get("username")
        password = data.get("password")

        db_user = User.query.filter_by(username=username).first()

        if db_user and check_password_hash(db_user.password_hash, password):
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)

            return ({"access_token": access_token, "refresh_token": refresh_token})

        else:
            return ({"message": "Invalid username or password"})
        
@auth_ns.route('/refresh')
class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return ({"access_token": new_access_token})