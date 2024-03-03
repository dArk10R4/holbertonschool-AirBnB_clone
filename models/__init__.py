#!/usr/bin/python3


'''doc'''


from models.base_model import BaseModel
from models.user import User

from models.engine.file_storage import FileStorage
from models.engine.file_storage import classes
storage = FileStorage()
storage.reload()

