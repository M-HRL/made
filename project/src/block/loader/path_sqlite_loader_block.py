import pandas as pd

from src.block.loader.loader_block import LoaderBlock


class PathSqliteLoaderBlock(LoaderBlock):
    def __init__(self):
        super().__init__()

    def invoke(self, path_df: pd.DataFrame):
        path_df.to_sql("path", con=self.engine, if_exists="replace")
