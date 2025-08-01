import unittest
from main import create_app
from config import TestConfig
from extension import db

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    # Testing the authorisation routes
    def test_signup(self):
        response = self.client.post('/auth/signup', json={
            'username': 'testuser',
            'email': 'johndoe@example.com',
            'password_hash': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_login(self):
        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)

    # Testing the posts routes
    def test_get_posts(self):
        response = self.client.get('/posts/posts')
        self.assertEqual(response.status_code, 200)
    
    def test_get_post(self):
        id=1
        response = self.client.get(f'/posts/posts/{id}')
        self.assertEqual(response.status_code, 404)
    
    def test_create_post(self):
        response = self.client.post('/auth/signup', json={
            'username': 'testuser',
            'email': 'johndoe@example.com',
            'password_hash': 'testpassword'
        })

        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        access_token = response.json['access_token']
        # print(access_token)
        headers = {'Authorization': f'Bearer {access_token}'}

        response = self.client.post('/posts/posts', json={
            'title': 'Test Post',
            'content': 'Test content'
        }, headers=headers)

        print(response.json)
        self.assertEqual(response.status_code, 201)
    
    def test_update_post(self):
        response = self.client.post('/auth/signup', json={
            'username': 'testuser',
            'email': 'johndoe@example.com',
            'password_hash': 'testpassword'
        })

        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        access_token = response.json['access_token']
        headers = {'Authorization': f'Bearer {access_token}'}

        response = self.client.post('/posts/posts', json={
            'title': 'Test Post',
            'content': 'Test content'
        }, headers=headers)

        id = 1
        update_response = self.client.put(f'/posts/posts/{id}', json={
            'title': 'Updated Test Post',
            'content': 'Updated test content'
        }, headers=headers)

        self.assertEqual(update_response.status_code, 200)

    def test_delete_post(self):
        response = self.client.post('/auth/signup', json={
            'username': 'testuser',
            'email': 'johndoe@example.com',
            'password_hash': 'testpassword'
        })

        response = self.client.post('/auth/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })

        access_token = response.json['access_token']
        headers = {'Authorization': f'Bearer {access_token}'}

        response = self.client.post('/posts/posts', json={
            'title': 'Test Post',
            'content': 'Test content'
        }, headers=headers)

        id = 1
        update_response = self.client.delete(f'/posts/posts/{id}', json={
            'title': 'Updated Test Post',
            'content': 'Updated test content'
        }, headers=headers)

        self.assertEqual(update_response.status_code, 200)

# Run the tests
if __name__ == '__main__':
    unittest.main()