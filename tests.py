#!/usr/bin/env python3

import unittest
from shopping import shopping

class UnitTests(unittest.TestCase):
   def test_null_strings(self):
      result = shopping("")
      self.assertTrue(result.startswith("Invalid"))

   def test_invalid_characters(self):
      result = shopping("fmep, gorp, 324, 567, 9800, 12")
      self.assertTrue(result.startswith("Invalid"))

   def test_valid_numbers(self):
      result = shopping("9800, 100, 23, 45, 16")
      self.assertEqual(result, 4)

   def test_data_provided(self):
      result = shopping("9850, 100, 30, 30, 100, 50, 100")
      self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
