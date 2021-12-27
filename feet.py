"""
    @File :   Feet
    @Author : mukul
    @Date :   26-12-2021
"""


class Feet:
    FEET = 1.0

    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            if self.feet == other.feet:
                return True
        return False