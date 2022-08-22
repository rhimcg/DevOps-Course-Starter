import requests, os

trello_base = "http://trello.com/1/"
board_id = os.environ.get("TRELLO_BOARD_ID")
trello_keys = ('&key=%s&token=%s' % (os.environ.get('TRELLO_KEY'), os.environ.get('TRELLO_TOKEN')))



def get_items():
    args = ("boards/%s/lists?cards=open" % board_id)
    lists =  requests.get(trello_base + args + trello_keys)
    lists = lists.json()
    cards = []
    for list in lists:
        for card in list['cards']:
            cards.append(Item.from_trello_card(Item, card, list))
    return cards

class Item:
  def __init__(self, id, title, status='To do'):
    self.id = id
    self.title = title
    self.status = status

  def from_trello_card(cls, card, list):
    return cls(card['id'], card['name'], list['name'])