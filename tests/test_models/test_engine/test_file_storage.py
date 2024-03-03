#!/usr/bin/python3

"""Unittest for FileStorage"""

from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    file_storage = None

    def setUp(self) -> None:
        self.file_storage = FileStorage()

    def tearDown(self) -> None:
        del self.file_storage

    def test_create_file_storage(self):
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)
        del file_storage

    def test_all(self):
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.assertIn("BaseModel.{}".format(base_model.id),
                      self.file_storage.all().keys())

    def test_save(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        with open(os.path.join(os.getcwd(), "file.json"), "r") as file:
            a = file.read()
            self.assertNotEqual(a, "")
            self.assertIn("{}.{}".format(base_model.__class__.__name__,
                                         base_model.id), a)

    def test_reload(self):
        self.file_storage.save()
        self.file_storage.objects = {}
        self.file_storage.reload()
        self.assertIsInstance(self.file_storage.all(), dict)
        self.assertNotEqual(len(self.file_storage._FileStorage__objects), 0)


    def test_reload_no_file(self):
        self.file_storage.save()
        self.file_storage.__class__.__file_path = "no_file.json"
        self.file_storage.reload()
        self.assertIsInstance(self.file_storage.all(), dict)

    def test___file_path(self):
        self.assertIsInstance(self.file_storage._FileStorage__file_path, str)

    def test___objects(self):
        self.assertIsInstance(self.file_storage._FileStorage__objects, dict)


if __name__ == "__main__":
    unittest.main()
