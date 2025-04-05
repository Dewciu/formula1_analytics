import pandas as pd
from formula1_analytics.logger import get_logger
from formula1_analytics.common.data_processor import DataProcessor
from formula1_analytics.common.f1_data import F1Data
from formula1_analytics.config.config import WEATHER_FILENAME

LOGGER = get_logger(__name__)

class WeatherColumns:
    TIME = "Time"
    AIR_TEMP = "AirTemp"
    HUMIDITY = "Humidity"
    PRESSURE = "Pressure"
    RAINFALL = "Rainfall"
    TRACK_TEMP = "TrackTemp"
    WIND_DIRECTION = "WindDirection"
    WIND_SPEED = "WindSpeed"
    ROUND = "Round Number"
    YEAR = "Year"

    @staticmethod
    def get_types() -> dict[str, str]:
        return {
            WeatherColumns.AIR_TEMP: "Float64",
            WeatherColumns.HUMIDITY: "Float64",
            WeatherColumns.PRESSURE: "Float64",
            WeatherColumns.RAINFALL: "boolean",
            WeatherColumns.TRACK_TEMP: "Float64",
            WeatherColumns.WIND_DIRECTION: "Int64",
            WeatherColumns.WIND_SPEED: "Float64",
            WeatherColumns.ROUND: "Int64",
            WeatherColumns.YEAR: "Int64",
        }

class Weather(F1Data):
    def __init__(self) -> None:
        super().__init__(WEATHER_FILENAME, None)
        DataProcessor().convert_types(self._data, WeatherColumns.get_types())

    def get_time(self) -> pd.Series:
        return self._data[WeatherColumns.TIME]

    def get_air_temp(self) -> pd.Series:
        return self._data[WeatherColumns.AIR_TEMP]

    def get_humidity(self) -> pd.Series:
        return self._data[WeatherColumns.HUMIDITY]

    def get_pressure(self) -> pd.Series:
        return self._data[WeatherColumns.PRESSURE]

    def get_rainfall(self) -> pd.Series:
        return self._data[WeatherColumns.RAINFALL]

    def get_track_temp(self) -> pd.Series:
        return self._data[WeatherColumns.TRACK_TEMP]

    def get_wind_direction(self) -> pd.Series:
        return self._data[WeatherColumns.WIND_DIRECTION]

    def get_wind_speed(self) -> pd.Series:
        return self._data[WeatherColumns.WIND_SPEED]
    
    def get_round(self) -> pd.Series:
        return self._data[WeatherColumns.ROUND]

    def get_year(self) -> pd.Series:
        return self._data[WeatherColumns.YEAR]