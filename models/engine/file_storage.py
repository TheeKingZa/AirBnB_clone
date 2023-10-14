#!/usr/bin/env python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add an object to the __objects dictionary.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize the __objects dictionary and save it to a JSON file.
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserialize the JSON file and populate the __objects dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj_dict = {}
                    for k, v in value.items():
                        if k not in ['created_at', 'updated_at']:
                            obj_dict[k] = v
                        else:
                            obj_dict[k] = datetime.fromisoformat(v)
                    # Create an instance of the object from the dictionary.
                    cls = globals()[class_name]
                    obj = cls(**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
