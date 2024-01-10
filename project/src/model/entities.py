from datetime import datetime

from sqlalchemy import Column, Float, Boolean, DateTime, String, Table, Integer, ForeignKey
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ride_path_mapping_table = Table("ride_path_mapping", Base.metadata,
#                                Column("ride_id", Integer, ForeignKey("ride.id")),
#                                Column("path_id", Integer, ForeignKey("path.id")))

ride_node_mapping_table = Table("ride_node_mapping", Base.metadata,
                                Column("ride_id", Integer, ForeignKey("ride.id")),
                                Column("node_id", Integer, ForeignKey("node.id")))

path_node_mapping_table = Table("path_node_mapping", Base.metadata,
                                Column("path_id", Integer, ForeignKey("path.id")),
                                Column("node_id", Integer, ForeignKey("node.id")))


class Ride(Base):
    __tablename__ = "ride"

    id: int = Column(Integer, primary_key=True, autoincrement=False)
    start_time: datetime = Column(DateTime(timezone=True), nullable=False)
    end_time: datetime = Column(DateTime(timezone=True), nullable=False)
    start_lat: float = Column(Float(64), nullable=False)
    start_lon: float = Column(Float(64), nullable=False)
    end_lat: float = Column(Float(64), nullable=False)
    end_lon: float = Column(Float(64), nullable=False)
    rental_is_station: bool = Column(Boolean, nullable=False)
    rental_station_name: str = Column(String(50))
    return_is_station: bool = Column(Boolean, nullable=False)
    return_station_name: str = Column(String(50))
    nodes = relationship("Node", secondary=ride_node_mapping_table, back_populates="rides")
    # paths = relationship("Path", secondary=ride_path_mapping_table, back_populates="rides")


class Path(Base):
    __tablename__ = "path"

    id: int = Column(Integer, primary_key=True, autoincrement=False)
    street_name: str = Column(String(50))
    shape_length: float = Column(Float(64), nullable=False)
    path_type: str = Column(String(50), nullable=False)
    start_lat: float = Column(Float(64), nullable=False)
    start_lon: float = Column(Float(64), nullable=False)
    end_lat: float = Column(Float(64), nullable=False)
    end_lon: float = Column(Float(64), nullable=False)
    nodes = relationship("Node", secondary=path_node_mapping_table, back_populates="paths")
    # rides = relationship("Ride", secondary=ride_path_mapping_table, back_populates="paths")


class Node(Base):
    __tablename__ = "node"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    osm_id: int = Column(Integer, nullable=False)
    route_order: int = Column(Integer, nullable=False)
    rides = relationship("Ride", secondary=ride_node_mapping_table, back_populates="nodes")
    paths = relationship("Path", secondary=path_node_mapping_table, back_populates="nodes")


def init_all_tables(engine: Engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
