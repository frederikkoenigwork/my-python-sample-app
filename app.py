import flask
from flask import Flask
from flask import request, jsonify
from inspect import getmembers
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def hello():
    return "In Python we trust!"

@app.route("/trust")
def trust():
    return "In Python we trust!"

@app.route("/req")
def req():
    pprint(getmembers(request))
    return ""

@app.route('/calc/<x>/<y>')
def calc(x=0,y=0):
  return str(int(x)*int(y))



# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


