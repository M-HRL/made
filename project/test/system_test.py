import os
from unittest import TestCase

import osmnx as ox
import sqlalchemy as sa

from src.base.pipeline import Pipeline
from src.block.extractor.path_csv_extractor_block import PathExtractorBlock
from src.block.extractor.ride_csv_extractor_block import RideExtractorBlock
from src.block.loader.path_sqlite_loader_block import PathSqliteLoaderBlock
from src.block.loader.ride_sqlite_loader_block import RideSqliteLoaderBlock
from src.block.transformer.add_node_mappings_transformer_block import AddNodeMappingsTransformerBlock
from src.block.transformer.clean_path_transformer_block import CleanPathTransformerBlock
from src.block.transformer.clean_ride_transformer_block import CleanRideTransformerBlock
from src.block.transformer.convert_path_coordinates_transformer_block import ConvertPathCoordinatesTransformerBlock
from src.model.entities import init_all_tables


class SystemTest(TestCase):
    def setUp(self):
        ride_url = "https://www.mvg.de/dam/mvg/services/mobile-services/mvg-rad/fahrten-csv/MVG_Rad_Fahrten_2022.zip"
        path_url = "https://opendata.muenchen.de/dataset/7ad3bc6c-4c1a-4a63-9cb2-0d613f5b69fa/resource/14977232-94f3-4cdb-94fc-1e709698ba3f/download/radwege_t2.csv"
        conn_string = "sqlite:///../data/bike_data.sqlite"

        ride_frac = 0.001
        ride_seed = 24
        cpus = 2

        engine = sa.engine.create_engine(conn_string, echo=False, future=True)
        graph = ox.graph_from_place("Munich, Bavaria, Germany", network_type="bike")
        graph = ox.speed.add_edge_speeds(graph)
        graph = ox.speed.add_edge_travel_times(graph)

        self.extract_ride_pipeline = Pipeline().register(
            RideExtractorBlock(url=ride_url, frac=ride_frac, seed=ride_seed)).register(
            CleanRideTransformerBlock())
        self.extract_path_pipeline = Pipeline().register(PathExtractorBlock(url=path_url)).register(
            CleanPathTransformerBlock()).register(ConvertPathCoordinatesTransformerBlock())
        self.combined_pipeline = Pipeline().register(AddNodeMappingsTransformerBlock(cpus=cpus, graph=graph))
        self.load_ride_pipeline = Pipeline().register(RideSqliteLoaderBlock(engine=engine))
        self.load_path_pipeline = Pipeline().register(PathSqliteLoaderBlock(engine=engine))

        self.db_file_path = os.path.join(os.path.dirname(__file__), "../../data/bike_data.sqlite")
        if os.path.isfile(self.db_file_path):
            os.remove(self.db_file_path)
        init_all_tables(engine)

    def test_pipeline(self):
        ride_df, = self.extract_ride_pipeline.invoke()
        path_df, = self.extract_path_pipeline.invoke()

        ride_df, path_df = self.combined_pipeline.invoke(ride_df, path_df)

        self.load_ride_pipeline.invoke(ride_df)
        self.load_path_pipeline.invoke(path_df)

        self._assert_db_file_exists()

    def _assert_db_file_exists(self):
        self.assertTrue(os.path.isfile(self.db_file_path))
