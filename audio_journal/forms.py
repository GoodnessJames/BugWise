from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from audio_journal.models import User

class RegistrationForm(FlaskForm):
    """
    A FlaskForm representing the registration form for user sign-up.

    Attributes:
    - username (StringField): Field for entering the desired username.
    - email (StringField): Field for entering the email address.
    - password (PasswordField): Field for entering the password.
    - confirm_password (PasswordField): Field for confirming the password.
    - submit (SubmitField): Button to submit the registration form.
      Label: 'Sign Up'
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """
        Validates the uniqueness of the provided username in the registration form.

        Parameters:
        - username (StringField): The username entered by the user.

        Raises:
        - ValidationError: If the provided username is already in use by an existing user,
        raises an error.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please choose a different one')
        
    def validate_email(self, email):
        """
        Validates the uniqueness of the provided email address in the registration form.

        Parameters:
        - email (StringField): The email entered by the user.

        Raises:
        - ValidationError: If the provided email is already in use by an existing user,
        raises an error.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please choose a different one')


class LoginForm(FlaskForm):
    """
    A FlaskForm representing the login form for user authentication.

    Attributes:
    - email (StringField): Field for entering the user's email address.
    - password (PasswordField): Field for entering the user's password.
    - remember (BooleanField): Checkbox for the user to indicate whether to remember the login session.
    - submit (SubmitField): Button to submit the login form.
      Label: 'Login'
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """
    A FlaskForm representing the form for updating user account information.

    Attributes:
    - username (StringField): Field for updating the username.
    - email (StringField): Field for updating the email address.
    - picture (FileField): Field for updating the user's profile picture.
    - submit (SubmitField): Button to submit the account update form.
      Label: 'Update'
    """
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        """
        Validates the uniqueness of the provided username during account update.

        Parameters:
        - username (StringField): The updated username entered by the user.

        Raises:
        - ValidationError: If the provided username is already in use by another user and
        it is different from the current user's username, raises an error.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken. Please choose a different one.')
        
    def validate_email(self, email):
        """
        Validates the uniqueness of the provided email during account update.

        Parameters:
        - email (StringField): The updated email entered by the user.

        Raises:
        - ValidationError: If the provided email is already in use by another user and
        it is different from the current user's email, raises an error.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken. Please choose a different one.')

# Create New Posts
class PostForm(FlaskForm):
    """
    A FlaskForm representing the form for creating or editing a post.

    Attributes:
    - title (StringField): Field for entering the post's title.
    - content (TextAreaField): Field for entering the post's content.
    - audio_data (FileField): Field for uploading an audio file related to the post.
    - submit (SubmitField): Button to submit the post form.
      Label: 'Post'
    """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    audio_data = FileField('Record Audio')
    submit = SubmitField('Post')
