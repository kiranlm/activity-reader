import gpxpy
import gpxpy.gpx
import pandas as pd
import json

# Parsing an existing file:
# -------------------------
def parseGpx(gpxFile):

    gpx_file = open('tcs.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)
    eventTime=gpx.time
    eventName=gpx.tracks[0].name

    data = gpx.tracks[0].segments[0].points

    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
    for point in data:
        df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)

    # print(df)
    jsonfiles = json.loads(df.to_json(orient='records'))
    return {"data":jsonfiles,"name":eventName,"time":eventTime}