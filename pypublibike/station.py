from pypublibike.location import Location
from pypublibike.vehicle import Vehicle
import requests


class Station:

    def __init__(self, _id: int, location: Location = None):
        self._id = _id
        self._name = None
        self._location = None
        self._address = None
        self._zip = None
        self._city = None
        self._numEbikes = None
        self._numBikes = None
        self._batteryLevels = []
        self._vehicles = []
        if location is not None:
            self._location = location

    def _retrieveStation(self, _id: int):
        return requests.get(f'https://api.publibike.ch/v1/public/stations/{_id}').json()

    def refresh(self):
        response = self._retrieveStation(self._id)
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
        for bike in vehicles:
            self._vehicles.append(Vehicle(bike["id"],bike["type"]["name"],self._id,self._location))
        

        


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
    
    @property
    def vehicles(self) ->list:
       return self._vehicles
