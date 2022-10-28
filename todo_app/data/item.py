class Item:
  def __init__(self, id, title, status='To do'):
    self.id = id
    self.title = title
    self.status = status

  def from_trello_card(cls, card, list):
    return cls(card['id'], card['name'], list['name'])