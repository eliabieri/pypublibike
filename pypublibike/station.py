from pypublibike.location import Location
from pypublibike.bike import Bike, Ebike
from pypublibike.constants import Constants, API_BASE_URL
import requests
from typing import Optional, List


class Station:

    def __init__(self, stationId: int, location: Location = None):
        self._stationId = stationId
        self._stationActive = None
        self._active = None
        self._name = None
        self._location = None
        self._address = None
        self._zip = None
        self._city = None
        self._bikes: List[Bike] = []
        self._ebikes: List[Ebike] = []
        if location is not None:
            self._location = location

    def __repr__(self):
        return f"Station '{self._name}': Bikes = {len(self._bikes)} Ebikes = {len(self._ebikes)}"

    @staticmethod
    def _retrieveStation(_stationId: int):
        return requests.get(f'{API_BASE_URL}{_stationId}').json()

    def refresh(self):
        response = self._retrieveStation(self._stationId)
        self._active = Constants.ACTIVE == response[Constants.STATE][Constants.NAME]
        self._name = response[Constants.NAME]
        self._location = Location(
            float(response[Constants.LATITUDE]), float(response[Constants.LONGITUDE]))
        self._address = response[Constants.ADDRESS]
        self._zip = int(response[Constants.ZIP])
        self._city = response[Constants.CITY]
        vehicles = response[Constants.VEHICLES]

        self._ebikes.clear()
        for entry in filter(lambda vehicle: vehicle[Constants.TYPE][Constants.NAME] == Constants.EBIKE, vehicles):
            batteryLevel = 0
            if None is not entry[Constants.BATTERY_LEVEL]:
                batteryLevel = int(entry[Constants.BATTERY_LEVEL])
            self._ebikes.append(
                Ebike(int(entry[Constants.NAME]), batteryLevel))

        self._bikes.clear()
        for entry in filter(lambda vehicle: vehicle[Constants.TYPE][Constants.NAME] == Constants.BIKE, vehicles):
            self._bikes.append(Bike(int(entry[Constants.NAME])))

    @property
    def stationId(self) -> int:
        return self._stationId

    @property
    def active(self) -> Optional[bool]:
        return self._active

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def location(self) -> Optional[Location]:
        return self._location

    @property
    def address(self) -> Optional[str]:
        return self._address

    @property
    def zip(self) -> Optional[int]:
        return self._zip

    @property
    def city(self) -> Optional[str]:
        return self._city

    @property
    def bikes(self) -> List[Bike]:
        return self._bikes

    @property
    def ebikes(self) -> List[Ebike]:
        return self._ebikes
