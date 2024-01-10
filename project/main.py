import os

from src.base.pipeline import Pipeline
from src.block.extractor.path_csv_extractor_block import PathExtractorBlock
from src.block.extractor.ride_csv_extractor_block import RideExtractorBlock
from src.block.loader.path_sqlite_loader_block import PathSqliteLoaderBlock
from src.block.loader.ride_sqlite_loader_block import RideSqliteLoaderBlock
from src.block.transformer.clean_ride_transformer_block import CleanRideTransformerBlock
from src.block.transformer.convert_path_coordinates_transformer_block import ConvertPathCoordinatesTransformerBlock

db_file_path = os.path.join(os.path.dirname(__file__), "../data/bike_data.sqlite")
ride_pipeline = Pipeline().register(RideExtractorBlock()).register(CleanRideTransformerBlock()).register(
    RideSqliteLoaderBlock())
path_pipeline = Pipeline().register(PathExtractorBlock()).register(ConvertPathCoordinatesTransformerBlock()).register(
    PathSqliteLoaderBlock())

if __name__ == '__main__':
    if os.path.isfile(db_file_path):
        os.remove(db_file_path)
    ride_pipeline.invoke()
    path_pipeline.invoke()
