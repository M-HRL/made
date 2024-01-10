import pandas as pd
from pyproj import Proj
from pyproj.enums import TransformDirection

from src.block.transformer.transformer_block import TransformerBlock


class ConvertPathCoordinatesTransformerBlock(TransformerBlock):
    def invoke(self, path_df: pd.DataFrame) -> tuple[pd.DataFrame]:
        # Define the UTM zone for Germany
        utm_zone = 32
        # Create a transformer
        proj = Proj(proj='utm', zone=utm_zone, ellps='WGS84', preserve_units=True)
        # Convert UTM to Longitude / Latitude
        start_lons, start_lats = proj.transform(xx=path_df["start_east"],
                                                yy=path_df["start_north"],
                                                direction=TransformDirection.INVERSE)
        path_df["start_lon"] = start_lons
        path_df["start_lat"] = start_lats
        end_lons, end_lats = proj.transform(xx=path_df["end_east"],
                                            yy=path_df["end_north"],
                                            direction=TransformDirection.INVERSE)
        path_df["end_lon"] = end_lons
        path_df["end_lat"] = end_lats
        # Drop converted columns
        columns_to_drop = ["start_east", "start_north", "end_east", "end_north"]
        path_df.drop(columns=columns_to_drop, inplace=True)
        return path_df,
