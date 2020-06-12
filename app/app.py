from flask import Flask,request, jsonify, make_response
from functools import wraps
import gpxpy
import gpxpy.gpx
import pandas as pd
import json
import os
from redis import Redis
import io

app = Flask(__name__)

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route("/")
def get_initial_response():
    """Welcome"""
    redis.incr('hits')
    return 'Redis ({}) hit counter: {}'.format(REDIS_HOST, redis.get('hits'))

@app.route('/api/v1/process-gpx', methods=['POST'])
def process_gpx():
    gpxFile = request.files['gpx']
    with io.TextIOWrapper(gpxFile) as f:
        # return jsonify(data)
        data = parseGpx(f)
        return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp

# Parsing an existing file:
# -------------------------
def parseGpx(gpxFile):
    
    gpx = gpxpy.parse(gpxFile)
    eventTime=gpx.time
    eventName=gpx.tracks[0].name

    data = gpx.tracks[0].segments[0].points

    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
    for point in data:
        df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)

    # print(df)
    jsonfiles = json.loads(df.to_json(orient='records'))
    return {"data":jsonfiles,"name":eventName,"time":eventTime}

if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True, host='0.0.0.0', port=os.environ['BIND_PORT'])
