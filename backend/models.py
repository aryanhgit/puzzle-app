from extension import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # def update(self, username=None, email=None, password_hash=None):
    #     if username is not None:
    #         self.username = username
    #     if email is not None:
    #         self.email = email
    #     if password_hash is not None:
    #         self.password_hash = password_hash
    #     db.session.commit()


class Posts(db.Model):
    # __tablename__ = 'posts'  # Explicit table name for clarity

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)  # Add timestamp

    def __repr__(self):
        return f"<Post {self.title}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, content):
        # Allow partial updates
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        db.session.commit() 
