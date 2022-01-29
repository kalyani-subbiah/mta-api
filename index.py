from flask import Flask, url_for, request, session, jsonify

from markupsafe import escape 
from subway_api import SubwayApi

# __name__ = name of current module
app = Flask(__name__)

@app.route('/api/')
def homepage():
  return 'Welcome to SubwayApi'

@app.route('/api/stops/<stop_id>')
def nextTrain(stop_id):
  routes = SubwayApi(stop_id).next_train_time
  return jsonify(routes)