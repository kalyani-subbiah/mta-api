import os

import requests
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict

load_dotenv()

class FeedParser:
  def __init__(self, ):
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