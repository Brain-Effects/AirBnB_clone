#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the functionality of the FileStorage class
    """

    def setUp(self):
        """
        Set up the tests
        """
        self.storage = FileStorage()
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """
        Tear down the tests
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Test the all method
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """
        Test the new method
        """
        self.storage.new(self.model1)
        self.assertIn("BaseModel." + self.model1.id, self.storage.all())

    def test_save_and_reload(self):
        """
        Test the save and reload methods
        """
        self.model1.save()
        self.assertTrue(os.path.exists("file.json"))
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn("BaseModel." + self.model1.id, objects)
        self.assertEqual(objects[
            "BaseModel." + self.model1.id].id, self.model1.id)


if __name__ == '__main__':
    unittest.main()
