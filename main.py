from formula1_analytics.drivers.driver_weather_perf import DriverWeatherPerf, WeatherType


if __name__ == "__main__":
    driver_weather = DriverWeatherPerf()
    season_year = 2020 
    driver_names = ["Lewis Hamilton", "Max Verstappen"]
    
    rainfall_perf = driver_weather.get_data(
        season_year=season_year,
        driver_names=driver_names,
        weather_type=WeatherType.WIND_SPEED
    )

    print(rainfall_perf)
