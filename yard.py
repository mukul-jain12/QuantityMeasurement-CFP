"""
    @File :   yard.py
    @Author : mukul
    @Date :   27-12-2021
"""


class Yard:
    YARD = 0.33

    def __init__(self, yard):
        self.yard = yard

    def __eq__(self, other):
        if isinstance(other, Yard):
            if self.yard == other.yard:
                return True
        return False