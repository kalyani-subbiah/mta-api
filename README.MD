# subway-countdown-api
Simple flask api. Countdown to next train for each station in the subway system. 
Uses MTA Realtime Feeds: https://api.mta.info/#/subwayRealTimeFeeds

To run:

1) Create virtual environment and activate:

`python3 -m venv env`

`source env/bin/activate`

2) Install requirements:

`pip install -r requirements.txt`

3) Get api key from https://api.mta.info/#/AccessKey and store in a .env file in the root of the directory:

`MTA_API_KEY="<api-key>"`

4) Run Flask app

`export FLASK_ENV=development`
`export FLASK_APP=index.py`
`flask run`

5) To find the next train for the stop, got to `subway_metadata/stops.csv` to find your stop. For example, 137th St City College Station is code '115'. (Do not enter 115N or 115S)

6) Navigate to:

http://127.0.0.1:5000/api/stops/115

## API fields:

`direction`: `N` (uptown), `S`(downtown)
`nextTime`: time in seconds to next train
`route_id`: The route name for the train, see `subway_metadata/routes.csv` for the routes table.

## Notes:
Things to add:
- Subway alerts and delays