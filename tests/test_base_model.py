import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_str(self):
        obj = BaseModel()
        obj.id = "test_id"
        obj_dict = obj.__dict__
        expected_str = "[BaseModel] (test_id) {}".format(obj_dict)
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj.id = "test_id"
        obj.created_at = datetime(2023, 10, 10, 12, 0, 0)
        obj_dict = obj.to_dict()
        expected_dict = {
            'id': 'test_id',
            '__class__': 'BaseModel',
            'created_at': '2023-10-10T12:00:00',
            'updated_at': obj.updated_at.isoformat()
        }
        self.assertEqual(obj_dict, expected_dict)

if __name__ == "__main__":
    unittest.main()
