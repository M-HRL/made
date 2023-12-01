import pandas as pd

from src.block.transformer.transformer_block import TransformerBlock


class ExtendPathTransformerBlock(TransformerBlock):
    def invoke(self, path_df: pd.DataFrame) -> tuple[pd.DataFrame]:
        path_df["utm_zone"] = "32U"
        return path_df,
