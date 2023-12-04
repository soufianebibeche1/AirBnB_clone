#!/usr/bin/python3
"""
Unittests for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_creation(self):
        """
        Test creating an instance of BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """
        Test attributes of the BaseModel class.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        """
        Test the __str__ method of BaseModel.
        """
        my_model = BaseModel()
        string_representation = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string_representation)

    def test_save_method(self):
        """
        Test the save method of BaseModel.
        """
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel.
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()

        self.assertTrue(isinstance(my_model_json, dict))
        self.assertTrue('__class__' in my_model_json)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertTrue('created_at' in my_model_json)
        self.assertTrue('updated_at' in my_model_json)
        self.assertTrue('id' in my_model_json)

    def test_to_dict_isoformat(self):
        """
        Test the isoformat conversion in to_dict method.
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()

        created_at_isoformat = datetime.strptime(
            my_model_json['created_at'], "%Y-%m-%dT%H:%M:%S.%f").isoformat()
        updated_at_isoformat = datetime.strptime(
            my_model_json['updated_at'], "%Y-%m-%dT%H:%M:%S.%f").isoformat()

        self.assertEqual(created_at_isoformat, my_model.created_at.isoformat())
        self.assertEqual(updated_at_isoformat, my_model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
