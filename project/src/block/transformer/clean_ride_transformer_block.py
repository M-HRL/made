import pandas as pd

from src.block.transformer.transformer_block import TransformerBlock


class CleanRideTransformerBlock(TransformerBlock):
    def invoke(self, ride_df: pd.DataFrame) -> tuple[pd.DataFrame]:
        ride_df["id"] = range(len(ride_df))
        ride_df["start_time"] = pd.to_datetime(ride_df["start_time"], errors="coerce")
        ride_df["end_time"] = pd.to_datetime(ride_df["end_time"], errors="coerce")
        ride_df["start_lat"] = pd.to_numeric(ride_df["start_lat"], errors="coerce").astype(float)
        ride_df["start_lon"] = pd.to_numeric(ride_df["start_lon"], errors="coerce").astype(float)
        ride_df["end_lat"] = pd.to_numeric(ride_df["end_lat"], errors="coerce").astype(float)
        ride_df["end_lon"] = pd.to_numeric(ride_df["end_lon"], errors="coerce").astype(float)
        ride_df["rental_is_station"] = pd.to_numeric(ride_df["rental_is_station"], errors="coerce").astype(bool)
        ride_df["return_is_station"] = pd.to_numeric(ride_df["return_is_station"], errors="coerce").astype(bool)
        return ride_df.dropna(axis=0, subset=[
            "start_time",
            "end_time",
            "start_lat",
            "start_lon",
            "end_lat",
            "end_lon",
            "rental_is_station",
            "return_is_station",
        ]),
