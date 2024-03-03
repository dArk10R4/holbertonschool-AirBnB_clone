#!/usr/bin/python3

"""Unittest for Amenity"""

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    amenity = None

    def setUp(self) -> None:
        self.amenity = Amenity()

    def tearDown(self) -> None:
        del self.amenity

    def test_create_amenity(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)
        del amenity

    def test_name(self):
        self.assertEqual(self.amenity.name, "")
        self.amenity.name = "Wifi"
        self.assertEqual(self.amenity.name, "Wifi")


if __name__ == "__main__":
    unittest.main()
