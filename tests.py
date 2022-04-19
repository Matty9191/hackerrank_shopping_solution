#!/bin/env python3

""" Test module """

import unittest
from shopping import shopping

class UnitTests(unittest.TestCase):
    """
       Purpose: Run unit tests to verify shopping method works
    """
    def test_null_strings(self):
        """ check if NULL values are handled properly """
        result = shopping("")
        self.assertTrue(result.startswith("Invalid"))

    def test_invalid_characters(self):
        """ Check it invalid inputs are handled properly """
        result = shopping("fmep, gorp, 324, 567, 9800, 12")
        self.assertTrue(result.startswith("Invalid"))

    def test_valid_numbers(self):
        """ Test valid data """
        result = shopping("9800, 100, 23, 45, 16")
        self.assertEqual(result, 4)

    def test_data_provided(self):
        """ Test the sample inputs from the coding exercise """
        result = shopping("9850, 100, 30, 30, 100, 50, 100")
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
