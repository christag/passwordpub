import random

from flask import Flask
app = Flask(__name__)

def read_word_list():
  f = open("wordlist","r")
  list_of_words = f.read().splitlines()
  return list_of_words

word_list = read_word_list()

def create_password():
  word_1 = str(random.choice(word_list)).title()
  word_2 = str(random.choice(word_list)).title()
  digits = str(random.randint(0,9999)).zfill(4)
  symbol = random.choice('!@#$%^&*()_')
  password= str(word_1 + word_2 + digits + symbol)
  return password

@app.route('/')
def generate_password():
    password = create_password()
    return password

if __name__ == "__main__":
    app.run()