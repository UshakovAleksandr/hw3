import pytest
import os
import json


@pytest.fixture
def base_url():
    url = "https://api.openbrewerydb.org/breweries/"
    return url


@pytest.fixture
def validation_schema_list():
    with open(os.path.join("schemas", "list_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_filter_by_city():
    with open(os.path.join("schemas", "filter_by_city_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_filter_by_word():
    with open(os.path.join("schemas", "filter_by_word_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_filter_by_id():
    with open(os.path.join("schemas", "filter_by_id_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema
