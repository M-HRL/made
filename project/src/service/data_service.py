import pandas as pd

from project.src.persistence.entities import Ride, Path
from project.src.persistence.repository import Repository


class DataService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def load_rides(self, url: str):
        ride_df = pd.read_csv(url, compression="zip", sep=r"\s*;", skipinitialspace=True, header=0,
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
                              engine="python")
        self.repository.save_rides(ride_df)

    def load_paths(self, url: str):
        path_df = pd.read_csv(url, sep=r"\s*,", skipinitialspace=True, header=0,
                              names=[
                                  "id",
                                  "street_name",
                                  "shape_length",
                                  "path_type",
                                  "start_east",
                                  "start_north",
                                  "end_east",
                                  "end_north",
                              ],
                              index_col="id",
                              dtype=Path,
                              engine="python")
        path_df["utm_zone"] = "32U"
        self.repository.save_paths(path_df)
