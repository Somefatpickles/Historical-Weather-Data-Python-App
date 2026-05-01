from weather_class import WeatherData
from weather_db import WeatherDB
from tabulate import tabulate

def main():

    # Hard-code desired location and dates into variables (Bentonville, AR: February 11, 2021 - February 11, 2026)

    latitude = 36.379612
    longitude = -94.224240
    month = 2
    day = 11
    start_year = 2026

    # C3 - Create WeatherData class instance

    weather = WeatherData(latitude=latitude, longitude=longitude, month=month, day=day, start_year=start_year)
    weather.fetch_weather_data()

    weather.set_weather_data()

    # Calculate and store values for each NoneType variable in weather class instance

    weather.avg_temp = weather.calculate_temp("temp", "avg")
    weather.min_temp = weather.calculate_temp("temp", "min")
    weather.max_temp = weather.calculate_temp("temp", "max")

    weather.avg_wind_speed = weather.calculate_wind("wind", "avg")
    weather.min_wind_speed = weather.calculate_wind("wind", "min")
    weather.max_wind_speed = weather.calculate_wind("wind", "max")

    weather.sum_precip = weather.calculate_precip("precip", "sum")
    weather.min_precip = weather.calculate_precip("precip", "min")
    weather.max_precip = weather.calculate_precip("precip", "max")

    # C5 - Add data to the database table

    db_url = 'sqlite:///weather.db'
    db = WeatherDB(db_url)
    db.add_weather(weather)

    # C6 - Query the database

    query_results = db.query_db()

    if query_results:

        # Format query table with appropriate headers

        headers = [
            'ID', 'Latitude', 'Longitude', 'Year', 'Month', 'Day', 'Temp (F)', 'Wind Speed (mph)',
            'Precip (in)', 'Avg Temp (5-year)','Min Temp (5-year)', 'Max Temp (5-year)',
            'Avg Wind Speed (5-year)', 'Min Wind Speed (5-year)', 'Max Wind Speed (5-year)',
            'Total Precipitation (5-year)', 'Minimum Precipitation (5-year)', 'Maximum Precipitation (5-year)'
        ]
        table_data = []
        print("Querying database...")
        for record in query_results:
            row = [
                record.id,
                record.latitude,
                record.longitude,
                record.years,
                record.month,
                record.day,
                record.temps,
                record.wind_speeds,
                record.precips,
                f"{record.avg_temp:.2f}",
                f"{record.min_temp:.2f}",
                f"{record.max_temp:.2f}",
                f"{record.avg_wind_speed:.2f}",
                f"{record.min_wind_speed:.2f}",
                f"{record.max_wind_speed:.2f}",
                f"{record.precipitation_sum:.2f}",
                f"{record.min_precipitation:.2f}",
                f"{record.max_precipitation:.2f}"
            ]
            table_data.append(row)

        print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == '__main__':
    main()