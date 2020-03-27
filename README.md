⚡️🚲 pypublibike - A python wrapper round the PubliBike API
===============================

![Upload Python Package](https://github.com/eliabieri/pypublibike/workflows/Upload%20Python%20Package/badge.svg)

[![PyPI version](https://badge.fury.io/py/pypublibike.svg)](https://badge.fury.io/py/pypublibike)

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/eliabieri/pypublibike/?ref=repository-badge)

pypublibike makes it easy to access the PubliBike API in your own Python projects.

Quick Start
-----------
    $ pip install pypublibike

Examples
-----------

Getting a list of all PubliBike stations

```python
from pypublibike import publibike, station

pb = publibike.PubliBike()
for station in pb.getStations():
	station.refresh() 		# refresh load data of station
	ebike = station.ebikes[0] 	# access the bikes/ebikes of the station
	ebike.batteryLevel 		# access information about a bike
```

Finding the nearest PubliBike station

```python
from pypublibike import publibike, location

pb = publibike.PubliBike()
ourLocation = location.Location(latitude=46.950043, longitude=7.443169)

nearestStation = pb.findNearestStationTo(ourLocation)

nearestStation.refresh()
print(nearestStation.name)
```


Getting Help
------------

* Open a issue on GitHub if you run into any problems

* Contact me on [Twitter](https://twitter.com/eliabieri)

Todo
------------

 * API documentation
 * Error handling
