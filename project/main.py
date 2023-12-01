from src.base.pipeline import Pipeline
from src.block.extractor.path_csv_extractor_block import PathExtractorBlock
from src.block.extractor.ride_csv_extractor_block import RideExtractorBlock
from src.block.loader.path_sqlite_loader_block import PathSqliteLoaderBlock
from src.block.loader.ride_sqlite_loader_block import RideSqliteLoaderBlock
from src.block.transformer.clean_ride_transformer_block import CleanRideTransformerBlock
from src.block.transformer.extend_path_transformer_block import ExtendPathTransformerBlock

ride_pipeline = Pipeline().register(RideExtractorBlock()).register(CleanRideTransformerBlock()).register(
    RideSqliteLoaderBlock())
path_pipeline = Pipeline().register(PathExtractorBlock()).register(ExtendPathTransformerBlock()).register(
    PathSqliteLoaderBlock())

if __name__ == '__main__':
    ride_pipeline.invoke()
    path_pipeline.invoke()
