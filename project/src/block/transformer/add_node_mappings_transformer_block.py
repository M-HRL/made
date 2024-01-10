import networkx as nx
import pandas as pd
from osmnx.distance import nearest_nodes
from osmnx.routing import shortest_path

from src.block.transformer.transformer_block import TransformerBlock
from src.model.entities import Node


def map_node_ids_to_nodes(node_ids: list[int]) -> list[Node]:
    return [Node(osm_id=node_id, route_order=idx) for idx, node_id in enumerate(node_ids)] if node_ids else []


class AddNodeMappingsTransformerBlock(TransformerBlock):
    def __init__(self, cpus: int, graph: nx.MultiDiGraph):
        self.cpus = cpus
        self.graph = graph

    def invoke(self, ride_df: pd.DataFrame, path_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        ride_start_node_ids = nearest_nodes(self.graph, X=ride_df["start_lon"].astype(float).to_list(),
                                            Y=ride_df["start_lat"].astype(float).to_list())
        ride_end_node_ids = nearest_nodes(self.graph, X=ride_df["end_lon"].astype(float).to_list(),
                                          Y=ride_df["end_lat"].astype(float).to_list())

        ride_df["nodes"] = shortest_path(self.graph, ride_start_node_ids, ride_end_node_ids, weight="travel_time",
                                         cpus=self.cpus)
        ride_df["nodes"] = ride_df["nodes"].map(map_node_ids_to_nodes)

        path_start_node_ids = nearest_nodes(self.graph, X=path_df["start_lon"].to_list(),
                                            Y=path_df["start_lat"].to_list())
        path_end_node_ids = nearest_nodes(self.graph, X=path_df["end_lon"].to_list(), Y=path_df["end_lat"].to_list())

        path_df["nodes"] = list(zip(path_start_node_ids, path_end_node_ids))
        path_df["nodes"] = path_df["nodes"].map(map_node_ids_to_nodes)

        return ride_df, path_df
