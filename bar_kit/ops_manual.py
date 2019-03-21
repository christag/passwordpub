'''
./bar_kit/ops_manual.py
'''

# Import pyyaml to read config.
import yaml

# Read the attached wordlist to compile a list of words.
def read_word_list():
  f = open("bar_kit/todays_specials","r")
  list_of_words = f.read().splitlines()
  return list_of_words

# Read the config file.
def read_config_file():
  with open("config.yml",'r') as yml_file:
    open_file = yml_file.read()
    cfg = yaml.load(open_file,Loader=yaml.SafeLoader)
    return cfg