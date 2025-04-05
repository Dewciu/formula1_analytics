import pandas as pd

from formula1_analytics.drivers.drivers import Drivers, ResultsColumns
from formula1_analytics.races.races import Races, RacesColumns
from formula1_analytics.results.results import Results
from formula1_analytics.weather.weather import LOGGER, Weather, WeatherColumns

class DriverWeatherPerf:
    _data: pd.DataFrame

    def __init__(self) -> None:
        LOGGER.debug("Initializing DriverWeatherPerf class")
        self._drivers = Drivers().get_driver_fullnames()
        self._results = Results().get_selected_columns(
            ResultsColumns.DRIVER_ID,
            ResultsColumns.POSITION,
            ResultsColumns.RACE_ID,
            ResultsColumns.POINTS,
        )
        self._race_weather = pd.merge(
            Races().get_selected_columns(
                RacesColumns.YEAR,
                RacesColumns.ROUND,
            ).reset_index(),
            Weather().get_selected_columns(
                WeatherColumns.ROUND, 
                WeatherColumns.YEAR,
                WeatherColumns.RAINFALL,
                WeatherColumns.TRACK_TEMP,
                WeatherColumns.AIR_TEMP,
                WeatherColumns.HUMIDITY,
                WeatherColumns.PRESSURE,
                WeatherColumns.WIND_SPEED,
            ),
            left_on=[RacesColumns.ROUND, RacesColumns.YEAR],
            right_on=[WeatherColumns.ROUND, WeatherColumns.YEAR]
        ).drop(columns=[WeatherColumns.ROUND, WeatherColumns.YEAR])

        LOGGER.debug(f"Got drivers: \n {self._drivers}")
        LOGGER.debug(f"Got results: \n {self._results}")
        LOGGER.debug(f"Got race_weather: \n {self._race_weather}")




    def get_data(self, season_year: int, driver: str, weather: str) -> pd.DataFrame:
        ...

    

    