#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_base_model(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_str(self):
        obj = BaseModel()
        obj_str = str(obj)
        self.assertTrue(obj.__class__.__name__ in obj_str)
        self.assertTrue(obj.id in obj_str)
        self.assertTrue(obj.__dict__.__str__() in obj_str)


    def test_init_with_kwargs(self):
        data = {
            'id': '1234-5678',
            'created_at': '2023-01-01T12:00:00',
            'updated_at': '2023-01-02T08:30:00',
            'name': 'John',
            'age': 30
        }
        obj = BaseModel(**data)
        self.assertIsInstance(obj, BaseModel)
        self.assertEqual(obj.id, '1234-5678')
        self.assertEqual(obj.created_at.year, 2023)
        self.assertEqual(obj.created_at.month, 1)
        self.assertEqual(obj.updated_at.hour, 8)
        self.assertEqual(obj.name, 'John')
        self.assertEqual(obj.age, 30)

if __name__ == '__main__':
    unittest.main()
