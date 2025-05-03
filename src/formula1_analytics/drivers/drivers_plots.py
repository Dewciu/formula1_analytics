from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.axes as plta
import matplotlib.pyplot as plt
from formula1_analytics.drivers.drivers_season_perf import DriversSeasonPerf
from formula1_analytics.drivers.drivers_most_wins import DriversMostWins
from formula1_analytics.drivers.driver_weather_perf import DriverWeatherPerf


class DriversPlots:
    @staticmethod
    def plot_drivers_season_performance(
        season_year: int,
        driver_names: list[str] = None,
    ) -> bytes:
        drivers_season_perf = DriversSeasonPerf().get_data(season_year, driver_names)
        colors = plt.cm.Paired(np.linspace(0, 0.8, len(drivers_season_perf.columns)))

        drivers_season_perf_plot = drivers_season_perf.plot(
            figsize=(25, 20),
            grid=True,
            lw=7,
            color=colors,
        )
        drivers_season_perf_plot.set_title(
            f"Drivers performance in {season_year} season", fontdict={"fontsize": 40}
        )
        drivers_season_perf_plot.set_xlabel("Round", fontdict={"fontsize": 20})
        drivers_season_perf_plot.set_ylabel("Points", fontdict={"fontsize": 20})
        drivers_season_perf_plot.legend(fontsize=20)
        img_bytes = BytesIO()
        plt.savefig(img_bytes, format="png")
        plt.close()

        return img_bytes.getvalue()

    @staticmethod
    def get_plot_drivers_most_wins(count: int) -> plta.Axes:
        data = DriversMostWins().get_data(count)
        drivers_most_wins = pd.Series(data["wins"].values, index=data["fullname"])
        colors = plt.cm.viridis(np.linspace(0, 1.1, len(drivers_most_wins)))
        print(drivers_most_wins)

        drivers_most_wins_plot = drivers_most_wins.plot(
            kind="bar",
            figsize=(10, 10),
            color=colors,
            grid=True,
        )
        drivers_most_wins_plot.set_xlabel("Driver", fontdict={"fontsize": 20})
        drivers_most_wins_plot.set_ylabel("Wins", fontdict={"fontsize": 20})
        drivers_most_wins_plot.tick_params(axis="x", labelsize=15)
        drivers_most_wins_plot.set_title(
            f"TOP {count} drivers with most wins", fontdict={"fontsize": 20}
        )

        for index, value in enumerate(drivers_most_wins):
            drivers_most_wins_plot.text(
                index,
                value + 1,
                str(value),
                ha="center",
                va="bottom",
                fontdict={"fontsize": 12},
            )

        img_bytes = BytesIO()
        plt.savefig(img_bytes, format="png", bbox_inches="tight")
        plt.close()

        return img_bytes.getvalue()
    

    @staticmethod
    def get_plot_drivers_weather_perf(
        season_year: int,
        driver_name: str = None,
        weather_type: str = None,
    ) -> plta.Axes:
        data = DriverWeatherPerf().get_data(season_year, [driver_name], weather_type)
        driver_weather_perf = data[["fullname", "weather_category", "avg_position"]]
        colors = plt.cm.Paired(np.linspace(0, 0.8, len(driver_weather_perf.columns)))

        drivers_weather_perf_plot = driver_weather_perf.plot(
            figsize=(25, 20),
            grid=True,
            lw=7,
            color=colors,
        )
        drivers_weather_perf_plot.set_title(
            f"{driver_name} performance in {weather_type} in {season_year} season", fontdict={"fontsize": 40}
        )
        drivers_weather_perf_plot.set_xlabel("Round", fontdict={"fontsize": 20})
        drivers_weather_perf_plot.set_ylabel("Points", fontdict={"fontsize": 20})
        drivers_weather_perf_plot.legend(fontsize=20)
        img_bytes = BytesIO()
        plt.savefig(img_bytes, format="png")
        plt.close()

        return img_bytes.getvalue()
