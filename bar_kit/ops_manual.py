'''
./bar_kit/ops_manual.py
'''

# Import os to check environment variables
import os

# Import pyyaml to read config.
import yaml

# Define bar/server options in class.
class Bar(object):
  def __init__(self,cfg):
    self.max_attempts = os.environ.get("PP_MAX_ATTEMPTS", cfg['max_attempts'])
    self.secret_key = os.environ.get("PP_SECRET_KEY", cfg['secret_key'])
    self.port = os.environ.get("PP_PORT", cfg['port'])
    self.ip_address = os.environ.get("PP_IP_ADDRESS", cfg['ip_address'])
    self.default_options = Defaults(cfg['default_options'])

class Defaults(object):
  def __init__(self,default_options):
    self.min_char = os.environ.get("PP_DEFAULT_MIN_CHAR", default_options['min_char'])
    self.max_char = os.environ.get("PP_DEFAULT_MAX_CHAR", default_options['max_char'])
    self.min_word_char = os.environ.get("PP_DEFAULT_MIN_WORD_CHAR", default_options['min_word_char'])
    self.max_word_char = os.environ.get("PP_DEFAULT_MAX_WORD_CHAR", default_options['max_word_char'])
    self.recipe = os.environ.get("PP_DEFAULT_RECIPE", default_options['recipe'])
    self.banned_ingredients = os.environ.get("PP_DEFAULT_BANNED_INGREDIENTS", default_options['banned_ingredients'])
    self.menu = os.environ.get("PP_DEFAULT_MENU", default_options['menu'])

# Read the config file.
def read_config_file():
  with open("config.yml",'r') as yml_file:
    open_file = yml_file.read()
    cfg = yaml.load(open_file,Loader=yaml.SafeLoader)
    return cfg

def open_bar():
  bar = Bar(read_config_file())
  return bar