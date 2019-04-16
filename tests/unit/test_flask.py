# Test if Flask loads and the api page returns an OK status
def test_flask(client):
    api_page = client.get('/api')
    assert api_page.status_code == 200