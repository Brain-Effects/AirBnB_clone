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
        self.model1 = BaseModel()
        self.model2 = BaseModel(**{
            'id': '123',
            'created_at': '2020-06-30T15:09:32.095238',
            'updated_at': '2020-06-30T15:09:32.095238'})

    def test_id(self):
        """
        Test the id attribute
        """
        self.assertEqual(type(self.model1.id), str)
        self.assertEqual(self.model2.id, '123')

    def test_created_at(self):
        """
        Test the created_at attribute
        """
        self.assertEqual(type(self.model1.created_at), datetime)
        self.assertEqual(self.model2.created_at, datetime.strptime(
            '2020-06-30T15:09:32.095238',
            "%Y-%m-%dT%H:%M:%S.%f"))

    def test_updated_at(self):
        """
        Test the updated_at attribute
        """
        self.assertEqual(type(self.model1.updated_at), datetime)
        self.assertEqual(self.model2.updated_at, datetime.strptime(
            '2020-06-30T15:09:32.095238',
            "%Y-%m-%dT%H:%M:%S.%f"))

    def test_save(self):
        """
        Test the save method
        """
        old_updated_at = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        model_dict = self.model1.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)


if __name__ == '__main__':
    unittest.main()
