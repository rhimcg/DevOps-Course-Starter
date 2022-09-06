import requests, os, urllib.parse

trello_base = "https://trello.com/1/"
board_id = os.environ.get("TRELLO_BOARD_ID")
trello_todo_list_id = os.environ.get('TRELLO_TODO_LIST_ID')
trello_done_list_id = os.environ.get('TRELLO_DONE_LIST_ID')
trello_keys = {
  'key': os.environ.get('TRELLO_KEY'),
  'token': os.environ.get('TRELLO_TOKEN')
}

class Item:
  def __init__(self, id, title, status='To do'):
    self.id = id
    self.title = title
    self.status = status

  def from_trello_card(cls, card, list):
    return cls(card['id'], card['name'], list['name'])

def get_items():
  args = ("boards/%s/lists" % board_id)
  url = trello_base + args
  params = {
    **trello_keys,
    'cards': 'open'
  }
  lists =  requests.get(url, params = params)
  lists = lists.json()
  todo_cards = []
  done_cards = []
  for list in lists:
      for card in list['cards']:
        if card['idList'] == trello_todo_list_id:
          todo_cards.append(Item.from_trello_card(Item, card, list))
        elif card['idList'] == trello_done_list_id:
          done_cards.append(Item.from_trello_card(Item, card, list))
  return todo_cards, done_cards

def add_item(title):
  args = ('cards')
  url = trello_base + args
  params = {
    **trello_keys,
    'name': title,
    'idList': trello_todo_list_id
  }

  requests.post(url, params = params) 

def complete_item(item_id):
  args = ('cards/%s' % item_id)
  url = trello_base + args
  params = {
    **trello_keys,
    'idList': trello_done_list_id
  }
  requests.put(url, params = params)

