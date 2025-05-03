from formula1_analytics.drivers.driver_weather_perf import DriverWeatherPerf, WeatherType
from formula1_analytics.drivers.drivers_season_perf import DriversSeasonPerf


if __name__ == "__main__":
    driver_weather = DriverWeatherPerf()
    season_year = 2020 
    driver_names = ["Lewis Hamilton", "Max Verstappen"]
    
    rainfall_perf = driver_weather.get_data(
        season_year=season_year,
        driver_names=None,
        weather_type=WeatherType.PRESSURE
    )

    print(rainfall_perf)

    season_perf = DriversSeasonPerf().get_data(
        season_year=season_year,
        driver_names=None
    )
    print(season_perf.columns.to_list())
