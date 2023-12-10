#!/usr/bin/python3
# models/base_model.py
"""Define BaseModel class"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """class BaseModel"""

    def __init__(self, *arg, **kwargs):
        """
        Initialize a new instance of the class.
        """
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "created_at" or j == "updated_at":
                    self.__dict__[j] = datetime.strptime(k, tformat)
                else:
                    self.__dict__[j] = k
        else:
            pass
            storage.new(self)

    def save(self):
        """
        update updated_at with the current datetime and saves the instance
        to the JSON file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This function takes an object and returns a
        dictionary representation of that object
        """
        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def __str__(self):
        """
        The function returns a string that contains the class name,
        the id of the object, and the contents of the object's
        dictionary
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
