import requests
import pytest
from fastapi.encoders import jsonable_encoder

from data.test_data import test_posts, test_accts

base_url = "http://localhost:8000/pairs"


@pytest.fixture
def api_url():
    return base_url


def test_get_request(api_url):

    # Define the data to be passed in the query parameters
    payload = {
        "posts": jsonable_encoder(test_posts),
        "accounts": jsonable_encoder(test_accts),
        "hashtag": "#diedsuddenly",
        "min_similarity": 0.8,
    }

    # Specify the Content-Type header as application/json
    headers = {"Content-Type": "application/json"}

    # Perform the GET request with the specified parameters
    response = requests.get(api_url, json=payload, headers=headers)

    # Check the status code
    if response.status_code == 200:
        # Successful response
        data = response.json()
    else:
        # Handle the error
        print(f"Error: {response.status_code}, {response.text}")

    # Check the status code
    assert response.status_code == 200

    # Check number of similar account pairs
    assert len(data['similar_account_pairs']) == 6
