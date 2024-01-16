#!/usr/bin/python3
import unittest
# from models.rectangle import Rectangle
# from models.square import Square
from models.base import Base


class test_base_class(unittest.TestCase):
    def test_base(self):
        none_id = Base(0)
        self.assertEqual(none_id, 1)
        
if __name__ == 'main':
    unittest.main()
