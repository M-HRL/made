import pandas as pd

from src.block.transformer.transformer_block import TransformerBlock


class CleanRideTransformerBlock(TransformerBlock):
    def invoke(self, ride_df: pd.DataFrame) -> tuple[pd.DataFrame]:
        return ride_df.dropna(axis=0, subset=["return_is_station"]),
