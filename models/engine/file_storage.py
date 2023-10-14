#!/usr/bin/env python3
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects (if the file exists)."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
