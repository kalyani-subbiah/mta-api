import time

from feed_parser import FeedParser

from utils import get_updates, get_route_id, get_sorted

MAX_TIME_DIFFERENCE = 1800

class Routes:
  def __init__(self):
    self.feed = FeedParser().feed
    self.routes = self.get_routes()
  
  def process_update(self, entity, update, routes):
    time_difference = self.get_time_difference(update)
    print(update['stopId'])
    stopId = update['stopId'][:-1]
    if stopId not in routes.keys():
      routes[stopId] = {}
    if time_difference > 0 and time_difference < MAX_TIME_DIFFERENCE:
      # add direction to route id 
      # Direction is the last character 'N' or 'S' at the end of the stop Id
      route_id = get_route_id(entity) + "+" + update['stopId'][-1]
      if route_id not in routes[stopId]:
        routes[stopId][route_id] = []
      routes[stopId][route_id].append(time_difference)
    return routes
  
  def process_entity(self, entity, routes):
    if 'tripUpdate' in entity.keys() and "stopTimeUpdate" in entity['tripUpdate'].keys(): 
      updates = get_updates(entity)
      for update in updates:
        routes = self.process_update(entity, update, routes)
    return routes

  def get_routes(self):
    routes = {}
    for entity in self.feed:
      routes = self.process_entity(entity, routes)
    for stop_id in routes.keys():
      routes[stop_id] = get_sorted(routes[stop_id])
      routes[stop_id] = self.split_directions(routes[stop_id])
    return routes

  @staticmethod
  def get_time_difference(update):
    """Return time difference between current time and train arrival/departure time in seconds"""
    if "arrival" in update.keys():
      # time in gtfs feed is in POSIX
      return float(update["arrival"]["time"]) - time.time()
    elif "departure" in update.keys():
      return float(update["departure"]["time"]) - time.time()
    else: return None
  
  @staticmethod
  def split_directions(routes):
    for route in routes:
      route["route_id"] = route["route"].split("+")[0]   
      route["direction"] = route["route"].split("+")[1] 
      route = route.pop("route")
    return routes