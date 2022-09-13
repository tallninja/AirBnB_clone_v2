#!/usr/bin/python3
"""
Unit tests for tha database storage.
"""
import unittest
import pycodestyle
from models.engine.db_storage import DBStorage


class test_db_storage(unittest.TestCase):
    """class to test the db_storage method"""

    def test_doc(self):
        """
        Check all the doc of the Amenity Class
        """
        # module documentation
        module = len(DBStorage.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(DBStorage.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(DBStorage.new.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(DBStorage.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(DBStorage.delete.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(DBStorage.reload.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(DBStorage.all.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(DBStorage.__init__.__doc__)
        self.assertGreater(module_class, 0)
