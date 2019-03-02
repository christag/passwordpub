import random

from flask import Flask,render_template
app = Flask(__name__)

def read_word_list():
  f = open("wordlist","r")
  list_of_words = f.read().splitlines()
  return list_of_words

word_list = read_word_list()

def create_password():
  words = []
  for i in range(4):
    words.append(str(random.choice(word_list)).title())
  digits = str(random.randint(0,9999)).zfill(4)
  symbol = random.choice('!@#$%^&*()_')
  password= str(''.join(words) + digits + symbol)
  return password

@app.route("/")
def display_password():
    password = create_password()
    return render_template('index.html', password=password)

@app.route('/api')
def generate_password():
    password = create_password()
    return password

if __name__ == "__main__":
    app.run()