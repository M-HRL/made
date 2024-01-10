import pandas as pd

from src.block.extractor.extractor_block import ExtractorBlock


class RideExtractorBlock(ExtractorBlock):
    def __init__(self, url: str, frac: float, seed: int):
        self.url = url
        self.frac = frac
        self.seed = seed

    def invoke(self, *args) -> tuple[pd.DataFrame]:
        ride_df = pd.read_csv(self.url, compression="zip", sep=r"\s*;", skipinitialspace=True, header=0,
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
                                  "return_station_name",
                              ],
                              engine="python")
        ride_df = ride_df.sample(frac=self.frac, random_state=self.seed)
        return ride_df,
