import pytest
from quantity_measurement import QuantityMeasurement
from length_conversion import Conversion
from feet import Feet
from measurement_exception import MeasurementException


def test_compare_two_same_feet_values():
    first_feet = QuantityMeasurement(Conversion.FEET, 2.0)
    second_feet = QuantityMeasurement(Conversion.FEET, 2.0)
    assert first_feet == second_feet


def test_compare_two_same_feet_objects():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


def test_check_null_in_feet():
    with pytest.raises(MeasurementException) as exception:
        first_feet = QuantityMeasurement(Conversion.FEET, 0.0)
        second_feet = QuantityMeasurement(Conversion.FEET, None)
        first_feet == second_feet
    assert exception.value.message == "Null"


def test_check_type_in_feet():
    with pytest.raises(MeasurementException) as exception:
        first_feet = QuantityMeasurement(Conversion.FEET, 0.0)
        second_feet = QuantityMeasurement(Conversion.FEET, 0)
        first_feet == second_feet
    assert exception.value.message == "Have different type"


def test_two_different_feet_value():
    with pytest.raises(MeasurementException) as exception:
        first_feet = QuantityMeasurement(Conversion.FEET, 0.0)
        second_feet = QuantityMeasurement(Conversion.FEET, 1.0)
        first_feet == second_feet
    assert exception.value.message == "Values are different"
