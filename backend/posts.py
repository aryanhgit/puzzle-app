from flask import request
from flask_restx import Api, Resource, fields, Namespace
from flask_jwt_extended import JWTManager, jwt_required
from models import Posts

post_ns = Namespace('posts', description='Posts related operations')

# Define the API model for posts

posts_model = post_ns.model(
    'Post', {
        "id": fields.Integer(),
        "title": fields.String(),  
        "content": fields.String(),
    }
)

@post_ns.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello from Posts API!"}


@post_ns.route('/posts')
class PostsListResource(Resource):
    @post_ns.marshal_with(posts_model)
    def get(self):
        """Get all posts"""
        return Posts.query.all()

    # Specifies the expected request payload schema for API documentation and validation purposes
    @post_ns.expect(posts_model)
    @post_ns.marshal_with(posts_model)
    @jwt_required()
    def post(self):
        """Create a new post"""
        data = post_ns.payload
        new_post = Posts(title=data['title'], content=data['content'])
        new_post.save()
        return new_post, 201

@post_ns.route('/posts/<int:id>')
class PostResource(Resource):
    @post_ns.marshal_with(posts_model)
    def get(self, id):
        """Get a post by id"""
        post = Posts.query.get_or_404(id)
        return post

    @post_ns.expect(posts_model)
    @post_ns.marshal_with(posts_model)
    @jwt_required()
    def put(self, id):
        """Update a post by id"""
        update_post = Posts.query.get_or_404(id)
        data = post_ns.payload
        update_post.update(title=data['title'], content=data['content'])
        return update_post

    @post_ns.marshal_with(posts_model)
    @jwt_required()
    def delete(self, id):
        """Delete a post by id"""
        delete_post = Posts.query.get_or_404(id)
        delete_post.delete()
        return ({'message': 'Post deleted successfully'}), 200
