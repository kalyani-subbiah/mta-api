# https://bennettgarner.medium.com/parsing-gtfs-format-transit-data-in-real-time-with-python-3a528ba7aab7
import time
import os

from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests

from dotenv import load_dotenv
from feed_entity_utils import get_route_id, get_updates

load_dotenv()

class SubwayApi:
  def __init__(self, closest_stop_id):
    self.next_refresh = 60
    self.closest_stop_id = str(closest_stop_id)
    
    self.urls_dict = {
      'ACE': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace',
      'BDFM': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
      'G': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g',
      'JZ': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
      'NQRW': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
      'L': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l',
      '1234567': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
      'SIR': 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si'
      }
    self.headers = {"x-api-key": os.getenv("MTA_API_KEY")}

    self.feed = self.combine_feeds()
    self.next_train_time = self.get_next_train_for_stop()
  
  def get_feed(self, url):
    feed = gtfs_realtime_pb2.FeedMessage()
    # get response from api
    response = requests.get(url, headers=self.headers)
    # pass response to parser
    feed.ParseFromString(response.content)
    return MessageToDict(feed)

  def combine_feeds(self):
    feeds = []
    for url in self.urls_dict.values():
      feeds.append(self.get_feed(url)['entity'])
    # unpack 2d list
    feed = [j for sub in feeds for j in sub]
    return feed
  
  def get_times_for_stop(self, entity, routes):
    """Gets all the next times for each train arriving in the subway station
    Each train is marked by a route. For ex. FX = Brooklyn F Express.
    Includes directions uptown and downtown, which is reflected in the stop id"""
    updates = get_updates(entity)
    for update in updates:
      if update["stopId"] == self.closest_stop_id + 'N' or update["stopId"] == self.closest_stop_id + 'S':
        time_difference = self.get_time_difference(update)
        if time_difference > 0 and time_difference < 1800:
          # add direction to route id
          route_id = get_route_id(entity) + "+" + update["stopId"][-1]
          if route_id not in routes:
            routes[route_id] = []
          routes[route_id].append(time_difference)
    return routes

  def get_next_train_for_stop(self):
    """Get the minimum/next time for each train's arrival at the station"""
    routes = {}
    for entity in self.feed:
      if 'tripUpdate' in entity.keys() and "stopTimeUpdate" in entity['tripUpdate'].keys(): 
        routes = self.get_times_for_stop(entity, routes) 
    routes = self.get_mins(routes)
    routes = self.split_directions(routes)
    return routes      
  
  @staticmethod
  def get_mins(dict_of_lists):
    return [{'route': k, 'nextTime': min(x)} if x != [] else None for (k,x)  in dict_of_lists.items()]

  @staticmethod
  def split_directions(routes):
    for route in routes:
      route["route_id"] = route["route"].split("+")[0]   
      route["direction"] = route["route"].split("+")[1] 
      route = route.pop("route")
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