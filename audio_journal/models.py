from datetime import datetime
from audio_journal import db, login_manager
from flask_login import UserMixin
from sqlalchemy import LargeBinary


@login_manager.user_loader
def load_user(user_id):
    """
    Callback function to load a user object based on the user ID stored in the session.

    Parameters:
    - user_id (str): The user ID retrieved from the session.

    Returns:
    User: The user object corresponding to the provided user ID.
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    Database model representing a user in the application.

    Attributes:
    - id (int): Primary key identifying the user.
    - username (str): Unique username for the user (maximum length: 20 characters).
    - email (str): Unique email address for the user (maximum length: 120 characters).
    - image_file (str): File name for the user's profile picture (default: 'default.jpg').
    - password (str): Hashed password for user authentication (maximum length: 60 characters).
    - posts (relationship): One-to-many relationship with 'Post' model, representing
      the posts authored by the user.

    Note:
    The 'UserMixin' provides default implementations for common user-related methods
    required by Flask-Login extension.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        """
        Returns a string representation of the User object.

        Returns:
        str: A string containing information about the User instance,
        including username, email, and profile image file.
        """
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """
    Database model representing a post in the application.

    Attributes:
    - id (int): Primary key identifying the post.
    - title (str): Title of the post (maximum length: 100 characters).
    - date_posted (datetime): Date and time when the post was created.
    - content (str): Content of the post.
    - audio_data (str): File name or identifier for associated audio data (nullable).
    - user_id (int): Foreign key referencing the 'id' of the User who authored the post.

    Methods:
    __repr__(): Returns a string representation of the Post object.

    Note:
    The 'user_id' establishes a many-to-one relationship with the 'User' model.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    audio_data = db.Column(db.String(255), nullable=True)  # New field for audio data
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Returns a string representation of the Post object."""
        return f"Post('{self.title}', '{self.date_posted}')"
