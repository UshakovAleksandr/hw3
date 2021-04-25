import pytest
import os
import json


@pytest.fixture
def base_url():
    base_url = "https://dog.ceo/api/"
    return base_url


@pytest.fixture
def validation_schema_all():
    with open(os.path.join("schemas", "all_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_random():
    with open(os.path.join("schemas", "random_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_random_count():
    with open(os.path.join("schemas", "random_count_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_list():
    with open(os.path.join("schemas", "list_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema


@pytest.fixture
def validation_schema_afghan():
    with open(os.path.join("schemas", "afghan_schema.json"), "r") as file:
        schema = json.loads(file.read())
    return schema
