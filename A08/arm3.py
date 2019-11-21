import pymongo
import plotly
import plotly.graph_objects as go

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

mapbox_access_token = "pk.eyJ1IjoiYnNoZWw0MTkiLCJhIjoiY2sxcmZoNWR1MDRxYjNjbzAwdDFwZGk0ayJ9.pM-XmYLU6phpO3EJ6JkPsQ"
mapbox_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"

crashes = db["plane_crashes"]

redLats = []
redLons = []

orangeLats = []
orangeLons = []

yellowLats = []
yellowLons = []

blueLats = []
blueLons = []

for obj in crashes.find():
    if obj["TotalFatalInjuries"] != '  ' and obj["TotalFatalInjuries"] is not None:
        if int(obj["TotalFatalInjuries"]) >= 300:
            redLats.append(obj["Latitude"])
            redLons.append(obj["Longitude"])
        elif int(obj["TotalFatalInjuries"]) >= 200:
            orangeLats.append(obj["Latitude"])
            orangeLons.append(obj["Longitude"])
        elif int(obj["TotalFatalInjuries"]) >= 100:
            yellowLats.append(obj["Latitude"])
            yellowLons.append(obj["Longitude"])
        else:
            blueLats.append(obj["Latitude"])
            blueLons.append(obj["Longitude"])
    else:
        blueLats.append(obj["Latitude"])
        blueLons.append(obj["Longitude"])

red = [go.Scattermapbox(
        lat=redLats,
        lon =redLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='red',
            opacity = .8,
        ),
        name="More than 300 Fatalities"
    )]

orange = [go.Scattermapbox(
        lat=orangeLats,
        lon =orangeLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='orange',
            opacity = .8,
        ),
        name="200-300 Fatalities"
    )]

yellow = [go.Scattermapbox(
        lat=yellowLats,
        lon =yellowLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='yellow',
            opacity = .8,
        ),
        name="100-200 Fatalities"
    )]

blue = [go.Scattermapbox(
        lat=blueLats,
        lon =blueLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='blue',
            opacity = .8,
        ),
        name="Less than 100 Fatalities"
    )]

layout = go.Layout(autosize=True,
    mapbox = dict(accesstoken= mapbox_access_token,
    bearing=0,
    pitch=0,
    zoom=5,
    center=dict(lat=0,lon=0),
    style=mapbox_style),
    width=1500,
    height=1080,
    title = "Arm3")

fig = dict(data=red+orange+yellow+blue, layout=layout)
plotly.offline.plot(fig, filename='Arm3.html')
