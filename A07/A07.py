#!/usr/bin/python3

import plotly
import plotly.graph_objects as go
from geo import mapbox_access_token
from geo import get_country_border
from geo import get_bbox
from geo import get_airports
from geo import get_earthquakes
from geo import get_meteorites
from geo import get_ufos
from geo import get_volcanoes


if __name__ == '__main__':
    mapbox_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"

    airLats,airLons = get_airports()
    earthLats, earthLons = get_earthquakes()
    meteorLats, meteorLons = get_meteorites()
    ufoLats, ufoLons = get_ufos()
    volcanoLats, volcanoLons = get_volcanoes()

    airports = [go.Scattermapbox(
        lat=airLats,
        lon = airLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='green',
            opacity = .8,
        ),
        name='Airports'
    )]
    earthquakes = [go.Scattermapbox(
        lat=earthLats,
        lon = earthLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='orange',
            opacity = .8,
        ),
        name='Earthquakes'
    )]
    meteorites = [go.Scattermapbox(
        lat=meteorLats,
        lon = meteorLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='cyan',
            opacity = .8,
        ),
        name='Meteorites'
    )]
    ufos = [go.Scattermapbox(
        lat=ufoLats,
        lon = ufoLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='blue',
            opacity = .8,
        ),
        name='Ufo Sightings'
    )]
    volcanoes = [go.Scattermapbox(
        lat=volcanoLats,
        lon = volcanoLons,
        mode = 'markers',
        marker=dict(
            size=4,
            color='red',
            opacity = .8,
        ),
        name='Volcanoes'
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
    title = "Armageddon")

    fig = dict(data=airports+earthquakes+meteorites+ufos+volcanoes, layout=layout)
    plotly.offline.plot(fig, filename='armageddon.html')