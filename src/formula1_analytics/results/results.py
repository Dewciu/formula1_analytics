from formula1_analytics.config.config import RESULTS_FILENAME
from formula1_analytics.common.f1_data import F1Data
import pandas as pd


class ResultsColumns:
    RESULT_ID = "resultId"
    DRIVER_ID = "driverId"
    CONSTRUCTOR_ID = "constructorId"
    NUMBER = "number"
    GRID = "grid"
    POSITION = "position"
    POSITION_TEXT = "positionText"
    POSITION_ORDER = "positionOrder"
    POINTS = "points"
    LAPS = "laps"
    TIME = "time"
    MILLISECONDS = "milliseconds"
    FASTEST_LAP = "fastestLap"
    RANK = "rank"
    FASTEST_LAP_TIME = "fastestLapTime"
    FASTEST_LAP_SPEED = "fastestLapSpeed"
    STATUS_ID = "statusId"


class Results(F1Data):
    def __init__(self) -> None:
        super().__init__(RESULTS_FILENAME, ResultsColumns.RESULT_ID)

    def get_driver_ids(self) -> pd.Series:
        return self._data[ResultsColumns.DRIVER_ID]

    def get_constructor_ids(self) -> pd.Series:
        return self._data[ResultsColumns.CONSTRUCTOR_ID]

    def get_numbers(self) -> pd.Series:
        return self._data[ResultsColumns.NUMBER]

    def get_grids(self) -> pd.Series:
        return self._data[ResultsColumns.GRID]

    def get_positions(self) -> pd.Series:
        return self._data[ResultsColumns.POSITION]

    def get_positions_texts(self) -> pd.Series:
        return self._data[ResultsColumns.POSITION_TEXT]

    def get_positions_orders(self) -> pd.Series:
        return self._data[ResultsColumns.POSITION_ORDER]

    def get_points(self) -> pd.Series:
        return self._data[ResultsColumns.POINTS]

    def get_laps(self) -> pd.Series:
        return self._data[ResultsColumns.LAPS]

    def get_times(self) -> pd.Series:
        return self._data[ResultsColumns.TIME]

    def get_miliseconds(self) -> pd.Series:
        return self._data[ResultsColumns.MILLISECONDS]

    def get_fastest_laps(self) -> pd.Series:
        return self._data[ResultsColumns.FASTEST_LAP]

    def get_rank(self) -> pd.Series:
        return self._data[ResultsColumns.RANK]

    def get_fastest_lap_times(self) -> pd.Series:
        return self._data[ResultsColumns.FASTEST_LAP_TIME]

    def get_fastest_lap_speeds(self) -> pd.Series:
        return self._data[ResultsColumns.FASTEST_LAP_SPEED]

    def get_status_ids(self) -> pd.Series:
        return self._data[ResultsColumns.STATUS_ID]
