from flask import Flask, redirect, render_template, request
from todo_app.data.trello_items import get_items, add_item_to_list, complete_item
from todo_app.flask_config import Config
from .view_model import ViewModel
import os

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config())

  trello_base = "https://trello.com/1/"
  board_id = os.environ.get("TRELLO_BOARD_ID")
  trello_todo_list_id = os.environ.get('TRELLO_TODO_LIST_ID')
  trello_done_list_id = os.environ.get('TRELLO_DONE_LIST_ID')
  trello_keys = {
    'key': os.environ.get('TRELLO_KEY'),
    'token': os.environ.get('TRELLO_TOKEN')
  }

  @app.route('/')
  def get_todos():
      items = get_items(board_id, trello_base, trello_keys)
      item_view_model = ViewModel(items)
      return render_template('index.html', view_model = item_view_model)

  @app.route('/add-todo', methods=['POST'])
  def add_todo():
      newTodo = request.form.get('new-todo')
      add_item_to_list(newTodo, trello_base, trello_keys, trello_todo_list_id)
      return redirect('/')

  @app.route('/complete-todo/<id>')
  def complete_todo(id):
      complete_item(id, trello_base, trello_keys, trello_done_list_id)    
      return redirect('/')
  return app
