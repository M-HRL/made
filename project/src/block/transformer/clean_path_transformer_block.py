import pandas as pd

from src.block.transformer.transformer_block import TransformerBlock


class CleanPathTransformerBlock(TransformerBlock):
    def invoke(self, path_df: pd.DataFrame) -> tuple[pd.DataFrame]:
        path_df["id"] = range(len(path_df))
        path_df["shape_length"] = pd.to_numeric(path_df["shape_length"], errors="coerce").astype(float)
        path_df["start_east"] = pd.to_numeric(path_df["start_east"], errors="coerce").astype(float)
        path_df["start_north"] = pd.to_numeric(path_df["start_north"], errors="coerce").astype(float)
        path_df["end_east"] = pd.to_numeric(path_df["end_east"], errors="coerce").astype(float)
        path_df["end_north"] = pd.to_numeric(path_df["end_north"], errors="coerce").astype(float)
        return path_df.dropna(axis=0, subset=[
            "shape_length",
            "path_type",
            "start_east",
            "start_north",
            "end_east",
            "end_north",
        ]),
