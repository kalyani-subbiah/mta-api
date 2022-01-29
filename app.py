from flask import Flask, jsonify
from flask_cors import CORS

from markupsafe import escape 
from subway_api import SubwayApi

# __name__ = name of current module
app = Flask(__name__)
CORS(app)

@app.route('/')
def homepage1():
  return 'Welcome to SubwayApi'

@app.route('/api/')
def homepage2():
  return 'Welcome to SubwayApi'

@app.route('/api/stops/<stop_id>')
def nextTrain(stop_id):
  routes = SubwayApi(stop_id).stop_times
  return jsonify(routes)