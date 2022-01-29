import geopy.distance
import pandas as pd
from utils import get_sorted

STOPS_FILE = "subway_metadata/stops.csv"

class Stops:
  def __init__(self):
    self.stops_file = STOPS_FILE
    self.stops_df = pd.read_csv(STOPS_FILE)
    self.stops = self.get_stops()
  
  def get_stop_info(self,stop_id):
    stop_row = self.stops_df.loc(self.stops_df['stop_id'] == self.stop_id)
    return {'stop_name': str(self.stop_row['stop_name']), 'stop_lat': str(self.stop_row['stop_lat']), 'stop_lon': str(self.stop_row['stop_lon'])}

  def get_stops(self):
    stops = {}
    for stop_id in self.stops_df['stop_id']:
      stops[stop_id] = self.get_stop_info(stop_id)
    return stops






  

 