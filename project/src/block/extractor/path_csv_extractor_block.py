import pandas as pd

from src.block.extractor.extractor_block import ExtractorBlock


class PathExtractorBlock(ExtractorBlock):
    def __init__(self, url: str):
        self.url = url

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
                           engine="python"),
