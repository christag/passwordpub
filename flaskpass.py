import random

from flask import Flask,render_template
app = Flask(__name__)

def read_word_list():
  f = open("wordlist","r")
  list_of_words = f.read().splitlines()
  return list_of_words

word_list = read_word_list()

# Temporary variables - this will be replaced by Form items and/or POST data later.
temp_configuration = {
  'number_of_words':3,
  'use_symbols' : True,
  'use_numbers' : True,
  'use_caps' : True,
  'min_char' : 4,
  'max_char' : 24,
  'layout' : 'Wswn'
}

def create_password(configuration):
  password = ''
  for letter in configuration['layout']:
    if letter == 'W':
      password+=(str(random.choice(word_list)).title())
    elif letter == 'w':
      password+=(str(random.choice(word_list)).lower())
    elif letter == 's':
      password+=(random.choice('!@#$%^&*()_'))
    elif letter == 'n':
      password+=(str(random.randint(0,9)))
    else:
      return 'Invalid Configuration'
  if len(password) < configuration['min_char'] or len(password) > configuration['max_char']:
    return 'Password too short or long, please refresh to try again.'
  else:
    return password

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