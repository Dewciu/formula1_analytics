import io
import pandas as pd
import pkgutil
import formula1_analytics.config.config as cfg


class DataLoader:
    @staticmethod
    def load_data(filename) -> pd.DataFrame:
        data = pkgutil.get_data("formula1_analytics", f"{cfg.DATA_DIR}{filename}")
        return pd.read_csv(io.BytesIO(data), sep=",", encoding="UTF-8")
