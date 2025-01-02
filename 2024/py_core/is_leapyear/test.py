import unittest
from main import is_leap_year
# from solution import is_leap_year
class TestingIsLeapYear(unittest.TestCase):
    """ Class used to unit-test the leap year function. """
    def testing_is_leap_year(self):
        years = [2000, 2004, 2008, 2012, 2016, 2020,
                     2024, 2028, 2032, 2036, 2040, 2044, 2048]
        for year in years:
            self.assertEqual(is_leap_year(year), True)


if __name__ == "__main__":
    unittest.main()
