"""
    @File :   inch.py
    @Author : mukul
    @Date :   27-12-2021
"""


class Inch:
    INCH = 1.0

    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Inch):
            if self.inch == other.inch:
                return True
        return False
