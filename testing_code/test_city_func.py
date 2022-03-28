import unittest
from city_func import city_country


class TestCountryCity(unittest.TestCase):
    def test_city_country(self):
        all_in_one = city_country('prague', 'czech republic')
        self.assertEqual(all_in_one, 'Prague Czech Republic')

    def test_city_country_population(self):
        all_in_one = city_country('prague', 'czech republic 10000000')
        self.assertEqual(all_in_one, 'Prague Czech Republic 10000000')
