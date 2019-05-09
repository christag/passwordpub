# Password Pub

This is a cocktail-bar-themed password generator that delivers passwords over HTTP using Python3 and Flask.

## Getting Started

Password Pub can be run with Python3 or with Docker.

### Prerequisites

Python3 is required. Required modules can be found in the [requirements](requirements) file and can be installed by running:

```
python -m pip install -r requirements
```

### Configuration

Server and password generation defaults can be set by environment variables (see [bar_kit/ops_manual.py](bar_kit/ops_manual.py)) or setting the options in [config.yml](config.yml). Environment variables will be given a higher priority than items in [config.yml](config.yml).

### Running in Python

Run the [start_server.py](start_server.py) file

```
python start_server.py
```

Flask will load the page and confirm in the terminal when it is running. Press CTRL-C to quit the application.

### Running as a Container

A [Dockerfile](container/Dockerfile) is included in the [container](container/) folder to build a container for passwordpub.

Build the container from the parent directory.

```
docker image build -t passwordpub:latest -f ./container/app/Dockerfile .
```

Run the docker container. Change the port if you've updated the configuration file.

```
docker container run -d -p 5000:5000 passwordpub:latest
```

Alternatively, you can use docker-compose from the [container](container) directory to quickly bring up a running instance of passwordpub and an nginx proxy server. With this method, the service will be available on port 80 (http). If using passwordpub on a non-default (!=5000), be sure to update the [nginx.conf](bar_kit/nginx/nginx.conf) file.

```
docker-compose up
curl http://127.0.0.1/api
```

## Usage

While running, the application can be accessed in a web browser at http://127.0.0.1:5000, http://localhost:5000, etc. This loads the graphical index.html where a clipart bartender will present a new password on the screen and will generate a new one every time the page is refreshed. The passwords generated here are based on the [config.yml](config.yml) options.

Alternatively, accessing http://127.0.0.1:5000/api will only return a plain-text password. This is better for making REST calls when utilizing the application as part of a larger workflow.

In PowerShell

```
Invoke-WebRequest -uri http://127.0.0.1:5000/api -UseBasicParsing
```

In Bash

```
curl http://127.0.0.1:5000/api
```

You can also specify password configuration items as query parameters:
* min_char: Minimum amount of characters allowed in the password.
* max_char: Minimum amount of characters allowed in the password.
* recipe : The 'recipe' for the password, should be a single string of characters from the following list:
    * 'W' for UPPER CASE word.
    * 'T' for Title Case word.
    * 'w' for lower case word.
    * 'S' for Symbol.
    * 'L' for UPPERCASE letter.  
    * 'l' for lowercase letter.
    * 'N' for random integer between 0 and 9.
    * 'A' for random choice from all UPPER CASE, lower case, and numeric characters.
    * 'C' for random choice from all UPPER CASE, lower case, symbols and numeric characters.
* banned_ingredients : Banned characters that are not allowed in a password.
* menu: The word list (menu) from the [menus](bar_kit/menus) folder. See [bar_kit/menus/README.md](bar_kit/menus/README.md) for descriptions of each menu.

The 'password_options' section in [config.yml](config.yml) file sets the default options for new requests. Any parameter not specified by a parameter will use these defaults.

```
http://127.0.0.1:5000?min_char=4&recipe=TTNNS
```

### Advanced Usage Examples

The following example shows a PowerShell script that can be used to change all user's passwords in Active Directory to a random value and ouput the results.

```
$ADUserList = Get-ADUser -Searchbase "OU=Users,dc=domain,dc=net" - Filter *
Foreach-Object $ADUserList {
    $password = (Invoke-WebRequest -uri http://127.0.0.1:5000/api?recipe=WSTNN -UseBasicParsing).content
    $securepassword = ConvertTo-SecureString $password -AsPlainText -Force
    Set-ADAccountPassword -Identity $_ -Reset -NewPassword $password
    Write-Host $_.UserPrincipalName ' password set to: '$password
}
```

## Built With

* [Flask](http://flask.pocoo.org/) - Web development microframework for Python
* [Python3](https://www.python.org/download/releases/3.0/) - The language that this app is written in.

<!---

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 
--->

## Authors

* **Christopher Tagliaferro** - *Initial work* - [christag](https://github.com/christag)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thanks to [PurpleBooth](https://gist.github.com/PurpleBooth) for this great [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* Inspired by [bbusschots](https://github.com/bbusschots)'s [xpasswd.net](https://xkpasswd.net)/[hsxkpasswd](https://github.com/bbusschots/hsxkpasswd)
