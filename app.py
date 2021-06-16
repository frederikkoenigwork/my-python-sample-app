from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!"

@app.route('/calc/<x>/<y>')
def calc(x=0,y=0):
  return str(int(x)*int(y))
