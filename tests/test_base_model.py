#!/usr/bin/python3
import sys
import os
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        """Test the BaseModel class."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        # Check __str__ method
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

        # Check save method
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

        # Check to_dict method
        my_model_json = my_model.to_dict()
        expected_json = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            'name': 'My First Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(my_model_json, expected_json)

if __name__ == '__main__':
    unittest.main()
