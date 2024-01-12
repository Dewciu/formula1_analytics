from formula1_analytics.races.races import Races
from formula1_analytics.results.results import Results


if __name__ == "__main__":
    data1 = Results().get_data()
    data = Races().get_data()
    print(data.dtypes)
    print(data1.dtypes)
