import unittest
from new import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('jane', 'mair')
        self.assertEqual(formatted_name, 'Jane Mair')

unittest.main()