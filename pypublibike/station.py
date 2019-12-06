from pypublibike.location import Location
import requests


class Station:

    def __init__(self, id: int, location: Location = None):
        self._id = id
        self._name = None
        self._location = None
        self._address = None
        self._zip = None
        self._city = None
        self._numEbikes = None
        self._numBikes = None
        self._batteryLevels = []
        if location is not None:
            self._location = location

    def _retrieveStation(self, id: int) -> str:
        return requests.get(f'https://api.publibike.ch/v1/public/stations/{id}').json()

    def refresh(self):
        response = self._retrieveStation(id)
        self._name = response["name"]
        self._location = Location(
            float(response["latitude"]), float(response["longitude"]))
        self._address = response["address"]
        self._zip = int(response["zip"])
        self._city = response["city"]
        vehicles = response["vehicles"]
        ebikes = list(filter(lambda vehicle: vehicle["type"]["name"] == "E-Bike", vehicles))
        bikes = list(filter(lambda vehicle: vehicle["type"]["name"] == "Bike", vehicles))
        self._numEbikes = len(ebikes)
        self._numBikes = len(bikes)
        self._batteryLevels = [ebike["ebike_battery_level"] for ebike in ebikes]

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> Location:
        return self._location

    @property
    def address(self) -> str:
        return self._address

    @property
    def zip(self) -> int:
        return self._zip

    @property
    def city(self) -> str:
        return self._city

    @property
    def numEbikes(self) -> int:
        return self._numEbikes

    @property
    def numBikes(self) -> int:
        return self._numBikes

    @property
    def batteryLevels(self) -> list:
        return self._batteryLevels
