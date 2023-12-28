from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.bug_entry_routes import bug_entry_bp

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugwise.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Register blueprint
app.register_blueprint(bug_entry_bp)

# Create database tables when the app is run
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
