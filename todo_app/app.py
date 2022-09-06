from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import get_items, add_item, complete_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

class ViewModel:
  def __init__(self, todo_items, done_items):
    self._todo_items = todo_items
    self._done_items = done_items

  @property
  def todo_items(self):
      return self._todo_items

  @property 
  def done_items(self):  
    return self._done_items


@app.route('/')
def get_todos():
    [todo_items, done_items] = get_items()
    item_view_model = ViewModel(todo_items, done_items)
    return render_template('index.html', view_model = item_view_model)

@app.route('/add-todo', methods=['POST'])
def add_todo():
    newTodo = request.form.get('new-todo')
    add_item(newTodo)
    return redirect('/')

@app.route('/complete-todo/<id>')
def complete_todo(id):
    complete_item(id)    
    return redirect('/')
