import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from audio_journal import app, db, bcrypt
from audio_journal.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from audio_journal.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    """
    Route handler for the home page, displaying a paginated list of posts.

    URL Parameters:
    - page (int, optional): The page number for pagination (default: 1).

    Returns:
    render_template: Renders the 'home.html' template with the paginated list of posts for display on the home page.
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)

@app.route("/audio/<int:post_id>")
def get_audio(post_id):
    """
    Route handler for retrieving and serving audio data associated with a specific post.

    Parameters:
    - post_id (int): The unique identifier of the post for which audio data is requested.

    Returns:
    send_file: Sends the audio data file (in Ogg format) associated with the post as an attachment for download. If no audio data is available, raises a 404 error.
    """
    post = Post.query.get_or_404(post_id)
    if post.audio_data:
        return send_file(BytesIO(post.audio_data), mimetype="audio/ogg", as_attachment=True, download_name=f"audio_{post_id}.ogg")
    else:
        abort(404)


@app.route("/about")
def about():
    """
    Route handler for the about page.

    Returns:
    render_template: Renders the 'about.html' template.
    """
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    """
    Route handler for user registration.

    Methods:
    - GET: Renders the 'register.html' template with the registration form for display.
    - POST: Processes the submitted registration form, validates the input, and creates
      a new user account if the form is valid. Redirects to the login page upon success.

    Returns:
    GET: render_template: Renders the 'register.html' template with the registration form.
    POST: redirect: Redirects to the login page upon successful user registration.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Route handler for user login.

    Methods:
    - GET: Renders the 'login.html' template with the login form for display.
    - POST: Processes the submitted login form, validates the credentials,
      and logs in the user if the credentials are valid. Redirects to the home
      page upon successful login, or to the 'next' page if specified.

    Returns:
    GET: render_template: Renders the 'login.html' template with the login form.
    POST: redirect: Redirects to the home page or the 'next' page upon successful login.
    Displays a flash message on unsuccessful login attempts.
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    """Route handler for user logout."""
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    """
    Save and process a profile picture uploaded through a form.

    Parameters:
    - form_picture (FileStorage): The uploaded file representing the user's profile picture.

    Returns:
    picture_fname: The filename of the saved picture, which can be stored in the database.
    """
    # Generate a random filename for the new picture
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fname = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fname)

    # Resize the image
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)

    img.save(picture_path)

    return picture_fname


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """
    Route handler for the user account page.

    Methods:
    - GET: Renders the 'account.html' template with the user's profile information for display.
    - POST: Processes the submitted form for updating the user's account information.
      If successful, updates the account details and displays a success message.
      Redirects to the 'account' page for display.

    Returns:
    - GET: render_template: Renders the 'account.html' template with the user's profile information.
    - POST: redirect: Redirects to the 'account' page upon successful account update.
      Displays a flash message on unsuccessful update attempts.
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated successfully!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)

# Create New Posts
@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    """
    Route handler for creating a new post.

    Methods:
    - GET: Renders the 'create_post.html' template with the post creation form for display.
    - POST: Processes the submitted form for creating a new post.
      If successful, creates a new post with the provided information, including optional audio data.
      Redirects to the home page upon successful post creation.

    Returns:
    - GET: render_template: Renders the 'create_post.html' template with the post creation form.
    - POST: redirect: Redirects to the home page upon successful post creation.
      Displays a flash message on unsuccessful post creation attempts.
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, audio_data=form.audio_data.data, author=current_user)
        
        if form.audio_data.data:
            audio_filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.mp3" 
            audio_path = os.path.join(app.root_path, 'static/audio', audio_filename)
            form.audio_file.data.save(audio_path)
            post.audio_file = audio_filename
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template("create_post.html", title="New Post", form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    """
    Route handler for displaying an individual post.

    Parameters:
    - post_id (int): The unique identifier of the post to be displayed.

    Returns:
    - render_template: Renders the 'post.html' template with the details of the specified post.
    """
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    """
    Route handler for updating an existing post.

    Parameters:
    - post_id (int): The unique identifier of the post to be updated.

    Methods:
    - GET: Renders the 'create_post.html' template with the post update form for display.
    - POST: Processes the submitted form for updating an existing post.
      If successful, updates the post with the provided information, including optional audio data.
      Redirects to the updated post page upon successful update.

    Returns:
    GET: render_template: Renders the 'create_post.html' template with the post update form.
    POST: redirect: Redirects to the updated post page upon successful update.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.audio_data = form.audio_data.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.audio_data.data = post.audio_data
    return render_template("create_post.html", title="Update Post", form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    """
    Route handler for deleting an existing post.

    Parameters:
    - post_id (int): The unique identifier of the post to be deleted.

    Methods:
    - POST: Processes the deletion request for an existing post.
      If the user is the author of the post, deletes the post from the database.
      Redirects to the home page upon successful deletion.

    Returns:
    redirect: Redirects to the home page upon successful post deletion.
    """
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    """
    Route handler for displaying posts authored by a specific user.

    Parameters:
    - username (str): The username of the user whose posts are to be displayed.

    Query Parameters:
    - page (int, optional): The page number for pagination (default: 1).

    Returns:
    render_template: Renders the 'user_posts.html' template with the posts authored by the specified user.
    """
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template("user_posts.html", posts=posts, user=user)