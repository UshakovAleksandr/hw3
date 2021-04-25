import requests
import pytest
from jsonschema import validate


def test_url_list(base_url, validation_schema_list):
    resp = requests.get(base_url)
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=validation_schema_list)


@pytest.mark.parametrize("url_end", ["Bellingham", "Mesa", "Gilbert",
                                     "Williamsville", "John Day"])
def test_url_filter_by_city(base_url, url_end, validation_schema_filter_by_city):
    resp = requests.get(base_url + "?by_city=" + str(url_end))
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=validation_schema_filter_by_city)


@pytest.mark.parametrize("url_end", ["dog", "cat", "door", 10, 15])
def test_url_filter_word(base_url, url_end, validation_schema_filter_by_word):
    resp = requests.get(base_url + "autocomplete?query=" + str(url_end))
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=validation_schema_filter_by_word)


@pytest.mark.parametrize("url_end", [15230, 15231, 15232, 15233, 15234])
def test_url_filter_by_id(base_url, validation_schema_filter_by_id, url_end):
    resp = requests.get(base_url + str(url_end))
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=validation_schema_filter_by_id)
