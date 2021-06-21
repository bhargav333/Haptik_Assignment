import requests
from q1_most_active_users import ActiveUsers
import pytest

@pytest.fixture
def example_url():
	return "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt"

@pytest.fixture
def example_url_wrong_filetype():
	return "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.png"

def test_get_active_users(example_url):
	test =  ActiveUsers(example_url)
	assert test.get_top_users() == 'Top 3 Active Users are : John, Ram and Adam'