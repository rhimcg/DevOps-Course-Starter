class ViewModel:
  def __init__(self, items):
    self._items = items

  @property
  def todo_items(self):
    return [item for item in self._items if item.status == 'To do']

  @property 
  def done_items(self):  
    return [item for item in self._items if item.status == 'Done']
  
  @property 
  def doing_items(self):
    return [item for item in self._items if item.status == 'Doing']
