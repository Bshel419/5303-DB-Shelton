import pymongo
import plotly
import plotly.graph_objects as go

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

mapbox_access_token = "pk.eyJ1IjoiYnNoZWw0MTkiLCJhIjoiY2sxcmZoNWR1MDRxYjNjbzAwdDFwZGk0ayJ9.pM-XmYLU6phpO3EJ6JkPsQ"
mapbox_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"

volcanoes = db["volcanoes"]

worstPEIs = []
worstGeo = []
worstNames = []

for obj in volcanoes.find():
    if len(worstPEIs) < 3:
        worstPEIs.append(float(obj["properties"]["PEI"]))
        worstGeo.append((float(obj['geometry']['coordinates'][1]), float(obj['geometry']['coordinates'][0])))
        worstNames.append(obj["properties"]["V_Name"])
    else:
        for x in range(3):
            if obj["properties"]["PEI"] > worstPEIs[x]:
                worstPEIs[x] = obj["properties"]["PEI"]
                worstGeo[x] = (float(obj['geometry']['coordinates'][1]), float(obj['geometry']['coordinates'][0]))
                worstNames[x] = obj["properties"]["V_Name"]
                break

ranking = []

if worstPEIs[0] >= worstPEIs[1] and worstPEIs[0] >= worstPEIs[2]:
    ranking.append(0)
    if worstPEIs[1] >= worstPEIs[2]:
        ranking.append(1)
        ranking.append(2)
    else:
        ranking.append(2)
        ranking.append(1)
elif worstPEIs[1] >= worstPEIs[2]:
    ranking.append(1)
    if worstPEIs[0] >= worstPEIs[2]:
        ranking.append(0)
        ranking.append(2)
    else:
        ranking.append(2)
        ranking.append(0)
else:
    ranking.append(2)
    if worstPEIs[0] >= worstPEIs[1]:
        ranking.append(0)
        ranking.append(1)
    else:
        ranking.append(1)
        ranking.append(0)

nLat, nLon = worstGeo[ranking[0]]
worstLat = []
worstLat.append(nLat)
worstLon = []
worstLon.append(nLon)
worst = [go.Scattermapbox(
        lat=worstLat,
        lon =worstLon,
        mode = 'markers',
        marker=dict(
            size=4,
            color='red',
            opacity = .8,
        ),
        name=worstNames[ranking[0]]
    )]

nLat, nLon = worstGeo[ranking[1]]
worstLat = []
worstLat.append(nLat)
worstLon = []
worstLon.append(nLon)
secondWorst = [go.Scattermapbox(
        lat=worstLat,
        lon =worstLon,
        mode = 'markers',
        marker=dict(
            size=4,
            color='red',
            opacity = .8,
        ),
        name=worstNames[ranking[1]]
    )]

nLat, nLon = worstGeo[ranking[2]]
worstLat = []
worstLat.append(nLat)
worstLon = []
worstLon.append(nLon)
thirdWorst = [go.Scattermapbox(
        lat=worstLat,
        lon =worstLon,
        mode = 'markers',
        marker=dict(
            size=4,
            color='red',
            opacity = .8,
        ),
        name=worstNames[ranking[2]]
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
    title = "Arm2")

fig = dict(data=worst+secondWorst+thirdWorst, layout=layout)
plotly.offline.plot(fig, filename='arm2.html')
