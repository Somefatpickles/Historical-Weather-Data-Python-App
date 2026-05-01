# Weather Prediction Python Application - WGU Course D493: Scripting And Programming - Applications

## Overview

This is my project submission for D493, Scripting And Programming - Applications.

In pursuit of meeting the course's requirements, this application was designed to access and store open-source weather
data, showcasing the use of API calls, SQLAlchemy, and GitLab's git functionality using PyCharm, an IDE for coding
in Python.

## Purpose

This application is intended to assist stakeholders with the task of determining a specific location's viability for 
hosting an outdoor event based on historical weather data. This data is sourced via requests from the 
`https://open-meteo.com` API.  By gathering aggregate data related to the following variables, event planners are
positioned to pinpoint excellent candidate dates on which outdoor events may be hosted at any given location:
- 5-year average, minimum, and maximum **temperature**
- 5-year average, minimum, and maximum **wind speed**
- 5-year sum, minimum, and maximum **precipitation**

These data are stored in a locally run SQLite database, allowing queries to be made against it for easy retrieval.

Below are relevant details on each of the documents contained within.

### requirements.txt

This file contains all the dependencies needed for this application to run properly.

### main.py

This file is used to run the application.

### weather_class.py

This file contains the WeatherData class and API request functions.

### weather_db.py

This file contains the database class and function to add data to the database.

### test.py

This file contains three tests written using the `unittest` framework to ensure the script and API are running properly.
To test this application via terminal, navigate to this project's directory and run:

```bash
> python -m unittest
```

## Running The Application

Ensure all needed dependencies are installed as listed within the `requirements.txt` document. 

**To run this application, simply run the `main.py` script in a Python Console.**

If the application runs as intended, the python console will populate with a JSON object for each year.  The application
will populate a table with one row of data before closing.

### Adjusting Location and Date Parameters

The following variables within the `main.py` script may be modified for weather analysis at any given location or time 
at which the open-meteo API contains weather data:

- `latitude`
- `longitude`
- `month`
- `day`
- `start_year`

By default, the `WeatherData` class in the `weather_class.py` script will retrieve weather data for the previous five
years. The number of years can be adjusted by changing the value assigned to the `self.num_years` variable.