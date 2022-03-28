import unittest
from full_name_func import full_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = full_name('artom', 'cernopascenko')
        self.assertEqual(formatted_name, 'Artom Cernopascenko')

    def test_first_last_middle_name(self):
        formatted_name = full_name('margarita', 'pastukhova', 'michailovna')
        self.assertEqual(formatted_name, 'Margarita Pastukhova Michailovna')



