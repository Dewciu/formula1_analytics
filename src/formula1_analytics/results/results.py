import pandas as pd
from formula1_analytics.config.config import RESULTS_FILENAME
from formula1_analytics.common.f1_data import F1Data
from formula1_analytics.common.data_processor import DataProcessor


class ResultsColumns:
    RESULT_ID = "resultId"
    RACE_ID = "raceId"
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

    @staticmethod
    def get_types() -> dict:
        return {
            ResultsColumns.RACE_ID: "Int64",
            ResultsColumns.DRIVER_ID: "Int64",
            ResultsColumns.CONSTRUCTOR_ID: "Int64",
            ResultsColumns.NUMBER: "Int64",
            ResultsColumns.GRID: "Int64",
            ResultsColumns.POSITION: "Int64",
            ResultsColumns.POSITION_TEXT: "string",
            ResultsColumns.POSITION_ORDER: "Int64",
            ResultsColumns.POINTS: "Float64",
            ResultsColumns.LAPS: "Int64",
            ResultsColumns.TIME: "string",
            ResultsColumns.MILLISECONDS: "Int64",
            ResultsColumns.FASTEST_LAP: "Int64",
            ResultsColumns.RANK: "Int64",
            ResultsColumns.FASTEST_LAP_TIME: "datetime64[ns]",
            ResultsColumns.FASTEST_LAP_SPEED: "Float64",
            ResultsColumns.STATUS_ID: "Int64",
        }


class Results(F1Data):
    def __init__(self) -> None:
        super().__init__(RESULTS_FILENAME, ResultsColumns.RESULT_ID)
        DataProcessor().convert_types(self._data, ResultsColumns.get_types())

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
