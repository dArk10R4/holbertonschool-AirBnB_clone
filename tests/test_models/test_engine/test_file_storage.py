#!/usr/bin/python3

"""Unittest for FileStorage"""

from models.engine.file_storage import FileStorage
import unittest
from models.base_model import BaseModel


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
        self.file_storage.save()
        with open("file.json", "r") as file:
            self.assertNotEqual(file.read(), "")

    def test_reload(self):
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_reload_no_file(self):
        self.file_storage.save()
        self.file_storage.__class__.__file_path = "no_file.json"
        self.file_storage.reload()
        self.assertIsInstance(self.file_storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
