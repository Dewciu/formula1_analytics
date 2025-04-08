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
