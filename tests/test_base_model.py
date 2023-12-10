#!/usr/bin/python3
"""Module for testing BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_base_model_creation(self):
        """Test creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_base_model_str(self):
        """Test the __str__ method of the BaseModel class."""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        expected_str = "[BaseModel] ({}) {'name': 'Test Model', 'my_number': 42, 'id': '{}', 'created_at': '{}', 'updated_at': '{}'}"\
            .format(my_model.id, my_model.created_at, my_model.updated_at)
        self.assertEqual(str(my_model), expected_str)

    def test_base_model_save(self):
        """Test the save method of the BaseModel class."""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        obj_dict = my_model.to_dict()
        self.assertEqual(obj_dict['id'], my_model.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], my_model.updated_at.isoformat())
        self.assertEqual(obj_dict['name'], 'Test Model')
        self.assertEqual(obj_dict['my_number'], 42)


if __name__ == '__main__':
    unittest.main()
