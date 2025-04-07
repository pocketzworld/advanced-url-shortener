from app.shortener import shorten_url

def test_shorten_url():
    assert len(shorten_url("http://example.com")) == 6
