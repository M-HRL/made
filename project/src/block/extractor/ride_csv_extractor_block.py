import pandas as pd

from src.block.extractor.extractor_block import ExtractorBlock
from src.model.entities import Ride


class RideExtractorBlock(ExtractorBlock):
    def __init__(self):
        self.url = "https://www.mvg.de/dam/mvg/services/mobile-services/mvg-rad/fahrten-csv/MVG_Rad_Fahrten_2022.zip"

    def invoke(self, *args) -> tuple[pd.DataFrame]:
        return pd.read_csv(self.url, compression="zip", sep=r"\s*;", skipinitialspace=True, header=0,
                           names=[
                               "id",
                               "start_time",
                               "end_time",
                               "start_lat",
                               "start_lon",
                               "end_lat",
                               "end_lon",
                               "rental_is_station",
                               "rental_station_name",
                               "return_is_station",
                               "return_station_name"
                           ],
                           index_col="id",
                           dtype=Ride,
                           engine="python"),
