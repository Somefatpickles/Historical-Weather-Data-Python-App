from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from itertools import chain

Base = declarative_base()

# C4 - Create a class for database table

class Weather_Table(Base):
    __tablename__ = 'weather_data'

    # Create columns for table

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    years = Column(String, nullable=False)

    temps = Column(String)
    wind_speeds = Column(String)
    precips = Column(String)

    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    precipitation_sum = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)

# C5 - Create class to populate weather_data table with data

class WeatherDB:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.drop_all(self.engine) # Drop table if exists
        Base.metadata.create_all(self.engine) # Create table

        self.Session = sessionmaker(bind=self.engine)

    def add_weather(self, weather_class):
        """
        DOCSTRING
        Add data from a WeatherData class instance to the weather_data database.
        :param weather_class: The class instance to be added.
        """
        session = self.Session()
        # for i in range(len(weather_class.years)):
        weather = Weather_Table(
            latitude = weather_class.latitude,
            longitude = weather_class.longitude,
            years = ", ".join(map(str, chain.from_iterable(weather_class.current_year_list))),
            month = weather_class.month,
            day = weather_class.day,
            temps = ", ".join(map(str, chain.from_iterable(weather_class.temp))),
            wind_speeds = ", ".join(map(str, chain.from_iterable(weather_class.wind_speed))),
            precips = ", ".join(map(str, chain.from_iterable(weather_class.precip))),
            avg_temp = weather_class.avg_temp,
            min_temp = weather_class.min_temp,
            max_temp = weather_class.max_temp,
            avg_wind_speed = weather_class.avg_wind_speed,
            min_wind_speed = weather_class.min_wind_speed,
            max_wind_speed = weather_class.max_wind_speed,
            precipitation_sum = weather_class.sum_precip,
            min_precipitation = weather_class.min_precip,
            max_precipitation = weather_class.max_precip
        )
        session.add(weather)
        session.commit()
        print(f"Successfully added weather data to database!")
        session.close()

# C6 - Write method to query stored data

    def query_db(self):
        """
        DOCSTRING
        Query all weather data from the database object.
        :return: Returns query results.
        """
        session = self.Session()
        try:
            query = session.query(Weather_Table).all()
            return query
        finally:
            session.close()