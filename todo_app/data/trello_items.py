import requests

class Item:
  def __init__(self, id, title, status='To do'):
    self.id = id
    self.title = title
    self.status = status

  def from_trello_card(cls, card, list):
    return cls(card['id'], card['name'], list['name'])

def get_items(board_id, trello_base, trello_keys):
  args = ("boards/%s/lists" % board_id)
  url = trello_base + args
  params = {
    **trello_keys,
    'cards': 'open'
  }
  lists = requests.get(url, params = params)
  lists = lists.json()
  cards = []
  for list in lists:
      for card in list['cards']:
        cards.append(Item.from_trello_card(Item, card, list))
  return cards

def add_item_to_list(title, trello_base, trello_keys, trello_list_id):
  args = ('cards')
  url = trello_base + args
  params = {
    **trello_keys,
    'name': title,
    'idList': trello_list_id
  }

  requests.post(url, params = params) 

def complete_item(item_id, trello_base, trello_keys, trello_done_list_id):
  args = ('cards/%s' % item_id)
  url = trello_base + args
  params = {
    **trello_keys,
    'idList': trello_done_list_id
  }
  requests.put(url, params = params)

