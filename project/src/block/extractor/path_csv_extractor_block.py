import pandas as pd

from src.block.extractor.extractor_block import ExtractorBlock
from src.model.entities import Path


class PathExtractorBlock(ExtractorBlock):
    def __init__(self):
        self.url = "https://opendata.muenchen.de/dataset/7ad3bc6c-4c1a-4a63-9cb2-0d613f5b69fa/resource/14977232-94f3-4cdb-94fc-1e709698ba3f/download/radwege_t2.csv"

    def invoke(self, *args) -> tuple[pd.DataFrame]:
        return pd.read_csv(self.url, sep=r"\s*,", skipinitialspace=True, header=0,
                           names=[
                               "id",
                               "street_name",
                               "shape_length",
                               "path_type",
                               "start_east",
                               "start_north",
                               "end_east",
                               "end_north",
                           ],
                           index_col="id",
                           dtype=Path,
                           engine="python"),
