import gpxpy
import gpxpy.gpx
import pandas as pd

# Parsing an existing file:
# -------------------------
def parseGpx(gpxFile):

    print(type(gpxFile))
    gpx_file = open('tcs.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)

    data = gpx.tracks[0].segments[0].points
    # There are many more utility methods and functions:
    # You can manipulate/add/remove tracks, segments, points, waypoints and routes and
    # get the GPX XML file from the resulting object:

    print('GPX:', data)
    ## Start Position
    start = data[0]
    ## End Position
    finish = data[-1]
    print(start)
    print(finish)


    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
    for point in data:
        df = df.append({'lon': point.longitude, 'lat' : point.latitude, 'alt' : point.elevation, 'time' : point.time}, ignore_index=True)

    print(df)
    return True