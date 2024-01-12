from formula1_analytics.results.results import Results
from formula1_analytics.drivers.drivers import Drivers
from formula1_analytics.drivers.drivers_season_perf import DriversSeasonPerf


if __name__ == "__main__":
    data1 = Results().get_data()
    # data = Races().get_races_by_year(2023)
    print(Drivers().get_driver_fullnames().name)
    # print(data)
    print(
        DriversSeasonPerf().get_data(
            2021,
        )
    )
