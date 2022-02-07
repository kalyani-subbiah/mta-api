import time

from flask import Flask, jsonify
from flask_cors import CORS
from markupsafe import escape 

from times import Times
from stations import Stations
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
def train_times():
  trains = Times().train_times
  return jsonify(trains)

@app.route('/api/train_times/<station_id>')
def nextTrains(station_id):
  times = Times().train_times
  station_route = list(filter(lambda station: station['station_id'] == int(station_id), times))
  return jsonify(station_route)

@app.route('/api/stations/')
def stops():
  stations = Stations().stations
  return jsonify(stations)

@app.route('/api/routes/')
def routes():
  routes = Routes().routes
  return jsonify(routes)