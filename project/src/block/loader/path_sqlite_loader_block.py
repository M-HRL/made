import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from src.block.loader.loader_block import LoaderBlock
from src.model.entities import Path


class PathSqliteLoaderBlock(LoaderBlock):
    def __init__(self, engine: Engine):
        self.engine = engine

    def invoke(self, path_df: pd.DataFrame):
        records = path_df.to_dict("records")
        with Session(self.engine) as session:
            for record in records:
                path = Path(**record)
                session.add(path)
            session.commit()
