import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from src.block.loader.loader_block import LoaderBlock
from src.model.entities import Ride


class RideSqliteLoaderBlock(LoaderBlock):
    def __init__(self, engine: Engine):
        self.engine = engine

    def invoke(self, ride_df: pd.DataFrame):
        records = ride_df.to_dict("records")
        with Session(self.engine) as session:
            for record in records:
                ride = Ride(**record)
                session.add(ride)
            session.commit()
