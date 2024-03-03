#!/usr/bin/python3
"""Unittest for state"""

from models.state import State
import unittest

class TestState(unittest.TestCase):
    state = None
    def setUp(self) -> None:
        self.state = State()
    
    def tearDown(self) -> None:
        del self.state

    def test_create_state(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)
        del state
    def test_name(self):
        self.assertEqual(self.state.name, "")
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")
if __name__ == "__main__":
    unittest.main()
