import pandas as pd

from src.base.block import Block


class LoaderBlock(Block):

    def invoke(self, *args: pd.DataFrame):
        return args
