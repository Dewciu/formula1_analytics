import pandas as pd
from formula1_analytics.config.config import DRIVERS_FILENAME
from formula1_analytics.common.f1_data import F1Data


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


class Drivers(F1Data):
    def __init__(self) -> None:
        super().__init__(DRIVERS_FILENAME, DriversColumns.DRIVER_ID)

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
