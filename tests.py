import roman_1
import unittest
from conversions import (
    convert_celsius_to_kelvin, convert_celsius_to_fahrenheit
)


class KnownValues(unittest.TestCase):
    case_1 = (
        (1, 274.15),
        (2, 275.15),
        (0, 273.15),
        (-5, 268.15),
        (100, 373.15)
    )

    def test_convert_celsius_to_kelvin(self):
        for celsius, kelvin in self.case_1:
            result = convert_celsius_to_kelvin(celsius)
            self.assertEqual(kelvin, result)

    case_2 = (
        (1, 33.8),
        (2, 35.6),
        (0, 32.0),
        (-5, 23.0),
        (100, 212.0)
    )

    def test_convert_celsius_to_fahrenheit(self):
        for celsius, fahrenheit in self.case_2:
            result = convert_celsius_to_fahrenheit(celsius)
            self.assertEqual(fahrenheit, result)


if __name__ == '__main__':
    unittest.main()
