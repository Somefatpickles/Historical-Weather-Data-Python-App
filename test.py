from unittest import TestCase
from weather_class import WeatherData
import itertools

class TestWeatherData(TestCase):
    @classmethod
    def setUpClass(cls):
        print('Retrieving API data...')
        cls.weather_data = WeatherData(latitude=36.379612,
                                       longitude=-94.224240,
                                       month=2,
                                       day=11,
                                       start_year=2026)
        cls.weather_data.fetch_weather_data()
        cls.weather_data.set_weather_data()
        print('API data retrieved.')

    def test_1(self):
        print('\nTest 1 initializing...testing to ensure list attributes are of intended length.')
        # Test to ensure list attributes are of intended length
        self.assertEqual(len(list(itertools.chain.from_iterable(self.weather_data.temp))), self.weather_data.num_years, f"temp list should be of length {self.weather_data.num_years}.")
        self.assertEqual(len(list(itertools.chain.from_iterable(self.weather_data.wind_speed))), self.weather_data.num_years, f"wind_speed list should be of length {self.weather_data.num_years}.")
        self.assertEqual(len(list(itertools.chain.from_iterable(self.weather_data.precip))), self.weather_data.num_years, f"precip list should be of length {self.weather_data.num_years}.")
        print('\nTest 1 passed.')

    def test_2(self):
        print('\nTest 2 initializing...testing to ensure sum_precip variable is assigned a value.')
        # Test on sum_precip variable to ensure it is assigned a value and is no longer of type NoneType
        self.weather_data.sum_precip = self.weather_data.calculate_precip("precip", "sum")
        self.assertIsNotNone(self.weather_data.sum_precip, "sum_precip should not be of type NoneType")
        print('\nTest 2 passed.')

    def test_3(self):
        print('\nTest 3 initializing...testing to ensure yearly_weather instance receives intended number of iterations.')
        # Test to ensure yearly_weather instance receives intended number of iterations
        self.assertIsNotNone(self.weather_data.yearly_weather, "yearly_weather should not be of type NoneType")
        self.assertEqual(len(self.weather_data.yearly_weather), self.weather_data.num_years, f"yearly_weather list should be of length {self.weather_data.num_years}.")
        print('\nTest 3 passed.')
