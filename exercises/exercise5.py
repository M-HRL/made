import zipfile
from urllib.request import urlretrieve

import pandas as pd
from sqlalchemy import (
    Column,
    Integer,
    Text, Float
)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Stop(Base):
    __tablename__ = "stops"

    stop_id: int = Column(Integer, primary_key=True)
    stop_name: str = Column(Text(50), nullable=False)
    stop_lat: float = Column(Float, nullable=False)
    stop_lon: float = Column(Float, nullable=False)
    zone_id: int = Column(Integer, nullable=False)


def load_data() -> pd.DataFrame:
    zip_url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
    local_zip_path = "gtfs.zip"

    urlretrieve(zip_url, local_zip_path)

    with zipfile.ZipFile(local_zip_path, "r") as zip_file:
        # Specify the file you want to extract from the zip archive
        csv_file_inside_zip = "stops.txt"

        # Extract the specific file from the zip archive
        with zip_file.open(csv_file_inside_zip) as csv_file:
            # Read the CSV file into a DataFrame
            return pd.read_csv(
                csv_file,
                sep=",",
                header=0,
                usecols=[0, 2, 4, 5, 6],
                dtype={
                    "stop_id": "Int64",
                    "stop_name": str,
                    "stop_lat": "Float64",
                    "stop_lon": "Float64",
                    "zone_id": "Int64"
                },
                na_values=[""],
                quotechar='"',
                on_bad_lines="skip",
                engine="python"
            )


def clean_data(stops_df: pd.DataFrame) -> pd.DataFrame:
    stops_df = stops_df.dropna(axis=0)
    stops_df = stops_df[stops_df["zone_id"] == 2001]
    stops_df = stops_df[stops_df["stop_id"] > 0]
    stops_df = stops_df[stops_df["stop_lat"] >= -90.]
    stops_df = stops_df[stops_df["stop_lat"] <= 90.]
    stops_df = stops_df[stops_df["stop_lon"] >= -90.]
    stops_df = stops_df[stops_df["stop_lon"] <= 90.]
    return stops_df


def save_data(stops_df: pd.DataFrame):
    conn_string = "sqlite:///gtfs.sqlite"
    engine = create_engine(conn_string, echo=True, future=True)
    Base.metadata.create_all(engine)
    stops_df.to_sql("stops", index=False, con=engine, if_exists="replace")


if __name__ == '__main__':
    df = load_data()
    df = clean_data(df)
    save_data(df)
