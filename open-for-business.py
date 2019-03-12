# Import python modules for randomly generating things and reading things.
import random, string, yaml

# Import Flask and Flask modules.
from flask import Flask,render_template

# Create an instance of the Flask app.
app = Flask(__name__)

# Read the attached wordlist to compile a list of words.
def read_WORD_LIST():
  f = open("wordlist","r")
  list_of_words = f.read().splitlines()
  return list_of_words

# Read the config file.
def read_config_file():
  with open("config.yml",'r') as yml_file:
    cfg = yaml.load(yml_file)
    return cfg

WORD_LIST = read_WORD_LIST() # Create the word list
APP_CONFIGURATION = read_config_file() # Set the configuration options
SERVER_OPTIONS = APP_CONFIGURATION['server_options']

# Generates a word, letter, number, symbol, etc. to be used as part of the password.
def generate_member(config_item):
  if config_item == 'W': # W for UPPER CASE word.
    return str(random.choice(WORD_LIST)).upper() # Take a random word from the attached word list, and make it UPPERCASE.
  if config_item == 'T': # T for Title Case word.
    return str(random.choice(WORD_LIST)).title() # Take a random word from the attached word list, and make it Title Case.
  if config_item == 'w': # w for lower case word.
    return str(random.choice(WORD_LIST)).lower() # Take a random word from the attached word list, and make it lower case.
  if config_item == 'S': # S for Symbol.
    return random.choice('!@#$%^&*()_') # Take a random character from the string of symbols provided.
  if config_item == 'L': # L for UPPERCASE letter.  
    return random.choice(string.ascii_uppercase) # Take a random choice from any UPPER CASE ascii character.
  if config_item == 'l': # l for lowercase letter.
    return random.choice(string.ascii_lowercase) # Take a random choice from any lower case ascii character.
  if config_item == 'N': # n for Number
    return (str(random.randint(0,9))) # Generate a random integer between 0 and 9.
  if config_item =='A': # A for any alphanumeric character.
    return random.choice(string.ascii_letters + '0123456789') # Combines all UPPER CASE, lower case, and numeric characters in one string and grabs a random choice. 
  if config_item == 'C': # C for any character.
    return random.choice(string.ascii_letters + '0123456789!@#$%^&*()_') # Combines all UPPER CASE, lower case, symbols and numeric characters in one string and grabs a random choice.

# Check if any characters in the password are in the banned_chars list.
def validate_password(password,banned_chars):
  for character in password:
    if character in banned_chars:
      return False
  return True

# Main function that creates the password.
def create_password(pw_options,gen_options):
  try_count = 0
  while try_count < gen_options['max_attempts']: # Only attempts to create the password 'max_attempts' times so as not to get caught in a never-ending loop of a bad password recipe.
    password = '' # Initialize the password.
    for letter in pw_options['layout']: # Look through the layout key of the configuration to build the ingredients list for the password.
      password += generate_member(letter) # Add ingredient to password.
    if (len(password) < pw_options['min_char']) or (len(password) > pw_options['max_char']) or (validate_password(password,pw_options['banned_chars']) == False): # Check if password is beyond length limits.
      try_count += 1 # Increment try_count closer to max_attempts and restart the loop, starting a new password.
    else: # Password meets all requirements.
      return password
  return 'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' # After max_attempts has been reached, generates this error.

@app.route("/") # Endpoint for HTML in Browser
def display_password():
    pw_options = APP_CONFIGURATION['password_options'] # Set the active password configuration items.
    gen_options = APP_CONFIGURATION['generator_options'] # Set the options for the generator.
    password = create_password(pw_options,gen_options) # Create password using the configuration.
    return render_template('index.html', password=password) # Returns a rendered version of index.html with the password displayed.

@app.route('/api') # Endpoint for API calls.
def generate_password():
    pw_options = APP_CONFIGURATION['password_options'] # Set the active password configuration items.
    gen_options = APP_CONFIGURATION['generator_options'] # Set the options for the generator.
    password = create_password(pw_options,gen_options) # Create password using the configuration.
    return password # Returns a plaintext password.

# If the python file is run by itself, run the app with these flask settings.
if __name__ == "__main__":
    app.run(host = SERVER_OPTIONS['ip_address'], port = SERVER_OPTIONS['port'])