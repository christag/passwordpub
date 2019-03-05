import random

# Import Flask and Flask modules
from flask import Flask,render_template

# Create an instance of the Flask app
app = Flask(__name__)

# Read the attached wordlist to compile a list of words.
def read_word_list():
  f = open("wordlist","r")
  list_of_words = f.read().splitlines()
  return list_of_words

word_list = read_word_list()

# Set maximum attempts to retry generation if character or length is incorrect.
max_attempts = 150

# Temporary variables - this will be replaced by Form items and/or POST data later.
temp_configuration = {
  'min_char' : 4,
  'max_char' : 26,
  'layout' : 'Wswn',
  'banned_chars' : 'f'
}

def generate_character(config_item):
  if config_item == 'W':
    return str(random.choice(word_list)).title()
  if config_item == 'w':
    return str(random.choice(word_list)).lower()
  if config_item == 's':
    return random.choice('!@#$%^&*()_')
  if config_item == 'n':
    return (str(random.randint(0,9)))

def validate_password(password,banned_chars):
  for character in password:
    if character in banned_chars:
      print('found banned character')
      return False
  return True

def create_password(configuration):
  try_count = 0
  while try_count < max_attempts:
    password = ''
    for letter in configuration['layout']:
      password += generate_character(letter)
    if (len(password) < configuration['min_char']) or (len(password) > configuration['max_char']) or (validate_password(password,configuration['banned_chars']) == False):
      print('check failed. retrying...')
      try_count += 1
    else:
      return password
  return 'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.'

@app.route("/")
def display_password():
    password = create_password(temp_configuration)
    return render_template('index.html', password=password)

@app.route('/api')
def generate_password():
    password = create_password(temp_configuration)
    return password

if __name__ == "__main__":
    app.run(host='0.0.0.0')