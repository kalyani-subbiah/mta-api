import geopy.distance
import pandas as pd
from utils import get_sorted

STOPS_FILE = "subway_metadata/stops.csv"

class Stops:
  def __init__(self):
    self.stops_file = STOPS_FILE

  class _Stop:
    def __init__(self, stop_id):
      self.stop_id = stop_id
      stops_df = pd.read_csv(STOPS_FILE)
      self.stop_row = stops_df.loc(stops_df['stop_id'] == self.stop_id)

    def __getattr__(self, name): 
        if name == 'stop_name':
            return str(stop_row['stop_name'])
        elif name == 'stop_lat':
          return str(stop_row['stop_lat'])
        elif name == 'stop_lon':
          return str(stop_row['stop_lon'])
        return getattr(self._pb_data, name) 
  
  def get_nearest_stops(self, location_coords):
    distances = []
    for stop_id in self.stops_file['stop_id']:
      stop = self._Stop(stop_id)
      stop_coords=(stop.lat, stop.lon)
      distances.append({stop_id: self.get_distance(stop_coords, location_coords)})





  

  @staticmethod
  def get_distance(coords1, coords2):
    return geopy.distance.vincenty(coords1, coords2).miles