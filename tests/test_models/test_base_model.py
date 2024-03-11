#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test the functionality of the BaseModel class
    """

    def setUp(self):
        """
        Set up the tests
        """
        self.model = BaseModel()

    def test_id(self):
        """
        Test the id attribute
        """
        self.assertEqual(type(self.model.id), str)

    def test_created_at(self):
        """
        Test the created_at attribute
        """
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at(self):
        """
        Test the updated_at attribute
        """
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_save(self):
        """
        Test the save method
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)

if __name__ == '__main__':
    unittest.main()
