import pytest
import os
import json


@pytest.fixture
def base_url():
    URL = "https://jsonplaceholder.typicode.com/posts/"
    return URL


@pytest.fixture
def validation_schema_all():
    with open(os.path.join("schemas", "all_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_by_id():
    with open(os.path.join("schemas", "by_id_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def post_url_by_id(base_url):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }

    data = {
        "title": "test",
        "body": "test",
        "userId": 1
    }
    return base_url, data, headers


@pytest.fixture
def put_url_by_id(base_url):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }

    data = {
        "id": 1,
        "title": "test",
        "body": "test",
        "userId": 2
    }
    return base_url, data, headers
