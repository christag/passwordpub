#Test the minimum character and maximum character paramters.

# Test a valid number of minimum characters.
def test_min_good(client):
    api_page_min_good = client.get('/api?min_char=9&recipe=CCCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' not in api_page_min_good.data

# Test an invalid number of minimum characters.
def test_min_bad(client):
    api_page_min_bad = client.get('/api?min_char=9&recipe=CCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' in api_page_min_bad.data

# Test a valid number of maximum characters.
def test_max_good(client):
    api_page_max_good = client.get('/api?max_char=12&recipe=CCCCCCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' not in api_page_max_good.data

# Test an invalid number of maximum characters.
def test_max_bad(client):
    api_page_max_bad = client.get('/api?max_char=12&recipe=CCCCCCCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' in api_page_max_bad.data

# Test both a valid number of minimum characters and a valid number of maximum characters.
def test_both_good(client):
    api_page_both_good = client.get('/api?min_char=9&max_char=11&recipe=CCCCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' not in api_page_both_good.data

# Test an invalid number of minimum characters but a valid number of maximum characters.
def test_both_bad_min(client):
    api_page_both_bad_min = client.get('/api?min_char=9&max_char=11&recipe=CCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' in api_page_both_bad_min.data

# Testa valid number of minimum characters but an invalid number of maximum characters.
def test_both_bad_max(client):
    api_page_both_bad_max = client.get('/api?min_char=9&max_char=11&recipe=CCCCCCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' in api_page_both_bad_max.data

# Test both an invalid number of minimum characters and an invalid number of maximum characters.
def test_both_bad_both(client):
    api_page_both_bad_both = client.get('/api?min_char=11&max_char=9&recipe=CCCCCCCCCC')
    assert b'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' in api_page_both_bad_both.data