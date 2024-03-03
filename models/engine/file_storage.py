#!/usr/bin/python3
'''doc'''
import json
import os
from models.base_model import BaseModel


class FileStorage:
    '''doc'''

    __file_path = 'file.json'
    __objects={}

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        FileStorage.__objects = value

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        FileStorage.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        new_items = {}
        for key, value in FileStorage.__objects.items():
            new_items[key] = value.to_dict()
            
        with open(FileStorage.__file_path, 'w') as write:
            json.dump(new_items, write)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF") as f:
                objs = json.load(f)
            for key in objs:
                class_name = key.split(".")[0]
                FileStorage.__objects[key] = eval(f"{class_name}(**objs[key])")
