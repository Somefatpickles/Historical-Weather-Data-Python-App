# Historical Weather Data Python Application

## Overview

This project is a Python-based weather application designed to retrieve and analyze historical weather data through API integration and user interaction. The application allows users to query weather information for specific locations and dates, demonstrating practical use of external data services, application logic, and data handling in Python.

The project was developed to apply software development principles and strengthen experience working with APIs, structured data, and interactive Python applications.

---

## Project Objective

The primary goal of this project was to build a functional weather data application capable of:

* Retrieving historical weather information
* Processing and displaying weather data
* Handling user input dynamically
* Integrating external APIs into a Python workflow

This project emphasizes real-world application development concepts commonly used in data and software engineering workflows.

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

---

## Features

* Historical weather data retrieval
* API integration and data requests
* User-driven location/date queries
* Structured data parsing and display
* Error handling and input validation
* Command-line application interface

---

## Technologies Used

* Python
* REST API integration
* JSON data handling
* HTTP requests
* Command-line interface (CLI)

---

## Application Workflow

1. User enters location and/or date information
2. Application sends a request to a weather API
3. Returned weather data is processed and parsed
4. Results are displayed in a readable format for the user

This workflow demonstrates practical interaction between Python applications and external web services.

---

## Skills Demonstrated

This project highlights experience with:

* Python application development
* API consumption and integration
* JSON parsing and structured data handling
* User input validation
* Error handling and debugging
* Modular application logic

---

## How to Run

1. Clone the repository:

```bash id="mjlwmn"
git clone https://github.com/Somefatpickles/Historical-Weather-Data-Python-App.git
```

2. Navigate to the project directory:

```bash id="fgghs0"
cd Historical-Weather-Data-Python-App
```

3. Install dependencies (if applicable):

```bash id="v1qg7q"
pip install -r requirements.txt
```

4. Run the application:

```bash id="m0rdbt"
python main.py
```

---

## Example Use Case

A user can request historical weather conditions for a specific city and date, allowing the application to retrieve and display relevant weather metrics such as:

* Temperature
* Humidity
* Wind conditions
* Precipitation data

Weather APIs are commonly used in analytics, forecasting, logistics, and operational planning applications. ([openweathermap.org](https://openweathermap.org/api?utm_source=chatgpt.com))

---

## Adjusting Location and Date Parameters

The following variables within the `main.py` script may be modified for weather analysis at any given location or time 
at which the open-meteo API contains weather data:

- `latitude`
- `longitude`
- `month`
- `day`
- `start_year`

By default, the `WeatherData` class in the `weather_class.py` script will retrieve weather data for the previous five
years. The number of years can be adjusted by changing the value assigned to the `self.num_years` variable.

## Project Structure

```id="a4i6e0"
Historical-Weather-Data-Python-App/
│
├── main.py
├── weather.db
├── weather_class.py
├── weather_db.py
├── test.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Add graphical user interface (GUI) support
* Implement data visualization and charting
* Support forecast and real-time weather data
* Store query history in a database
* Expand error handling and user customization options

---

## Conclusion

This project demonstrates practical Python software development through the creation of an interactive weather data application. It highlights API integration, external data handling, and user-focused application design while reinforcing foundational software engineering concepts.
