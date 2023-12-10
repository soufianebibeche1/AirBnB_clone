#!/usr/bin/python3
"""Module for BaseModel class."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class for AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in [
                        "created_at", "updated_at"
                    ]:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'
                        )
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Saves the current instance to the storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
