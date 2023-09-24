import unittest
from num_to_hex_conversion import num_to_hex


class MyTestCase(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            num_to_hex(3.14)
            num_to_hex('hello')


if __name__ == '__main__':
    unittest.main()