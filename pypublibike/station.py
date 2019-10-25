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
        if location is not None:
            self._location = location

    def refresh(self):
        r = requests.get(
            'https://api.publibike.ch/v1/public/stations/{}'.format(self._id))
        self._name = r.json()["name"]
        self._location = Location(
            float(r.json()["latitude"]), float(r.json()["longitude"]))
        self._address = r.json()["address"]
        self._zip = int(r.json()["zip"])
        self._city = r.json()["city"]

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
