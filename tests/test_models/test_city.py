#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
import os
import pep8


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_attribute_types_City(self):
        """ test attribute type """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_City(self):
        """ test save function city """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_pep8_City(self):
        """"  Test pep8 for City class  """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

if __name__ == "__main__":
    unittest.main()
