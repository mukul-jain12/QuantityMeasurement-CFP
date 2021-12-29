"""
    @File :   quantity_measurement.py
    @Author : mukul
    @Date :   26-12-2021
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def convert(self, unit, length):
        return unit * length

    def __eq__(self, other):
        if other.length is None:
            raise MeasurementException("Null")
        if self.unit != other.unit and other.length != self.length:
            return self.convert(self.unit, self.length) == self.convert(other.unit, other.length)
        if self.unit != other.unit and other.length == self.length:
            raise MeasurementException("Different units don't have same length")
        if self.length != other.length:
            raise MeasurementException("Values are different")
        if type(self.length) != type(other.length):
            raise MeasurementException("Have different type")
        if self.unit == other.unit and other.length == self.length:
            return True

