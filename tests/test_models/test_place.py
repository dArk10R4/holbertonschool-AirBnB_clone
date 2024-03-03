#!/usr/bin/python3

"""Unittest for Place"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    place = None

    def setUp(self) -> None:
        self.place = Place()

    def tearDown(self) -> None:
        del self.place

    def test_create_place(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
        del place

    def test_city_id(self):
        self.assertEqual(self.place.city_id, "")
        self.place.city_id = "123"
        self.assertEqual(self.place.city_id, "123")

    def test_user_id(self):
        self.assertEqual(self.place.user_id, "")
        self.place.user_id = "123"
        self.assertEqual(self.place.user_id, "123")

    def test_name(self):
        self.assertEqual(self.place.name, "")
        self.place.name = "San Francisco"
        self.assertEqual(self.place.name, "San Francisco")


if __name__ == "__main__":
    unittest.main()
