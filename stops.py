import pandas as pd

STOPS_FILE = "subway_metadata/stops.csv"

class Stops:
  def __init__(self):
    self.stops_file = STOPS_FILE
    self.stops_df = pd.read_csv(STOPS_FILE)
    self.stops = self.get_stops()
  
  def get_stop_info(self,stop_id):
    stop_row = self.stops_df.loc[self.stops_df['stop_id'] == stop_id]
    return {'stop_id':stop_id, 'name': str(stop_row['stop_name'].item()), 'lat': str(stop_row['stop_lat'].item()), 'lon': str(stop_row['stop_lon'].item())}

  def get_stops(self):
    stops = []
    for stop_id in self.stops_df['stop_id']:
      if stop_id[-1] == "N" or stop_id[-1] == "S":
        continue
      stops.append(self.get_stop_info(stop_id))
    return stops






  

 