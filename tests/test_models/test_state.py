#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest, os, pep8


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_State(self):
        """ test pep8 Review class"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_docstring_State(self):
        """test docstring State class"""
        self.assertIsNotNone(State.__doc__)

    def test_attribute_types_State(self):
        """test attributes type of State class"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_State(self):
        """test save function of State class"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

if __name__ == "__main__":
    unittest.main()