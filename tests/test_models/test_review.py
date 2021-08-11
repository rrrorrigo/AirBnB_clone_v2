#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import os
import pep8


class test_review(test_basemodel):
    """Review tests"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_pep8_Review(self):
        """check pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_Review(self):
        """ test save function in Review class"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

if __name__ == '__main__':
    unittest.main()
