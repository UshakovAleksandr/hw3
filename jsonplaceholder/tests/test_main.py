import requests
import pytest
from jsonschema import validate


def test_url_all(base_url, validation_schema_all):
    resp = requests.get(base_url)
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=validation_schema_all)


@pytest.mark.parametrize("url_end", [1, 2, 3, 4, 5, 6, 7])
def test_url_by_id(base_url, validation_schema_by_id, url_end):
    resp = requests.get(base_url + str(url_end))
    assert resp.status_code == 200
    assert resp.json().get("id") == url_end
    assert resp.json().get("userId") == 1
    validate(instance=resp.json(), schema=validation_schema_by_id)


def test_post_url_by_id(post_url_by_id, validation_schema_by_id):
    resp = requests.post(url=post_url_by_id[0], json=post_url_by_id[1], headers=post_url_by_id[2])
    assert resp.status_code == 201
    assert resp.json().get("userId") == post_url_by_id[1]["userId"]
    validate(instance=resp.json(), schema=validation_schema_by_id)


def test_put_url_by_id(put_url_by_id, validation_schema_by_id):
    resp = requests.put(url=put_url_by_id[0] + "1", json=put_url_by_id[1], headers=put_url_by_id[2])
    assert resp.status_code == 200
    assert resp.json().get("userId") == put_url_by_id[1]["userId"]
    validate(instance=resp.json(), schema=validation_schema_by_id)


@pytest.mark.parametrize("url_end", [1, 2, 3, 4, 5, 6, 7])
def test_user_by_id(base_url, url_end):
    resp = requests.delete(base_url + str(url_end))
    assert resp.status_code == 200
    assert resp.json() == {}
