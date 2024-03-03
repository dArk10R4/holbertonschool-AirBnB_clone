#!/usr/bin/python3

"""Unittest for city"""

from models.city import City
import unittest

class TestCity(unittest.TestCase):
    city = None
    def setUp(self) -> None:
        self.city = City()
    
    def tearDown(self) -> None:
        del self.city

    def test_create_city(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)
        del city
    def test_name(self):
        self.assertEqual(self.city.name, "")
        self.city.name = "San Francisco"
        self.assertEqual(self.city.name, "San Francisco")
    def test_state_id(self):
        self.assertEqual(self.city.state_id, "")
        self.city.state_id = "123"
        self.assertEqual(self.city.state_id, "123")