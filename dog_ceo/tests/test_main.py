import requests
import pytest
from jsonschema import validate


def test_url_all(base_url, validation_schema_all):
    resp = requests.get(base_url + "breeds/list/all")
    assert resp.status_code == 200
    assert resp.json().get("status") == "success"
    validate(instance=resp.json(), schema=validation_schema_all)


def test_url_random(base_url, validation_schema_random):
    resp = requests.get(base_url + "breeds/image/random")
    assert resp.status_code == 200
    assert resp.json().get("status") == "success"
    validate(instance=resp.json(), schema=validation_schema_random)


def test_url_list(base_url, validation_schema_list):
    resp = requests.get(base_url + "breed/hound/list")
    assert resp.status_code == 200
    assert resp.json().get("status") == "success"
    validate(instance=resp.json(), schema=validation_schema_list)


@pytest.mark.parametrize("url_end", [10, 22, 53, 44, 3, 55, 29])
def test_url_random_count(base_url, validation_schema_random_count, url_end):
    resp = requests.get(base_url + "breed/hound/images/random/" + str(url_end))
    assert resp.status_code == 200
    assert resp.json().get("status") == "success"
    validate(instance=resp.json(), schema=validation_schema_random_count)


@pytest.mark.parametrize("url_end", [2, 4, 5, 1, 12, 15, 21, 24])
def test_url_random_afghan(base_url, url_end, validation_schema_afghan):
    resp = requests.get(base_url + "breed/hound/afghan/images/random/" + str(url_end))
    assert resp.status_code == 200
    assert resp.json().get("status") == "success"
    validate(instance=resp.json(), schema=validation_schema_afghan)
