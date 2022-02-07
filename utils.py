from datetime import date


def get_route_id(entity):
  # get route id to get info on where the train is going
  return entity["tripUpdate"]["trip"]["routeId"]

def get_updates(entity):
  updates = entity["tripUpdate"]["stopTimeUpdate"]
  return updates
"""
def get_sorted(dict1):
  In a dict where the values are lists, sort the lists
  return [{'route': k, 'times': v} for k, v in sorted(dict1.items(), key=lambda item: item[1])]
"""
