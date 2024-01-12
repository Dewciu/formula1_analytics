import pandas as pd
from formula1_analytics.config.config import DRIVERS_FILENAME
from formula1_analytics.common.f1_data import F1Data
from formula1_analytics.common.data_processor import DataProcessor


class DriversColumns:
    DRIVER_ID = "driverId"
    DRIVER_REF = "driverRef"
    NUMBER = "number"
    CODE = "code"
    FORENAME = "forename"
    SURNAME = "surname"
    DOB = "dob"
    NATIONALITY = "nationality"
    URL = "url"
    FULLNAME = "fullname"

    @staticmethod
    def get_types() -> dict[str, str]:
        return {
            DriversColumns.NUMBER: "Int64",
            DriversColumns.CODE: "string",
            DriversColumns.FORENAME: "string",
            DriversColumns.SURNAME: "string",
            DriversColumns.DOB: "string",
            DriversColumns.NATIONALITY: "string",
            DriversColumns.URL: "string",
        }


class Drivers(F1Data):
    def __init__(self) -> None:
        super().__init__(DRIVERS_FILENAME, DriversColumns.DRIVER_ID)
        DataProcessor().convert_types(self._data, DriversColumns.get_types())

    def get_refs(self) -> pd.Series:
        return self._data[DriversColumns.DRIVER_REF]

    def get_numbers(self) -> pd.Series:
        return self._data[DriversColumns.NUMBER]

    def get_codes(self) -> pd.Series:
        return self._data[DriversColumns.CODE]

    def get_forenames(self) -> pd.Series:
        return self._data[DriversColumns.FORENAME]

    def get_surnames(self) -> pd.Series:
        return self._data[DriversColumns.SURNAME]

    def get_dobs(self) -> pd.Series:
        return self._data[DriversColumns.DOB]

    def get_nationalities(self) -> pd.Series:
        return self._data[DriversColumns.NATIONALITY]

    def get_url(self) -> pd.Series:
        return self._data[DriversColumns.URL]

    def get_driver_fullnames(self) -> pd.Series:
        driver_fullnames = (
            self._data[DriversColumns.FORENAME]
            + " "
            + self._data[DriversColumns.SURNAME]
        )
        driver_fullnames.name = DriversColumns.FULLNAME
        return driver_fullnames


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
            ResultsColumns.POSITION: "int64",
            ResultsColumns.POSITION_TEXT: "string",
            ResultsColumns.POSITION_ORDER: "Int64",
            ResultsColumns.POINTS: "Float64",
            ResultsColumns.LAPS: "Int64",
            ResultsColumns.TIME: "string",
            ResultsColumns.MILLISECONDS: "Int64",
            ResultsColumns.FASTEST_LAP: "Int64",
            ResultsColumns.RANK: "Int64",
            ResultsColumns.FASTEST_LAP_TIME: "string",
            ResultsColumns.FASTEST_LAP_SPEED: "Float64",
            ResultsColumns.STATUS_ID: "Int64",
        }
