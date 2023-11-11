import pandas as pd
from sqlalchemy import (
    Column,
    Integer,
    Float,
    Text
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class Airport(Base):
    __tablename__ = "airports"
    id = Column(Integer, primary_key=True, autoincrement=True)
    column_1 = Column(Integer)
    column_2 = Column(Text(100))
    column_3 = Column(Text(50))
    column_4 = Column(Text(50))
    column_5 = Column(Text(10))
    column_6 = Column(Text(50))
    column_7 = Column(Float)
    column_8 = Column(Float)
    column_9 = Column(Integer)
    column_10 = Column(Float)
    column_11 = Column(Text(10))
    column_12 = Column(Text(50))
    geo_punkt = Column(Text(50))


def load_data() -> pd.DataFrame:
    csv_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
    return pd.read_csv(csv_url, sep=";")


def convert_types(airports_df: pd.DataFrame) -> list[dict]:
    return airports_df.to_dict(orient="records")


def save_data(airports: list[dict]):
    conn_string = "sqlite:///airports.sqlite"
    engine = create_engine(conn_string, echo=True, future=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        for airport_dict in airports:
            airport = Airport(**airport_dict)
            session.add(airport)
        session.commit()


if __name__ == '__main__':
    df = load_data()
    arr = convert_types(df)
    save_data(arr)
