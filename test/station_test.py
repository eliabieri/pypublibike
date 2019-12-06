import unittest
import os
import json
from pypublibike.station import Station
from pypublibike.location import Location

class TestStation(unittest.TestCase):

    def getSampleJson(self, id:int) -> object:
        with open(os.path.join("test","test_data","station_happyday.json")) as f:
            sampleJson = f.read()
        sampleJson = json.loads(sampleJson)
        return sampleJson

    def test_happyday(self):
        id = 123
        station = Station(id)
        station._retrieveStation = self.getSampleJson

        station.refresh()
        self.assertEqual(station.name, "Köniz Zentrum")
        self.assertEqual(station.address, "Bläuacker 10")
        self.assertEqual(station.zip, 3098)
        self.assertEqual(station.city, "Köniz")
        self.assertEqual(station.numBikes, 0)
        self.assertEqual(station.numEbikes, 1)
        self.assertEqual(station.batteryLevels, [44])
        self.assertEqual(station.location, Location(46.9229774, 7.4141121))
        self.assertEqual(station._id, id)

if __name__ == '__main__':
    unittest.main()