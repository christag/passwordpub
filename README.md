# Flaskpass

This is a simple password generator that delivers passwords over HTTP using Python3 and Flask. 

## Getting Started

Flaskpass can be run with Python3 or with Docker.

### Prerequisites

Python3 is required. Flask is a required Python module that can be installed using pip.

```
python -m pip install flask
```

### Running in Python

Simply run the python file and the default Flask settings will be used to run the app on port 5000.

Run the flaskpass.py file

```
python flaskpass.py
```

Flask will load the page and confirm in the terminal when it is running. Press CTRL-C to quit the application.

### Running in Docker

A Dockerfile is included to build a container for flaskpass.

Build the container

```
docker build -t flaskpass:latest .
```

Run the docker container

```
docker run -d -p 5000:5000 flaskpass:latest
```

Alternatively, you can use docker-compose to quickly bring up a running instance of flaskpass.

```
docker-compose up
```

### Please Note

Note that HTTPS is not yet supported so be careful when using this in production systems.

<!---
## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```
--->

## Usage

While running, the application can be accessed in a web browser at http://127.0.0.1:5000, http://localhost:5000, etc. This loads the basic web page with flavor text surrounding the password. 

Alternatively, accessing http://127.0.0.1:5000/api will only return a plain-text password. This is better for making REST calls when utilizing the application as part of a larger workflow.

In PowerShell

```
$password = (Invoke-WebRequest -uri http://127.0.0.1/api -UseBasicParsing).content
```

In Bash

```
curl http://127.0.0.1/api
```

### Advanced Usage

Change all user's passwords in Active Directory to a random value and ouput the results.

```
$ADUserList = Get-ADUser -Searchbase "OU=Users,dc=domain,dc=net" - Filter *
Foreach-Object $ADUserList {
    $password = (Invoke-WebRequest -uri http://127.0.0.1/api -UseBasicParsing).content
    $securepassword = ConvertTo-SecureString $password -AsPlainText -Force
    Set-ADAccountPassword -Identity $_ -Reset -NewPassword $password
    Write-Host $_.UserPrincipalName ' password set to: '$password
}
```

## Built With

* [Flask](http://flask.pocoo.org/) - Web development microframework for Python
* [Python3](https://www.python.org/download/releases/3.0/) - The Language

<!---

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

--->

## Authors

* **Christopher Tagliaferro** - *Initial work* - [christag](https://github.com/christag)

<!---
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
--->

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Thanks to [PurpleBooth](https://gist.github.com/PurpleBooth) for this great [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* Inspired by [bbusschots](https://github.com/bbusschots)'s [xpasswd.net](https://xkpasswd.net), powered by [hsxkpasswd](https://github.com/bbusschots/hsxkpasswd)