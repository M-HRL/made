import pandas as pd

from src.block.loader.loader_block import LoaderBlock


class RideSqliteLoaderBlock(LoaderBlock):
    def __init__(self):
        super().__init__()

    def invoke(self, ride_df: pd.DataFrame):
        ride_df.to_sql("ride", con=self.engine, if_exists="replace")
