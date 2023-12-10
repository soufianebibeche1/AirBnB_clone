#!/usr/bin/python3
"""Module for testing save and reload methods of BaseModel class."""
import unittest
from models import storage
from models.base_model import BaseModel


class TestSaveReloadBaseModel(unittest.TestCase):
    """Test cases for saving and reloading BaseModel instances."""

    def test_save_reload_base_model(self):
        """Test saving and reloading BaseModel instance."""
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

if __name__ == '__main__':
    unittest.main()
