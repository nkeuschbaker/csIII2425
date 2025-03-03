import unittest
class TestStringUtils(unittest.testcase):
  def test_reverse_string(self):
    result = "olleh"
    self.assertEqual(result, reverse_string("hello"))
