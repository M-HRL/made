import pandas as pd

from src.base.block import Block


class TransformerBlock(Block):
    def invoke(self, *args: pd.DataFrame) -> tuple[pd.DataFrame]:
        return args
