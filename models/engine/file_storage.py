# models/engine/file_storage.py
import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {
            key: obj.to_dict() for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key]["created_at"] = datetime.strptime(
                        value["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    obj_dict[key]["updated_at"] = datetime.strptime(
                        value["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    cls = BaseModel if class_name == "BaseModel" else None
                    instance = cls(**obj_dict[key])
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
