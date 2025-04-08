import pandas as pd
import numpy as np
from formula1_analytics.logger import get_logger
from formula1_analytics.drivers.drivers import Drivers, DriversColumns
from formula1_analytics.races.races import Races, RacesColumns
from formula1_analytics.results.results import Results, ResultsColumns
from formula1_analytics.weather.weather import Weather, WeatherColumns
from formula1_analytics.drivers.exceptions import (
    SeasonNotFoundException,
    DriverNotFoundException,
    InvalidSeasonException,
)

LOGGER = get_logger(__name__)

class WeatherType:
    """Types of weather conditions to analyze"""
    RAINFALL = "rainfall"
    TRACK_TEMP = "track_temp"
    AIR_TEMP = "air_temp"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"
    WIND_SPEED = "wind_speed"
    
    @staticmethod
    def get_all_types():
        return [
            WeatherType.RAINFALL,
            WeatherType.TRACK_TEMP,
            WeatherType.AIR_TEMP,
            WeatherType.HUMIDITY,
            WeatherType.PRESSURE,
            WeatherType.WIND_SPEED,
        ]
    
    @staticmethod
    def get_column_map():
        """Maps weather type to corresponding column in weather data"""
        return {
            WeatherType.RAINFALL: WeatherColumns.RAINFALL,
            WeatherType.TRACK_TEMP: WeatherColumns.TRACK_TEMP,
            WeatherType.AIR_TEMP: WeatherColumns.AIR_TEMP,
            WeatherType.HUMIDITY: WeatherColumns.HUMIDITY,
            WeatherType.PRESSURE: WeatherColumns.PRESSURE,
            WeatherType.WIND_SPEED: WeatherColumns.WIND_SPEED,
        }
    
    @staticmethod
    def categorize_value(weather_type, value):
        """Categorize weather values into interpretable ranges"""
        if weather_type == WeatherType.RAINFALL:
            return "Rainy" if value else "Dry"
        
        elif weather_type == WeatherType.TRACK_TEMP:
            if value < 20:
                return "Cold Track (<20°C)"
            elif value < 30:
                return "Medium Track (20-30°C)"
            else:
                return "Hot Track (>30°C)"
                
        elif weather_type == WeatherType.AIR_TEMP:
            if value < 20:
                return "Cold Air (<20°C)"
            elif value < 25:
                return "Medium Air (20-25°C)"
            else:
                return "Hot Air (>25°C)"
                
        elif weather_type == WeatherType.HUMIDITY:
            if value < 40:
                return "Low Humidity (<40%)"
            elif value < 70:
                return "Medium Humidity (40-70%)"
            else:
                return "High Humidity (>70%)"
                
        elif weather_type == WeatherType.PRESSURE:
            if value < 990:
                return "Low Pressure (<990 hPa)"
            elif value < 1020:
                return "Medium Pressure (990-1020 hPa)"
            else:
                return "High Pressure (>1020 hPa)"
                
        elif weather_type == WeatherType.WIND_SPEED:
            if value < 10:
                return "Light Wind (<10 km/h)"
            elif value < 20:
                return "Medium Wind (10-20 km/h)"
            else:
                return "Strong Wind (>20 km/h)"
        
        return "Unknown"


class DriverWeatherPerf:
    """Analyzes driver performance under different weather conditions"""
    
    def __init__(self) -> None:
        LOGGER.debug("Initializing DriverWeatherPerf class")
        self._drivers = Drivers()
        self._results = Results()
        self._races = Races()
        self._weather = Weather()
        
    def get_data(
        self,
        season_year: int,
        driver_names: list[str] = None,
        weather_type: str = WeatherType.RAINFALL
    ) -> pd.DataFrame:
        """
        Description
        -----------
        Get the performance of drivers based on weather conditions in a given season.

        Parameters
        ----------
        season_year : int
            The season to get the performance for (2018-2023).
        driver_names : list[str], optional
            A list of driver names to filter the results by, by default None.
        weather_type : str, optional
            The weather condition to analyze, by default 'rainfall'.
            Options: rainfall, track_temp, air_temp, humidity, pressure, wind_speed

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the performance metrics of drivers under different 
            weather conditions in the specified season.
        """
        LOGGER.debug(f"Getting driver weather performance for {season_year}, {driver_names}, {weather_type}")
        
        if not isinstance(season_year, int):
            raise TypeError("Season year must be an integer")
        if season_year < 1996 or season_year > 2023:
            raise InvalidSeasonException(season_year, range(1996, 2024))
        if weather_type not in WeatherType.get_all_types():
            raise ValueError(f"Weather type must be one of: {', '.join(WeatherType.get_all_types())}")
        
        self._check_season(season_year)
        
        driver_df = self._drivers.get_driver_fullnames()
        if driver_names:
            if not isinstance(driver_names, list):
                raise TypeError("Driver names must be a list")
            self._validate_drivers(driver_names, driver_df)
        
        results_df = self._results.get_selected_columns(
            ResultsColumns.RACE_ID,
            ResultsColumns.DRIVER_ID,
            ResultsColumns.POSITION,
            ResultsColumns.POINTS
        )
        
        races_df = self._races.get_selected_columns(
            RacesColumns.YEAR,
            RacesColumns.ROUND
        )
        races_df = races_df[races_df[RacesColumns.YEAR] == season_year].reset_index()
        
        if races_df.empty:
            raise SeasonNotFoundException(season_year)
        
        weather_df = self._weather.get_selected_columns(
            WeatherColumns.ROUND,
            WeatherColumns.YEAR,
            WeatherType.get_column_map()[weather_type]
        )
        weather_df = weather_df[weather_df[WeatherColumns.YEAR] == season_year]
        
        if weather_df.empty:
            LOGGER.warning(f"No weather data found for season {season_year}")
            return pd.DataFrame()
        
        race_weather = pd.merge(
            races_df,
            weather_df,
            left_on=[RacesColumns.ROUND, RacesColumns.YEAR],
            right_on=[WeatherColumns.ROUND, WeatherColumns.YEAR]
        ).drop(columns=[WeatherColumns.ROUND, WeatherColumns.YEAR])
        
        merged_data = pd.merge(
            results_df,
            race_weather,
            left_on=ResultsColumns.RACE_ID,
            right_on=RacesColumns.RACE_ID
        )

        merged_data = pd.merge(
            merged_data,
            driver_df.reset_index(),
            left_on=ResultsColumns.DRIVER_ID,
            right_on=DriversColumns.DRIVER_ID
        )
        
        if driver_names:
            merged_data = merged_data[merged_data[DriversColumns.FULLNAME].isin(driver_names)]
        
        weather_col = WeatherType.get_column_map()[weather_type]
        merged_data['weather_category'] = merged_data[weather_col].apply(
            lambda x: WeatherType.categorize_value(weather_type, x)
        )
        
        performance_data = self._calculate_performance_metrics(merged_data)
        
        return performance_data
    
    def _check_season(self, season_year: int) -> None:
        """Prepare and validate the base data"""
        LOGGER.debug(f"Preparing data for season {season_year}")
        
        season_races = self._races.get_data()
        season_races = season_races[season_races[RacesColumns.YEAR] == season_year]
        
        if season_races.empty:
            raise SeasonNotFoundException(season_year)
    
    def _validate_drivers(self, driver_names: list[str], driver_df: pd.DataFrame) -> None:
        """Validate that all requested drivers exist"""
        for driver in driver_names:
            if driver not in driver_df.values:
                raise DriverNotFoundException(driver)
    
    def _calculate_performance_metrics(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate various performance metrics for each driver by weather category"""
        grouped = data.groupby(['fullname', 'weather_category'])

        metrics = grouped.agg(
            avg_position=pd.NamedAgg(column='position', aggfunc=lambda x: x.astype(float).mean()),
            avg_points=pd.NamedAgg(column='points', aggfunc='mean'),
            total_points=pd.NamedAgg(column='points', aggfunc='sum'),
            race_count=pd.NamedAgg(column='raceId', aggfunc='count'),
            win_count=pd.NamedAgg(column='position', aggfunc=lambda x: (x == 1).sum()),
            podium_count=pd.NamedAgg(column='position', aggfunc=lambda x: (x <= 3).sum())
        ).reset_index()
        
        metrics['win_rate'] = (metrics['win_count'] / metrics['race_count'] * 100).round(2)
        metrics['podium_rate'] = (metrics['podium_count'] / metrics['race_count'] * 100).round(2)
        
        metrics = metrics.sort_values(['fullname', 'weather_category'])
        
        return metrics

    def compare_drivers_in_conditions(
        self,
        season_year: int,
        driver_names: list[str],
        weather_type: str = WeatherType.RAINFALL
    ) -> pd.DataFrame:
        """
        Compare multiple drivers' performances in different weather conditions
        for a specified season.
        
        This is useful for direct driver-to-driver comparisons in specific conditions.
        """
        performance_data = self.get_data(season_year, driver_names, weather_type)
        
        pivot_data = performance_data.pivot(
            index='weather_category',
            columns='fullname',
            values=['avg_position', 'avg_points', 'win_rate', 'podium_rate']
        )
        
        return pivot_data
    
    def get_driver_best_conditions(
        self,
        season_year: int,
        driver_name: str,
    ) -> dict:
        """
        Find the weather conditions where a driver performs best
        based on various metrics.
        
        Returns a dictionary with the best condition for each metric.
        """
        best_conditions = {}
        
        for weather_type in WeatherType.get_all_types():
            LOGGER.debug(f"Analyzing {weather_type} for {driver_name}")
            try:
                data = self.get_data(season_year, [driver_name], weather_type)
                
                if not data.empty:
                    best_pos_idx = data['avg_position'].idxmin()
                    best_conditions[f'best_{weather_type}_position'] = {
                        'condition': data.loc[best_pos_idx, 'weather_category'],
                        'value': round(data.loc[best_pos_idx, 'avg_position'], 2)
                    }
                    
                    best_points_idx = data['avg_points'].idxmax()
                    best_conditions[f'best_{weather_type}_points'] = {
                        'condition': data.loc[best_points_idx, 'weather_category'],
                        'value': round(data.loc[best_points_idx, 'avg_points'], 2)
                    }
            except Exception as e:
                LOGGER.warning(f"Error analyzing {weather_type}: {e}")
        
        return best_conditions