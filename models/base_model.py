#!/usr/bin/python3
"""
Module for BaseModel class.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class definition.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of BaseModel.
        Args:
            *args: Unused
            **kwargs: Dictionary of attributes to initialize the instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of BaseModel instance.
        Returns:
            Formatted string [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        A key __class__ is added to this dictionary with the class name of the object.
        created_at and updated_at are converted to string object in ISO format.
        Returns:
            Dictionary representation of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
