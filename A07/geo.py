import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

mapbox_access_token = "pk.eyJ1IjoiYnNoZWw0MTkiLCJhIjoiY2sxcmZoNWR1MDRxYjNjbzAwdDFwZGk0ayJ9.pM-XmYLU6phpO3EJ6JkPsQ"

def get_country_border(country):
    global db
    countries = db["countries"]

    lines = []
    points = {'lat':[],'lon':[],'latlon':[]}

    for obj in countries.find({"properties.ADMIN" : country}, { "geometry.coordinates": 1, "_id": 0 }):
        lines.append(obj)
    
    for group in lines[0]['geometry']['coordinates']:
        #print(group)
        for line in group:
            #print(line)
            for point in line:
                points['lat'].append(point[1])
                points['lon'].append(point[0])
                points['latlon'].append(point)

    return points

def get_center_point(points):
    min_lat = 90
    max_lat = -90
    min_lon = 180
    max_lon = -180

    for point in points:
        if point[1] < min_lat:
            min_lat = point[1]
        if point[0] < min_lon:
            min_lon = point[0]
        if point[1] > max_lat:
            max_lat = point[1]
        if point[0] > max_lon:
            max_lon = point[0]

    return {"lon":(min_lon + max_lon)/2,"lat":(min_lat + max_lat)/2}

def get_bbox(points):
    min_lat = 90
    max_lat = -90
    min_lon = 180
    max_lon = -180
    
    for point in points:
        if point[1] < min_lat:
            min_lat = point[1]
        if point[0] < min_lon:
            min_lon = point[0]
        if point[1] > max_lat:
            max_lat = point[1]
        if point[0] > max_lon:
            max_lon = point[0]

    return {"lon":(min_lon + max_lon)/2,"lat":(min_lat + max_lat)/2,"min_lat":min_lat,"max_lat":max_lat,"min_lon":min_lon,"max_lon":max_lon}

def within_bbox(bbox,lat,lon):
    return (lat < bbox['max_lat'] and lat > bbox['min_lat'] and lon < bbox['max_lon'] and lon > bbox['min_lon'])


def get_airports():
    airports = db["airports"]
    lats = []
    lons = []
    for obj in airports.find():
        lat = float(obj['-6']['081689834590001'])
        lon = float(obj['145']['391998291'])
            #if within_bbox(bbox,lat,lon):
        lats.append(lat)
        lons.append(lon)
    return (lats,lons)


def get_earthquakes():
    earthquakes = db["earthquakes"]
    lats = []
    lons = []
    for obj in earthquakes.find():
        lat = float(obj['latitude'])
        lon = float(obj['longitude'])
            #if within_bbox(bbox,lat,lon):
        lats.append(lat)
        lons.append(lon)
    return (lats,lons)

def get_meteorites():
    meteors = db["meteorites"]
    lats = []
    lons = []
    for obj in meteors.find():
        latlon = obj['GeoLocation'][1:-1]
        if len(latlon.strip()) > 0:
            lat,lon = latlon.split(',')
            lat = float(lat)
            lon = float(lon)
            #if within_bbox(bbox,lat,lon):
            lats.append(lat)
            lons.append(lon)
    return (lats,lons)

def get_ufos():
    ufos = db["ufos"]
    lats = []
    lons = []
    for obj in ufos.find():
        lati = isinstance(obj['latitude'], int)
        loni = isinstance(obj['longitude'], int) 
        flat = isinstance(obj['latitude'], float)
        flon = isinstance(obj['longitude'], float)
        if (lati or flat) and (flat or flon):
            lat = float(obj['latitude'])
            lon = float(obj['longitude'])
            #if within_bbox(bbox,lat,lon):
            lats.append(lat)
            lons.append(lon)
    return (lats,lons)

def get_volcanoes():
    volcanoes = db["volcanoes"]
    lats = []
    lons = []
    for obj in volcanoes.find():
        lat = float(obj['geometry']['coordinates'][1])
        lon = float(obj['geometry']['coordinates'][0])
            #if within_bbox(bbox,lat,lon):
        lats.append(lat)
        lons.append(lon)
    return (lats,lons)
