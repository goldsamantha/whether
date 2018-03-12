# Whether weather

This is a simple api that will tell you if it's going to rain or snow in the next 12 hours. That's it! : )

### Install requisite libs:
```
pip install -r requirements.txt
```

### Set up your environment
You'll need to get an api key from [darksky](https://darksky.net/dev/register). In order for this to work, you'll also need to get your latitude and longitude as strings

Sample export from Brooklyn:
```
$ export DS_LAT="40.671365" DS_LON="-73.969434" DS_KEY="<your api key>"
```

### Run app on port 5001
```
$ FLASK_APP=app.py flask run --port=5001
```
View at http://localhost:5001/
