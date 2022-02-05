# mta-api
Simple flask api. Countdown to next train for each station in the subway system. 
Uses MTA Realtime Feeds: https://api.mta.info/#/subwayRealTimeFeeds

To run:

1) Create virtual environment and activate:

`python3 -m venv env`

`source env/bin/activate`

2) Install requirements:

`pip install -r requirements.txt`

3) Get api key from https://api.mta.info/#/AccessKey and store the following in a .env file in the root of the directory:

`MTA_API_KEY="<api-key>"`

`export FLASK_ENV=development`

`export FLASK_APP=index.py`

4) Run Flask app

`flask run`

5) To find the next train for the stop, go to 'http://localhost:5000/api/stops/' to find your station. Note down the `station_id` field. For ex. `Times Sq-42 St` has the `station_id` = 38.

6) Navigate to:

http://localhost:5000/api/train_times/38

## API fields:

- `direction`: `N` (uptown), `S`(downtown)
- `times`: time in seconds to next trains
- `route_id`: The route name for the train, see `subway_metadata/routes.csv` for the routes table.

## Notes:
Things to add:
- Subway alerts and delays
