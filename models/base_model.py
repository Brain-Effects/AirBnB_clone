#!/usr/bin/python4
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """
        Initialize the BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models.engine.file_storage import FileStorage
            storage = FileStorage()
            storage.new(self)

    def __str__(self):
        """
        Return the string representation of the BaseModel
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict_)

    def save(self):
        """
        Update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the
        instance's __dict__
        """
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
