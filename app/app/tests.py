"""
Sample Tests
"""

from django.test import SimpleTestCase
from .calc import add, subtract

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = add(2, 6)
        self.assertEqual(res, 8)
    
    
    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = subtract(2, 6)
        self.assertEqual(res, -4)