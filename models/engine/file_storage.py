#!/usr/bin/python3
'''doc'''
import json
import os


class FileStorage:
    '''doc'''

    __file_path = 'file.json'
    __objects={}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        new_items = {}
        for key, value in FileStorage.__objects.items():
            new_items[key] = value.to_dict()
            
        with open(FileStorage.__file_path, 'w') as write:
            json.dump(new_items, write)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF") as f:
                FileStorage.__objects = json.load(f)
