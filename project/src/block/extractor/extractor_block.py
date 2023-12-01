import pandas as pd

from src.base.block import Block


class ExtractorBlock(Block):
    def invoke(self, *args) -> tuple[pd.DataFrame]:
        return pd.DataFrame(),
