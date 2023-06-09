import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    done = db.Column(db.Boolean)

@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_templates('base.html', todo_list=todo_list)

def add():
    name = request.form.get("name")
    new_task = Todo(name=name, done=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:todo_id>')
def update (todo_id):
    todo = Todo.query.get(Todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/delete/<int:todo_id>')
def delete (todo_id):
    todo = Todo.query.get(Todo_id)
    todo.session.delete(tod)
    db.session.commit()
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug = True)





















