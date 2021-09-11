from pypublibike.station import Station
from pypublibike.location import Location
from pypublibike.constants import Constants, API_BASE_URL
from haversine import haversine
from typing import List
import requests


class PubliBike:

    @classmethod
    def findNearestStationTo(cls, location: Location):
        stations = cls.getStations()
        stations.sort(key=lambda station: haversine(
                (station.location.latitude, station.location.longitude), (location.latitude, location.longitude)))
        return stations[0]

    @classmethod
    def getStations(cls) -> List[Station]:
        r = requests.get(API_BASE_URL)
        return list(map(lambda station: Station(station[Constants.ID], Location(
                float(station[Constants.LATITUDE]), float(station[Constants.LONGITUDE]))), r.json()))
