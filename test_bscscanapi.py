# test_bscscanapi.py
"""
Tests for BscscanApi module.
"""

import unittest
from bscscanapi import BscscanApi

class TestBscscanApi(unittest.TestCase):
    """Test cases for BscscanApi class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BscscanApi()
        self.assertIsInstance(instance, BscscanApi)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BscscanApi()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
