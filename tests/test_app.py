import pytest, os, requests
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    #Arrange
    monkeypatch.setattr(requests, 'get', get_items_stub)
    
    #Act
    response = client.get('/')

    #Assert
    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
    assert 'In progress' not in response.data.decode()
    assert 'Complete card' in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data
    
    def json(self):
        return self.fake_response_data

def get_items_stub(url, params):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    if url == f'https://trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [
            {
                'id': '123',
                'name': 'To do',
                'cards': [{'id': '456', 'name': 'Test card'}]
            },
            {
                'id': '789',
                'name': 'Doing',
                'cards': [
                    {
                        'id': '101', 
                        'name': 'In progress'
                    },
                    {
                        'id': '112',
                        'name': 'In progress'
                    }
                ]
            },
             {
                'id': '213',
                'name': 'Done',
                'cards': [
                    {
                        'id': '141', 
                        'name': 'Complete card'
                    }
                ]
            },

        ]
    return StubResponse(fake_response_data)

