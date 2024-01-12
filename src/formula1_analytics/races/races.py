import pandas as pd
from formula1_analytics.config.config import RACES_FILENAME
from formula1_analytics.common.f1_data import F1Data
from formula1_analytics.common.data_processor import DataProcessor


class RacesColumns:
    RACE_ID = "raceId"
    YEAR = "year"
    ROUND = "round"
    CIRCUIT_ID = "circuitId"
    NAME = "name"
    DATE = "date"
    TIME = "time"
    URL = "url"
    FP1_DATE = "fp1_date"
    FP1_TIME = "fp1_time"
    FP2_DATE = "fp2_date"
    FP2_TIME = "fp2_time"
    FP3_DATE = "fp3_date"
    FP3_TIME = "fp3_time"
    QUALI_DATE = "quali_date"
    QUALI_TIME = "quali_time"
    SPRINT_DATE = "sprint_date"
    SPRINT_TIME = "sprint_time"

    @staticmethod
    def get_types() -> dict:
        return {
            RacesColumns.YEAR: "Int64",
            RacesColumns.ROUND: "Int64",
            RacesColumns.CIRCUIT_ID: "Int64",
            RacesColumns.NAME: "string",
            RacesColumns.DATE: "datetime64[ns]",
            RacesColumns.TIME: "datetime64[ns]",
            RacesColumns.URL: "string",
            RacesColumns.FP1_DATE: "datetime64[ns]",
            RacesColumns.FP1_TIME: "datetime64[ns]",
            RacesColumns.FP2_DATE: "datetime64[ns]",
            RacesColumns.FP2_TIME: "datetime64[ns]",
            RacesColumns.FP3_DATE: "datetime64[ns]",
            RacesColumns.FP3_TIME: "datetime64[ns]",
            RacesColumns.QUALI_DATE: "datetime64[ns]",
            RacesColumns.QUALI_TIME: "datetime64[ns]",
            RacesColumns.SPRINT_DATE: "datetime64[ns]",
            RacesColumns.SPRINT_TIME: "datetime64[ns]",
        }


class Races(F1Data):
    def __init__(self) -> None:
        super().__init__(RACES_FILENAME, RacesColumns.RACE_ID)
        DataProcessor().convert_types(self._data, RacesColumns.get_types())

    def get_race_ids(self) -> pd.Series:
        return self._data[RacesColumns.RACE_ID]

    def get_years(self) -> pd.Series:
        return self._data[RacesColumns.YEAR]

    def get_rounds(self) -> pd.Series:
        return self._data[RacesColumns.ROUND]

    def get_circuit_ids(self) -> pd.Series:
        return self._data[RacesColumns.CIRCUIT_ID]

    def get_names(self) -> pd.Series:
        return self._data[RacesColumns.NAME]

    def get_dates(self) -> pd.Series:
        return self._data[RacesColumns.DATE]

    def get_times(self) -> pd.Series:
        return self._data[RacesColumns.TIME]

    def get_urls(self) -> pd.Series:
        return self._data[RacesColumns.URL]

    def get_fp1_dates(self) -> pd.Series:
        return self._data[RacesColumns.FP1_DATE]

    def get_fp1_times(self) -> pd.Series:
        return self._data[RacesColumns.FP1_TIME]

    def get_fp2_dates(self) -> pd.Series:
        return self._data[RacesColumns.FP2_DATE]

    def get_fp2_times(self) -> pd.Series:
        return self._data[RacesColumns.FP2_TIME]

    def get_fp3_dates(self) -> pd.Series:
        return self._data[RacesColumns.FP3_DATE]

    def get_fp3_times(self) -> pd.Series:
        return self._data[RacesColumns.FP3_TIME]

    def get_quali_dates(self) -> pd.Series:
        return self._data[RacesColumns.QUALI_DATE]

    def get_quali_times(self) -> pd.Series:
        return self._data[RacesColumns.QUALI_TIME]

    def get_sprint_dates(self) -> pd.Series:
        return self._data[RacesColumns.SPRINT_DATE]

    def get_sprint_times(self) -> pd.Series:
        return self._data[RacesColumns.SPRINT_TIME]
