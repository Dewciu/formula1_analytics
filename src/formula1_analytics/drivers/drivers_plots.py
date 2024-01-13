from io import BytesIO
import matplotlib.axes as plta
import matplotlib.pyplot as plt
from formula1_analytics.drivers.drivers_season_perf import DriversSeasonPerf
from formula1_analytics.drivers.drivers_most_wins import DriversMostWins


class DriversPlots:
    @staticmethod
    def plot_drivers_season_performance(
        season_year: int,
        driver_names: list[str] = None,
    ) -> bytes:
        drivers_season_perf = DriversSeasonPerf().get_data(season_year, driver_names)

        drivers_season_perf_plot = drivers_season_perf.plot(
            figsize=(25, 20), grid=True, lw=3
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
        drivers_most_wins = DriversMostWins().get_data(count)
        drivers_most_wins_plot = drivers_most_wins.plot(
            kind="bar", x="fullname", y="wins", legend=True
        )
        drivers_most_wins_plot.set_xlabel("Driver")
        drivers_most_wins_plot.set_ylabel("Wins")
        drivers_most_wins_plot.legend().set_visible(False)
        for index, value in enumerate(drivers_most_wins["wins"]):
            drivers_most_wins_plot.text(index - 0.25, value + 1, str(value))

        return drivers_most_wins_plot
