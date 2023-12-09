#!/usr/bin/python3
"""
Module for BaseModel class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class definition.
    """
    def __init__(self):
        """
        Initializes an instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of BaseModel instance.
        Returns:
            Formatted string [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns:
            Dictionary representation of the instance
        """
        dictionary = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at":
                dictionary[key] = value.isoformat()
            elif key == "updated_at":
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
