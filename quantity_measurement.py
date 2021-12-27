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

    def __eq__(self, other):
        if other.length is None:
            raise MeasurementException("Null")
        if self.length != other.length:
            raise MeasurementException("Values are different")
        if type(self.length) != type(other.length):
            raise MeasurementException("Have different type")
        if self.unit == other.unit and other.length == self.length:
            return True
