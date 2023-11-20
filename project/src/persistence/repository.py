import pandas as pd
from sqlalchemy import create_engine

from project.src.persistence.entities import init_all_tables


class Repository:
    def __init__(self):
        conn_string = "sqlite:///../../data/bike_data.sqlite"
        self.engine = create_engine(conn_string, echo=True, future=True)
        init_all_tables(self.engine)

    def save_rides(self, ride_df: pd.DataFrame):
        ride_df.to_sql("ride", con=self.engine, if_exists="append")

    def save_paths(self, path_df: pd.DataFrame):
        path_df.to_sql("path", con=self.engine, if_exists="append")
