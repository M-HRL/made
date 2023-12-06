import pandas as pd
from sqlalchemy import (
    Column,
    Integer,
    Text
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Car(Base):
    __tablename__ = "cars"
    date: str = Column(Text(10), nullable=False)
    CIN: str = Column(Text(5), primary_key=True)
    name: str = Column(Text(50), nullable=False)
    petrol: int = Column(Integer, nullable=False)
    diesel: int = Column(Integer, nullable=False)
    gas: int = Column(Integer, nullable=False)
    electro: int = Column(Integer, nullable=False)
    hybrid: int = Column(Integer, nullable=False)
    plugInHybrid: int = Column(Integer, nullable=False)
    others: int = Column(Integer, nullable=False)


def load_data() -> pd.DataFrame:
    csv_url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
    return pd.read_csv(
        csv_url,
        sep=";",
        skiprows=7,
        skipfooter=4,
        header=None,
        index_col=0,
        usecols=[0, 1, 2, 12, 22, 32, 42, 52, 62, 72],
        names=[
            "date",
            "CIN",
            "name",
            "petrol",
            "diesel",
            "gas",
            "electro",
            "hybrid",
            "plugInHybrid",
            "others",
        ],
        dtype={
            "date": str,
            "CIN": str,
            "name": str,
            "petrol": "Int64",
            "diesel": "Int64",
            "gas": "Int64",
            "electro": "Int64",
            "hybrid": "Int64",
            "plugInHybrid": "Int64",
            "others": "Int64",
        },
        na_values=["-"],
        on_bad_lines="skip",
        encoding="iso-8859-1",
        engine="python"
    )


def clean_data(cars_df: pd.DataFrame) -> pd.DataFrame:
    cars_df = cars_df.dropna(axis=0)
    cars_df = cars_df[cars_df["petrol"] > 0]
    cars_df = cars_df[cars_df["diesel"] > 0]
    cars_df = cars_df[cars_df["gas"] > 0]
    cars_df = cars_df[cars_df["electro"] > 0]
    cars_df = cars_df[cars_df["hybrid"] > 0]
    cars_df = cars_df[cars_df["plugInHybrid"] > 0]
    cars_df = cars_df[cars_df["others"] > 0]
    cars_df = cars_df[cars_df["CIN"].str.match(r"^[0-9]{5}$")]
    return cars_df


def save_data(cars_df: pd.DataFrame):
    conn_string = "sqlite:///cars.sqlite"
    engine = create_engine(conn_string, echo=True, future=True)
    Base.metadata.create_all(engine)
    cars_df.to_sql("cars", con=engine, if_exists="replace")


if __name__ == '__main__':
    df = load_data()
    df = clean_data(df)
    save_data(df)
