#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest, os, pep8


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "Filestorage")
    def test_save_Amenity(self):
        """  Test save function for Amenity class  """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_pep8_Amenity(self):
        """"  Test pep8 for Amenity class  """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error")

    def test_docstring_Amenity(self):
        """  Test docstring for Amenity class  """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """  Test for Amenity class  """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_types_Amenity(self):
        """  Test attribute type for Amenity class """
        self.assertEqual(type(self.amenity.name), str)
    
if __name__ == '__main__':
    unittest.main()