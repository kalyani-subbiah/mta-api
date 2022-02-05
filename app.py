import time

from flask import Flask, jsonify
from flask_cors import CORS
from markupsafe import escape 

from routes import Routes
from stops import Stops

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

@app.route('/api/train_times/<station_id>')
def nextTrains(station_id):
  station_routes = []
  stops = Stops().stops
  routes = Routes().routes
  for stop in stops:
    if stop['station_id'] == int(station_id):
      for stopId in stop['stop_ids']:
        stop_routes = list(filter(lambda route: route['stop_id'] == stopId, routes))
        for route in stop_routes:
          route['station_id'] = station_id
          station_routes.append(route)
  return jsonify(station_routes)

@app.route('/api/stations/')
def stops():
  stops = Stops().stops
  return jsonify(stops)