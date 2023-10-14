#!/usr/bin/env python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance
        with id, created_at, and updated_at attributes.

        If 'kwargs' is not empty, it populates the instance attributes
            from the dictionary representation.

        :param kwargs:
            Dictionary containing attribute values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        """
        Update the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name,
                self.id,
                self.__dict__
        )
