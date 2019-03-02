# flaskpass
Password generator built using Python3 and Flask.

Requirements are:
- Python3
- Flask

To run this app on its own, run flaskpass.py. This app can also be run in docker by running 'docker-compose up' from this folder.

There are two endpoints:
- / : This loads index.html and is intended for a graphical interaction
 - /api : Returns a plaintext generated password. Meant to be used with by REST GET.
