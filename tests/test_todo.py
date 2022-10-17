import pytest 

from todo_app.app import ViewModel
from todo_app.data.trello_items import Item

def test_view_model_filters_items_by_status():
    #Arrange 
    items = [
        Item(1, 'item1', 'To do'),
        Item(2, 'item2', 'Doing'),
        Item(3, 'item3', 'Done')
    ]
    view_model = ViewModel(items)

    #Act
    todo_items = view_model.todo_items
    doing_items = view_model.doing_items
    done_items = view_model.done_items

    #Assert
    assert len(doing_items) == 1
    assert todo_items[0].title == 'item1'
    assert doing_items[0].title == 'item2'
    assert done_items[0].title == 'item3'