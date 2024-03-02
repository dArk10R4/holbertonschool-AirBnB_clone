#!/usr/bin/python3
'''doc'''

from datetime import datetime
import uuid
import models


class BaseModel:
    '''Base class'''
    
    def __init__(self, *args, **kwargs):
        '''Initializer'''
        
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''String of BaseModel'''
        
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''update updated item'''
        
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Dictionary represendation'''
        
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
