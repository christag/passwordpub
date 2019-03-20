'''
./bar_kit/shaker.py
'''

import random, string

from bar_kit.ops_manual import read_word_list

WORD_LIST = read_word_list() # Create the word list

# Generates a word, letter, number, symbol, etc. to be used as part of the password.
def add_ingredient(config_item):
  if config_item == 'W': # W for UPPER CASE word.
    return str(random.choice(WORD_LIST)).upper() # Take a random word from the attached word list, and make it UPPERCASE.
  elif config_item == 'T': # T for Title Case word.
    return str(random.choice(WORD_LIST)).title() # Take a random word from the attached word list, and make it Title Case.
  elif config_item == 'w': # w for lower case word.
    return str(random.choice(WORD_LIST)).lower() # Take a random word from the attached word list, and make it lower case.
  elif config_item == 'S': # S for Symbol.
    return random.choice('!@#$%^&*()_') # Take a random character from the string of symbols provided.
  elif config_item == 'L': # L for UPPERCASE letter.  
    return random.choice(string.ascii_uppercase) # Take a random choice from any UPPER CASE ascii character.
  elif config_item == 'l': # l for lowercase letter.
    return random.choice(string.ascii_lowercase) # Take a random choice from any lower case ascii character.
  elif config_item == 'N': # n for Number
    return (str(random.randint(0,9))) # Generate a random integer between 0 and 9.
  elif config_item =='A': # A for any alphanumeric character.
    return random.choice(string.ascii_letters + '0123456789') # Combines all UPPER CASE, lower case, and numeric characters in one string and grabs a random choice. 
  elif config_item == 'C': # C for any character.
    return random.choice(string.ascii_letters + '0123456789!@#$%^&*()_') # Combines all UPPER CASE, lower case, symbols and numeric characters in one string and grabs a random choice.
  else:
    return False

# Check if any characters in the password are in the banned_chars list.
def taste_test(drink,banned_ingredients):
  for ingredient in drink:
    if ingredient in banned_ingredients:
      return False
  return True

# Main function that creates the password.
def mix_drink(pw_options,GEN_OPTIONS):
  try_count = 0
  while try_count < GEN_OPTIONS['max_attempts']: # Only attempts to create the password 'max_attempts' times so as not to get caught in a never-ending loop of a bad password recipe.
    password = '' # Initialize the password.
    for ingredients in pw_options['recipe']: # Look through the layout key of the configuration to build the ingredients list for the password.
      new_ingredient = add_ingredient(ingredients) # Pick out a new ingredient
      if new_ingredient != False:
        password += add_ingredient(ingredients) # Add ingredient to password.
      else:
        return 'Inedible ingredient in recipe. Try again with valid characters only.'
    if (len(password) < int(pw_options['min_char'])) or (len(password) > int(pw_options['max_char'])) or (taste_test(password,pw_options['banned_ingredients']) == False): # Check if password is beyond length limits.
      try_count += 1 # Increment try_count closer to max_attempts and restart the loop, starting a new password.
    else: # Password meets all requirements.
      return password
  return 'Maximum attempts to generate a password have been reached. Try less restrictions in length or banned characters.' # After max_attempts has been reached, generates this error.