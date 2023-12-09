#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """
    def test_init(self):
        """
        Test the initialization of the BaseModel instance.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        my_model = BaseModel()
        str_representation = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), str_representation)

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertTrue('__class__' in my_model_json)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertTrue('created_at' in my_model_json)
        self.assertTrue('updated_at' in my_model_json)
        self.assertTrue('id' in my_model_json)
        self.assertEqual(my_model_json['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(my_model_json['updated_at'],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model_json['id'], my_model.id)

if __name__ == '__main__':
    unittest.main()
