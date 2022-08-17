import requests, os

trello_base = "trello.com/1/"
board_id = os.environ("TRELLO_BOARD_ID")


def get_items():
    return requests.get(trello_base + "/boards/{board_id}}/lists?cards=open")
