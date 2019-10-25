from pypublibike.station import Station
from pypublibike.location import Location
from haversine import haversine
import requests


class PubliBike:

    def findNearestStationTo(self, location: Location):
        stations = self.getStations()
        nearestStation = None
        distanceNearestStation = 100000
        for station in stations:
            distance = haversine(
                (station.location.latitude, station.location.longitude), (location.latitude, location.longitude))
            if distance < distanceNearestStation:
                nearestStation = station
                distanceNearestStation = distance
        return nearestStation

    def getStations(self) -> list:
        stations = []
        r = requests.get("https://api.publibike.ch/v1/public/stations/")
        for station in r.json():
            location = Location(
                float(station["latitude"]), float(station["longitude"]))
            stations.append(Station(station["id"], location))
        return stations
