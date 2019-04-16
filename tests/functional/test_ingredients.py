# Test the letters in the recipe parameter

# Test all valid ingredients, expect everything to be ok
def test_all_ingredients(client): 
    api_page = client.get('/api?recipe=WTwSLlNAC')
    assert b'Inedible ingredient in recipe. Try again with valid characters only.' not in api_page.data

# Test a bad ingredient (J) and expect an error.
def test_bad_ingredients(client):
    api_page = client.get('/api?recipe=WTwSLJNAC')
    assert b'Inedible ingredient in recipe. Try again with valid characters only.' in api_page.data

# Ask for a password with a 12-character recipe and expect a 12-character password.
def test_ingredient_length(client):
    api_page = client.get('/api?recipe=CCCCCCCCCCCC')
    assert len((api_page.data).decode("utf-8")) == 12

# Test a password of all numbers and test that it can be converted to an integer.
def test_number_ingredients(client):
    api_page = client.get('/api?recipe=NNNNNNNNNN')
    assert type(int((api_page.data).decode("utf-8"))) is int