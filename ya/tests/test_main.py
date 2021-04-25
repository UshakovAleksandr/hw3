import requests


def test_ya(base_url, status_code):
    resp = requests.get(base_url)
    assert resp.status_code == int(status_code)
