FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements
CMD ["python", "flaskpass.py"]