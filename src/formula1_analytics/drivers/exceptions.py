class DriverNotFoundException(Exception):
    def __init__(self, driver_name: str) -> None:
        self.driver_id = driver_name
        self.message = f"Driver with id {driver_name} not found"
        super().__init__(self.message)


class SeasonNotFoundException(Exception):
    def __init__(self, season_year: int) -> None:
        self.season_year = season_year
        self.message = f"Season {season_year} not found"
        super().__init__(self.message)


class InvalidSeasonException(Exception):
    def __init__(self, season_year: int, range: list[int]) -> None:
        self.season_year = season_year
        self.message = f"Season {season_year} is invalid, must be between {range[0]} and {range[-1]}"
        super().__init__(self.message)
