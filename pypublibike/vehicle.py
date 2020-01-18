from pypublibike.location import Location

class Vehicle:

    def __init__(self, _id: int, _type: str, _stationId: int, _location: Location = None):
        self._id = _id
        self._name = None
        self._location = None  #The location is given as the stations ID           
        self._lastKnownLocation = None 
        self._stationId = _stationId
        self._type = _type
        self._eBikeBatteryLevel = None
        if _location is not None:
            self._location = _location
            self._lastKnownLocation = _location

    @property
    def id(self) -> int:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def batteryLevel(self) -> int:
        return self._eBikeBatteryLevel

    @property
    def location(self) -> Location:
        return self._lastKnownLocation

    @property
    def stationId(self) -> int:
        return self._stationId
