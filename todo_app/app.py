from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/')
def get_todos():
    items = get_items()
    print(items)
    return render_template('index.html', items = items)

@app.route('/add-todo', methods=['POST'])
def add_todo():
    print('Hello')
    newTodo = request.form.get('new-todo')
    print(newTodo)
    add_item(newTodo)
    return redirect('/todos')
