from flask import Flask
from darksky import forecast
import requests, json, os

app = Flask(__name__)

@app.route("/")
def hello():
    lat = os.getenv("DS_LAT")
    lon = os.getenv("DS_LON")
    key = os.getenv("DS_KEY")

    cast = forecast(key, lat, lon)

    rain = False
    #TODO: do some proper error checking eventually 0.o
    if (len(cast.hourly) < 12):
        return json.dumps(False)

    for i in range(12):
        data = cast.hourly[i]
        if data.precipProbability > 0.4:
            rain = True

    return json.dumps(rain)
