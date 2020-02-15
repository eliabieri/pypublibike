from dataclasses import dataclass


@dataclass
class Bike():
    name: int


@dataclass
class Ebike(Bike):
    batteryLevel: int
