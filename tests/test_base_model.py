#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

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

        '''
        def test_init_with_kwargs(self):
        # Create a dict with correct datetime values
        kwargs = {
        'name': 'My_First_Model',
        'my_number': 89,
        'id': 'b7202822-a97d-485d-94a9-4d88fd2b65a5',
        'created_at': datetime(2023, 10, 14, 22, 29, 44, 72717),
        'updated_at': datetime(2023, 10, 14, 22, 29, 44, 72832)
        }
        '''

    def test_init_with_kwargs(self):
        kwargs = {
                'id': 'b7202822-a97d-485d-94a9-4d88fd2b65a5',
                'created_at': datetime(2023, 10, 14, 22, 29, 44, 72717),
                'updated_at': datetime(2023, 10, 14, 22, 29, 44, 72832),
                'name': 'My_First_Model',
                'my_number': 89
        }
        obj = BaseModel(**kwargs)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertTrue(hasattr(obj, "name"))
        self.assertTrue(hasattr(obj, "my_number"))
        self.assertEqual(obj.id, 'b7202822-a97d-485d-94a9-4d88fd2b65a5')
        self.assertEqual(obj.created_at, datetime(2023, 10, 14, 22, 29, 44, 72717))
        self.assertEqual(obj.updated_at, datetime(2023, 10, 15, 0, 11, 13, 267082))
        self.assertEqual(obj.name, 'My_First_Model')
        self.assertEqual(obj.my_number, 89)


        # Create a BaseModel object with the provided kwargs
        obj = BaseModel(**kwargs)

        # Assertions about the object's attr
        self.assertEqual(obj.name, 'My_First_Model')
        self.assertEqual(obj.my_number, 89)
        self.assertEqual(obj.created_at.year, 2023)
        self.assertEqual(obj.updated_at, kwargs['updated_at'])


if __name__ == '__main__':
    unittest.main()
