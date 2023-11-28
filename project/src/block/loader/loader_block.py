import pandas as pd
from sqlalchemy import create_engine

from src.base.block import Block
from src.model.entities import init_all_tables


class LoaderBlock(Block):
    def __init__(self):
        conn_string = "sqlite:///../data/bike_data.sqlite"
        self.engine = create_engine(conn_string, echo=True, future=True)
        init_all_tables(self.engine)

    def invoke(self, *args: pd.DataFrame):
        return args
