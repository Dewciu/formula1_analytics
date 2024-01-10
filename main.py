from formula1_analytics.common.data_loader import DataLoader
from formula1_analytics.config.config import CONSTRUCTORS_FILENAME
from formula1_analytics.common.index import Index

if __name__ == "__main__":
    data = DataLoader().load_data(CONSTRUCTORS_FILENAME)
    print(Index.id_to_index(data, "constructorId"))
