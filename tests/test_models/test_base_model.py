#!/usr/bin/python3

"""Unittest for BaseModel"""

from models.base_model import BaseModel
import unittest
import datetime
import time

class TestBaseModel(unittest.TestCase):
    base = None

    def setUp(self) -> None:
        self.base = BaseModel()

    def tearDown(self) -> None:
        del self.base

    def test_create_base(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)
        del base

    def test_id(self):
        self.assertNotEqual(self.base.id, "")
        self.base.id = "123"
        self.assertEqual(self.base.id, "123")

    def test_created_at(self):
        self.assertIsInstance(self.base.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base.updated_at, datetime.datetime, "Not a datetime object")

    def test_str(self):
        self.assertIsInstance(self.base.__str__(), str)
        self.assertRegex(self.base.__str__(), "^\[BaseModel\] (.*) {(.*)}$")

    def test_save(self):
        time.sleep(0.3)
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict(self):
        self.assertIsInstance(self.base.to_dict(), dict)
        self.assertIsInstance(self.base.to_dict()["created_at"], str)
        self.assertIsInstance(self.base.to_dict()["updated_at"], str)
        self.assertIsInstance(self.base.to_dict()["__class__"], str)