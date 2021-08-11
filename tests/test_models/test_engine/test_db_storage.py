#!/usr/bin/python
""" Unittest for DB_Storage """
from models.engine.file_storage import FileStorage
import unittest
import pep8
import os
from models.user import User


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    """ testing """
    @classmethod
    def setUpClass(cls):
        """Tests for User class"""
        cls.user = User()
        cls.user.first_name = "Pichu"
        cls.user.last_name = "Otegui"
        cls.user.email = "correo@hbtn.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """ delete User """
        del cls.user

    def test_pep8_DBStorage(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(pep.total_errors, 0, "pep8 errors")

    def test_all(self):
        """ Testing Object """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ Testing Object """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.name = "ElSergio"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

if __name__ == '__main__':
    unittest.main()
