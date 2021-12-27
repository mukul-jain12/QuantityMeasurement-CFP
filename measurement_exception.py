"""
    @File :   measurement_exception.py
    @Author : mukul
    @Date :   23-12-2021
"""


class MeasurementException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
