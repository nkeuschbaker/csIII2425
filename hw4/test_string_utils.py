import unittest

from string_utils import reverse_string, capitalize_string, is_capitalized
class TestStringUtils(unittest.TestCase):
  def test_reverse_string(self):
    result = "olleh"
    self.assertEqual(result, reverse_string("hello"))
  def test_capitalize_string(s):
    result = "Hello"
    s.assertEqual(result, capitalize_string("hello"))
  def test_is_capitalized(s):
    s.assertTrue(is_capitalized("Hello"))
if __name__ == '__main__':
  unittest.main()