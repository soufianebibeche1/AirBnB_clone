#!/usr/bin/python3
#models/__init__.py
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
