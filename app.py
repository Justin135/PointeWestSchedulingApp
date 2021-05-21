# Be sure to use CMD instead of PowerShell.
# Use py -3 -m venv env to create env.
# Use env\Scripts\activate.bat to activate env.

from flask import Flask, render_template, url_for, request, redirect, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os.path
from os import path

# Setup application.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SECRET_KEY"] = "xF6m7FCDKPzfwrKD"

db = SQLAlchemy(app)

if not path.exists("site.db"):
    db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    requested_days_off = db.relationship("RequestedDayOff", backref="author", lazy=True) # This is actually just a query and not a column itself.
    shifts = db.relationship("Shift", backref="auth", lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}'"

class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    start = db.Column(db.String(10), nullable=False)
    end = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return f"Shift('{self.username}',  '{self.day}', '{self.month}', '{self.year}', '{self.start}', '{self.end}'"

class RequestedDayOff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"RequestedDayOff('{self.username}', '{self.day}', '{self.month}', '{self.year}'"

"""
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sunday_open_start = db.Column(db.String(10), nullable=False)
    sunday_open_end = db.Column(db.String(10), nullable=False)
    sunday_close_start = db.Column(db.String(10), nullable=False)
    sunday_close_end = db.Column(db.String(10), nullable=False)
    
    monday_open_start = db.Column(db.String(10), nullable=False)
    monday_open_end = db.Column(db.String(10), nullable=False)
    monday_close_start = db.Column(db.String(10), nullable=False)
    monday_close_end = db.Column(db.String(10), nullable=False)
    
    tuesday_open_start = db.Column(db.String(10), nullable=False)
    tuesday_open_end = db.Column(db.String(10), nullable=False)
    tuesday_close_start = db.Column(db.String(10), nullable=False)
    tuesday_close_end = db.Column(db.String(10), nullable=False)
    
    wednesday_open_start = db.Column(db.String(10), nullable=False)
    wednesday_open_end = db.Column(db.String(10), nullable=False)
    wednesday_close_start = db.Column(db.String(10), nullable=False)
    wednesday_close_end = db.Column(db.String(10), nullable=False)
    
    thursday_open_start = db.Column(db.String(10), nullable=False)
    thursday_open_end = db.Column(db.String(10), nullable=False)
    thursday_close_start = db.Column(db.String(10), nullable=False)
    thursday_close_end = db.Column(db.String(10), nullable=False)
    
    friday_open_start = db.Column(db.String(10), nullable=False)
    friday_open_end = db.Column(db.String(10), nullable=False)
    friday_close_start = db.Column(db.String(10), nullable=False)
    friday_close_end = db.Column(db.String(10), nullable=False)
    
    saturday_open_start = db.Column(db.String(10), nullable=False)
    saturday_open_end = db.Column(db.String(10), nullable=False)
    saturday_close_start = db.Column(db.String(10), nullable=False)
    saturday_close_end = db.Column(db.String(10), nullable=False)
    
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r' % self.id
"""

"""
if not path.exists("template_schedules.db"):
    db.create_all()
"""

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"]) # Required to accept the form data.
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # Valid form submit.
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
        
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"]) # Required to accept the form data.
def login():
    form = LoginForm()
    if form.validate_on_submit(): # Valid form submit.
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")
    
    return render_template("login.html", title="Login", form=form)

"""
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        
        sos = request.form.get("sunday_open_start")
        
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # Returns all data in the database.
        return render_template('index.html', tasks=tasks)
"""

if __name__ == "__main__":
    app.run(debug=True)