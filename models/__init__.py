#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


""" Create an instance of the FileStorage class """
storage = FileStorage()
""" Reload data from storage (if any) """
storage.reload()
