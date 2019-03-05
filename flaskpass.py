import random, string

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
default_configuration = {
  'min_char' : 8,
  'max_char' : 50,
  'layout' : 'WsTwNlLs',
  'banned_chars' : ''
}

# Generates a word, letter, number, symbol, etc. to be used as part of the password.
def generate_member(config_item):
  if config_item == 'W': # W for UPPERCASE word.
    return str(random.choice(word_list)).upper()
  if config_item == 'T': # T for TitleCase word.
    return str(random.choice(word_list)).title()
  if config_item == 'w': # w for lowercase word.
    return str(random.choice(word_list)).lower()
  if config_item == 's': # S for Symbol
    return random.choice('!@#$%^&*()_')
  if config_item == 'L': # L for UPPERCASE letter.
    return random.choice(string.ascii_uppercase)
  if config_item == 'l': # l for lowercase letter.
    return random.choice(string.ascii_lowercase)
  if config_item == 'N': # n for Number
    return (str(random.randint(0,9)))

# Check if any characters in the password are in the banned_chars list.
def validate_password(password,banned_chars):
  for character in password:
    if character in banned_chars:
      return False
  return True

# Main function that creates the password.
def create_password(configuration):
  try_count = 0
  while try_count < max_attempts: # Only attempts to create the password 'max_attempts' times so as not to get caught in a never-ending loop of a bad password recipe.
    password = '' # Initialize the password.
    for letter in configuration['layout']: # Look through the layout key of the configuration to build the ingredients list for the password.
      password += generate_member(letter) # 
    if (len(password) < configuration['min_char']) or (len(password) > configuration['max_char']) or (validate_password(password,configuration['banned_chars']) == False):
      try_count += 1
    else:
      return password
  return 'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.'

@app.route("/")
def display_password():
    configuration = default_configuration
    password = create_password(configuration)
    return render_template('index.html', password=password)

@app.route('/api')
def generate_password():
    configuration = default_configuration
    password = create_password(configuration)
    return password

if __name__ == "__main__":
    app.run(host='0.0.0.0')