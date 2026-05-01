import requests

# C1 - Create class

class WeatherData:
    def __init__(self, latitude, longitude, day, month, start_year):
        self.latitude = latitude
        self.longitude = longitude
        self.day = day
        self.month = month

        self.start_year = start_year
        self.current_year_list = []
        self.num_years = 5

        self.temp = []
        self.avg_temp = None
        self.min_temp = None
        self.max_temp = None

        self.wind_speed = []
        self.avg_wind_speed = None
        self.min_wind_speed = None
        self.max_wind_speed = None

        self.precip = []
        self.sum_precip = None
        self.min_precip = None
        self.max_precip = None

        self.yearly_weather = []

# C2 - Create methods for API requests

    def fetch_weather_data(self):
        """
        DOCSTRING
        Retrieve weather data from the Open Meteo API based on specific params.
        :return: A list containing daily weather data as dictionaries
        """
        for i in range(self.num_years):
            current_year = self.start_year - i
            url = (f"https://archive-api.open-meteo.com/v1/archive?"
                   f"latitude={self.latitude}&longitude={self.longitude}&"
                   f"start_date={current_year}-{self.month:02d}-{self.day:02d}&"
                   f"end_date={current_year}-{self.month:02d}-{self.day:02d}&"
                   f"daily=temperature_2m_mean,wind_speed_10m_max,precipitation_sum&"
                   f"temperature_unit=fahrenheit&wind_speed_unit=mph&"
                   f"precipitation_unit=inch&timezone=America/Chicago"
                   )
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                print(f"Data for {current_year}: {data}")

                daily_data = {
                    "year": current_year,
                    "temp": data.get("daily").get("temperature_2m_mean")[0],
                    "wind": data.get("daily").get("wind_speed_10m_max")[0],
                    "precip": data.get("daily").get("precipitation_sum")[0]
                }

                self.yearly_weather.append(daily_data)

        return self.yearly_weather

    def create_weather_list(self, daily_element):
        """
        DOCSTRING
        Create a list of values using a key-value pair from the daily_data dictionary.
        :param daily_element: The daily_data element from which another list of values is to be created.
        Acceptable values include: year, temp, wind, precip
        :return: Returns a list of values from the selected daily_data dictionary key
        """
        value_list = []
        for day in self.yearly_weather:
            value_list.append(day[daily_element])
        return value_list

    def calculate_temp(self, daily_element, operation):
        """
        DOCSTRING
        Calculate and return a temperature value based on desired operation.
        :param daily_element: The daily_data element from which another list of values is created.
        Acceptable values include: temp
        :param operation: The type of calculation to be performed.
        Accepted values include: avg, min, max
        :return: Returns a calculated temp value.
        """
        value_list = self.create_weather_list(daily_element)
        if operation == "avg":
            return sum(value_list) / len(value_list)
        elif operation == "min":
            return min(value_list)
        elif operation == "max":
            return max(value_list)
        else:
            return None

    def calculate_wind(self, daily_element, operation):
        """
        DOCSTRING
        Calculate and return a wind speed value based on desired operation.
        :param daily_element: The daily_data element from which another list of values is created.
        Acceptable values include: wind
        :param operation: The type of calculation to be performed.
        Accepted values include: avg, min, max
        :return: Returns a calculated temp value.
        """
        value_list = self.create_weather_list(daily_element)
        if operation == "avg":
            return sum(value_list) / len(value_list)
        elif operation == "min":
            return min(value_list)
        elif operation == "max":
            return max(value_list)
        else:
            return None

    def calculate_precip(self, daily_element, operation):
        """
        DOCSTRING
        Calculate and return a precipitation value based on desired operation.
        :param daily_element: The daily_data element from which another list of values is created.
        Acceptable values include: precip
        :param operation: The type of calculation to be performed.
        Accepted values include: sum, min, max
        :return: Returns a calculated temp value.
        """
        value_list = self.create_weather_list(daily_element)
        if operation == "sum":
            return sum(value_list)
        elif operation == "min":
            return min(value_list)
        elif operation == "max":
            return max(value_list)
        else:
            return None

    def set_weather_data(self):
        """
        DOCSTRING
        Retrieve year, temp, wind, and precip data points and append them to list variables.
        """
        current_year_list = self.create_weather_list("year")
        self.current_year_list.append(current_year_list)

        temp_list = self.create_weather_list("temp")
        self.temp.append(temp_list)

        wind_list = self.create_weather_list("wind")
        self.wind_speed.append(wind_list)

        precip_list = self.create_weather_list("precip")
        self.precip.append(precip_list)
