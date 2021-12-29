import pytest
from quantity_measurement import QuantityMeasurement
from feet import Feet
from inch import Inch
from yard import Yard
from measurement_exception import MeasurementException


class TestCase:
    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 0.0, Feet.FEET, 0.0), (Inch.INCH, 0.0, Inch.INCH, 0.0),
                              (Yard.YARD, 0.0, Yard.YARD, 0.0)])
    def test_compare_two_having_zero_values(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having zero length and same unit
            :param first_unit - assign unit(eg: feet, inch, yard):
            :param first_length - assign length/value:
            :param second_unit - assign unit(eg: feet, inch, yard):
            :param second_length - assign length/value:
            :return True:
        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = QuantityMeasurement(second_unit, second_length)
        assert first_obj == second_obj

    @pytest.mark.parametrize("first_length", [2.0])
    def test_compare_two_same_feet_objects(self, first_length):
        """
            desc: check two object reference are same or not
            :param first_length - assign length/value:
            :return: True
        """
        first_obj = Feet(first_length)
        second_obj = first_obj
        assert first_obj == second_obj

    @pytest.mark.parametrize("first_length", [5.0])
    def test_compare_two_same_inch_objects(self, first_length):
        first_obj = Inch(first_length)
        second_obj = first_obj
        assert first_obj == second_obj

    @pytest.mark.parametrize("first_length", [2.0])
    def test_compare_two_same_yard_objects(self, first_length):
        first_obj = Yard(first_length)
        second_obj = first_obj
        assert first_obj == second_obj

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 2.0, Feet.FEET, None), (Inch.INCH, 2.0, Inch.INCH, None),
                              (Yard.YARD, 2.0, Yard.YARD, None)])
    def test_raise_exception_on_null_value(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having null value in one object and same unit
            :param first_unit - assign unit(eg: feet, inch, yard):
            :param first_length - assign length/value:
            :param second_unit - assign unit(eg: feet, inch, yard):
            :param second_length - assign length/value:
            :return True:
        """
        with pytest.raises(MeasurementException) as exception:
            first_obj = QuantityMeasurement(first_unit, first_length)
            second_obj = QuantityMeasurement(second_unit, second_length)
            first_obj == second_obj
        assert exception.value.message == "Null"

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 0.0, Feet.FEET, 0), (Inch.INCH, 3.0, Inch.INCH, 3),
                              (Yard.YARD, 6.0, Yard.YARD, 6)])
    def test_raise_exception_on_different_type_values(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having same length and same unit but type is different
            :param first_unit - assign unit(eg: feet, inch, yard):
            :param first_length - assign length/value:
            :param second_unit - assign unit(eg: feet, inch, yard):
            :param second_length - assign length/value:
            :return True:
        """
        with pytest.raises(MeasurementException) as exception:
            first_obj = QuantityMeasurement(first_unit, first_length)
            second_obj = QuantityMeasurement(second_unit, second_length)
            first_obj == second_obj
        assert exception.value.message == "Have different type"

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 0.0, Feet.FEET, 1.0), (Inch.INCH, 0.0, Inch.INCH, 1.0),
                              (Yard.YARD, 0.0, Yard.YARD, 1.0)])
    def test_two_different_unit_value(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having different length and same unit
            :param first_unit - assign unit(eg: feet, inch, yard):
            :param first_length - assign length/value:
            :param second_unit - assign unit(eg: feet, inch, yard):
            :param second_length - assign length/value:
            :return True:
        """
        with pytest.raises(MeasurementException) as exception:
            first_obj = QuantityMeasurement(first_unit, first_length)
            second_obj = QuantityMeasurement(second_unit, second_length)
            first_obj == second_obj
        assert exception.value.message == "Values are different"

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 1.0, Inch.INCH, 12.0), (Inch.INCH, 12.0, Feet.FEET, 1.0), (Feet.FEET, 3.0, Yard.YARD, 1.0),
                              (Yard.YARD, 1.0, Feet.FEET, 3.0), (Yard.YARD, 3.0, Inch.INCH, 36.0), (Inch.INCH, 36.0, Yard.YARD, 3.0)])
    def test_compare_two_having_different_units(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having different length and different unit
            :param first_unit - assign unit(eg: feet, inch, yard):
            :param first_length - assign length/value:
            :param second_unit - assign unit(eg: feet, inch, yard):
            :param second_length - assign length/value:
            :return True:
        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = QuantityMeasurement(second_unit, second_length)
        assert first_obj == second_obj

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 1.0, Inch.INCH, 1.0), (Inch.INCH, 1.0, Feet.FEET, 1.0),
                              (Feet.FEET, 1.0, Yard.YARD, 1.0), (Yard.YARD, 1.0, Feet.FEET, 1.0)])
    def test_compare_two_having_different_units(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having same length and different unit
            :param first_unit - assign unit(eg: feet, inch, yard):
            :param first_length - assign length/value:
            :param second_unit - assign unit(eg: feet, inch, yard):
            :param second_length - assign length/value:
            :return True:
        """
        with pytest.raises(MeasurementException) as exception:
            first_obj = QuantityMeasurement(first_unit, first_length)
            second_obj = QuantityMeasurement(second_unit, second_length)
            first_obj == second_obj
        assert exception.value.message == "Different units don't have same length"
