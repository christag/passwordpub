'''
./start_server.py
'''

# Import Flask
from flask import Flask,render_template,request

# Import other parts of PasswordPub
from bar_kit.shaker import mix_drink
from bar_kit.ops_manual import open_bar

# Define class object for a password order, expects Bar class object as an input.
class Drink_order(object):
  def __init__(self, config):
    self.min_char = config.min_char
    self.max_char = config.max_char
    self.min_word_char = config.min_word_char
    self.max_word_char = config.max_word_char
    self.recipe = config.recipe
    self.banned_ingredients = config.banned_ingredients
    self.menu = config.menu

# Create a password using the supplied parameters
def fulfill_order(order,bar):
  drink_order = Drink_order(bar.default_options) # Create a new Drink_order object for this order, set it initially to the bar's default options.
  for parameter in order: # Checks paremeters in query.
    if hasattr(drink_order,parameter) == True: # Is parameter an actual parameter?
      setattr(drink_order, parameter, order.get(parameter)) # If so, update the Drink_order object with new options.
    else:
      return 'Error: Bad parameter in request!' # If there's a bad parameter, fail.
  cocktail = mix_drink(drink_order,bar) # Create password using the configuration.
  return cocktail

# Create an instance of the Flask app.
def create_app(bar):
  app = Flask(__name__)

  @app.route("/") # Endpoint for HTML in Browser
  def display_password():
    #pylint: disable=unused-variable
    cocktail = fulfill_order(request.args,bar) # Create a password using the parameters in the URL plus the bar's default options.
    return render_template('index.html', password=cocktail) # Returns a rendered version of index.html with the password displayed.
  
  @app.route('/api') # Endpoint for API calls.
  def generate_password():
    #pylint: disable=unused-variable
    cocktail = fulfill_order(request.args,bar) # Create a password using the parameters in the URL plus the bar's default options.
    return cocktail # Returns a plaintext password.

  return app

# If the python file is run by itself, run the app with these flask settings.
if __name__ == "__main__":
  bar = open_bar()
  app = create_app(bar)
  app.run(host = bar.ip_address, port = bar.port)