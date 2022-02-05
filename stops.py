import time
import pandas as pd

STOPS_FILE = "subway_metadata/stops.csv"

class Stops:
  def __init__(self):
    self.stops_file = STOPS_FILE
    self.stops_df = pd.read_csv(STOPS_FILE)
    self.stops = self.get_stops()

  def get_stops(self):
    stops = {}
    names = list(set(self.stops_df['stop_name']))
    count = 0
    for stop_name in names:
      stops[stop_name] = {'station_id': count, 'name': stop_name, 'stop_ids': []}
      loc = False
      for row in self.stops_df.itertuples():
        if row.stop_name == stop_name:
          if loc == False:
            stops[stop_name]['lat'] = row.stop_lat
            stops[stop_name]['lng'] = row.stop_lon
            loc = True
          stopId = row.stop_id
          if stopId[-1] == "N" or stopId[-1] == "S":
            continue
          else:
            stops[stop_name]['stop_ids'].append(stopId)
      count += 1
    stops2 = []
    for stop_name in stops.keys():
      stops2.append(stops[stop_name])
    return stops2






  

 