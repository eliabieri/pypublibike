import unittest
import os
import json
from pypublibike.station import Station
from pypublibike.location import Location


class TestStation(unittest.TestCase):

    @staticmethod
    def getSampleJson(_unused):
        with open(os.path.join("test", "test_data", "station_happyday.json")) as f:
            sampleJson = f.read()
            return json.loads(sampleJson)

    def test_happyday(self):
        stationId = 123
        station = Station(stationId)
        station._retrieveStation = self.getSampleJson

        station.refresh()
        self.assertEqual(station.name, "Köniz Zentrum")
        self.assertTrue(station.active)
        self.assertEqual(station.address, "Bläuacker 10")
        self.assertEqual(station.zip, 3098)
        self.assertEqual(station.city, "Köniz")
        self.assertEqual(station.bikes[0].name, 102783)
        self.assertEqual(station.ebikes[0].name, 501352)
        self.assertEqual(station.ebikes[0].batteryLevel, 44)
        self.assertEqual(station.location, Location(46.9229774, 7.4141121))
        self.assertEqual(station.stationId, stationId)

    @staticmethod
    def test_live():
        station = Station(421)
        station.refresh()


if __name__ == '__main__':
    unittest.main()
