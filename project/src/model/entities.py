import pandas as pd
from sqlalchemy import Column, Float, Boolean, DateTime, String, BigInteger
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Ride(Base):
    __tablename__ = "ride"

    id: pd.Int64Dtype = Column(BigInteger, primary_key=True)
    start_time: pd.DatetimeTZDtype = Column(DateTime(timezone=True), nullable=False)
    end_time: pd.DatetimeTZDtype = Column(DateTime(timezone=True), nullable=False)
    start_lat: pd.Float64Dtype = Column(Float(64), nullable=False)
    start_lon: pd.Float64Dtype = Column(Float(64), nullable=False)
    end_lat: pd.Float64Dtype = Column(Float(64), nullable=False)
    end_lon: pd.Float64Dtype = Column(Float(64), nullable=False)
    rental_is_station: pd.BooleanDtype = Column(Boolean, nullable=False)
    rental_station_name: pd.StringDtype = Column(String(50))
    return_is_station: pd.BooleanDtype = Column(Boolean, nullable=False)
    return_station_name: pd.StringDtype = Column(String(50))


class Path(Base):
    __tablename__ = "path"

    id: pd.Int64Dtype = Column(BigInteger, primary_key=True)
    street_name: pd.StringDtype = Column(String(50))
    shape_length: pd.Float64Dtype = Column(Float(64), nullable=False)
    path_type: pd.StringDtype = Column(String(50), nullable=False)
    start_east: pd.Float64Dtype = Column(Float(64), nullable=False)
    start_north: pd.Float64Dtype = Column(Float(64), nullable=False)
    end_east: pd.Float64Dtype = Column(Float(64), nullable=False)
    end_north: pd.Float64Dtype = Column(Float(64), nullable=False)
    utm_zone: pd.StringDtype = Column(String(3), nullable=False)


def init_all_tables(engine: Engine):
    Base.metadata.create_all(engine)
