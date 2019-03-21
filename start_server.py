'''
./start_server.py
'''

# Import Flask
from flask import Flask,render_template,request
import os 

# Import other parts of PasswordPub
from bar_kit.shaker import mix_drink
from bar_kit import ops_manual

# 
def fulfill_order(order):
  pw_options = dict(APP_CONFIGURATION['password_options']) # Set the password options to the defaults.
  for parameter in order: # Checks paremeters in query.
    if parameter in pw_options: # If parameter matches a password option...
      pw_options[parameter] = order.get(parameter) # ...set the value of the parameter to that option.
    else:
      return 'Error: Bad parameter in request!' # If there's a bad parameter, fail.
  cocktail = mix_drink(pw_options,GEN_OPTIONS) # Create password using the configuration.
  return cocktail

# Create an instance of the Flask app.
def create_app():
  app = Flask(__name__)

  @app.route("/") # Endpoint for HTML in Browser
  def display_password():
    cocktail = fulfill_order(request.args)
    return render_template('index.html', password=cocktail) # Returns a rendered version of index.html with the password displayed.
  
  @app.route('/api') # Endpoint for API calls.
  def generate_password():
    cocktail = fulfill_order(request.args)
    return cocktail # Returns a plaintext password.

  return app

# Variable setup
APP_CONFIGURATION = ops_manual.read_config_file() # Set the configuration options.
SERVER_OPTIONS = APP_CONFIGURATION['server_options'] # Set server options from config.
GEN_OPTIONS = APP_CONFIGURATION['generator_options'] # Set generator options from config.

# If the python file is run by itself, run the app with these flask settings.
if __name__ == "__main__":
  app = create_app()
  port = os.environ.get("PP_PORT", SERVER_OPTIONS['port'])
  app.run(host = SERVER_OPTIONS['ip_address'], port = port)

