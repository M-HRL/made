import os
from unittest import TestCase

from src.base.pipeline import Pipeline
from src.block.extractor.path_csv_extractor_block import PathExtractorBlock
from src.block.extractor.ride_csv_extractor_block import RideExtractorBlock
from src.block.loader.path_sqlite_loader_block import PathSqliteLoaderBlock
from src.block.loader.ride_sqlite_loader_block import RideSqliteLoaderBlock
from src.block.transformer.clean_ride_transformer_block import CleanRideTransformerBlock
from src.block.transformer.extend_path_transformer_block import ExtendPathTransformerBlock


class SystemTest(TestCase):
    def setUp(self):
        self.ride_pipeline = Pipeline().register(RideExtractorBlock()).register(CleanRideTransformerBlock()).register(
            RideSqliteLoaderBlock())
        self.path_pipeline = Pipeline().register(PathExtractorBlock()).register(ExtendPathTransformerBlock()).register(
            PathSqliteLoaderBlock())
        self.db_file_path = os.path.join(os.path.dirname(__file__), "../../data/bike_data.sqlite")
        if os.path.isfile(self.db_file_path):
            os.remove(self.db_file_path)

    def test_ride_pipeline(self):
        self.ride_pipeline.invoke()
        self._assert_db_file_exists()

    def test_path_pipeline(self):
        self.path_pipeline.invoke()
        self._assert_db_file_exists()

    def test_pipeline(self):
        self.ride_pipeline.invoke()
        self.path_pipeline.invoke()
        self._assert_db_file_exists()

    def _assert_db_file_exists(self):
        self.assertTrue(os.path.isfile(self.db_file_path))
