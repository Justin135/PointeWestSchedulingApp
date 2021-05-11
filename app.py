# Use py -3 -m venv env to create env.
# Use env\Scripts\activate.bat to activate env.

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os.path
from os import path

# Setup application.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///template_schedules.db'
db = SQLAlchemy(app)

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

if not path.exists("template_schedules.db"):
    db.create_all()

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        
        sos = request.form.get("sunday_open_start")
        
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # Returns all data in the database.
        return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)