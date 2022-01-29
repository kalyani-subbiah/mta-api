from flask import Flask, jsonify
from flask_cors import CORS

from markupsafe import escape 
from routes import Routes

# __name__ = name of current module
app = Flask(__name__)
CORS(app)

@app.route('/')
def homepage1():
  return 'Welcome to SubwayApi'

@app.route('/api/')
def homepage2():
  return 'Welcome to SubwayApi'

@app.route('/api/train_times/')
def routes():
  routes = Routes().routes
  return jsonify(routes)

@app.route('/api/train_times/<stop_id>')
def nextTrain(stop_id):
  routes = Routes().routes
  return jsonify({stop_id: routes[stop_id]})