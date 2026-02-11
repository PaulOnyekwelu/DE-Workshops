#!/usr/bin/env python
import click
import pandas as pd
from sqlalchemy import create_engine

data_types = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
file_name = "./yellow_tripdata_2021-01.csv"

@click.command
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2021, type=int, help='Year of the data')
@click.option('--month', default=1, type=int, help='Month of the data')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
@click.option('--chunk-size', default=100000, type=int, help='Chunk size for reading CSV')

def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table, chunk_size):
    engine = create_engine(f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")
    # inserting data in chunks
    df_iter = pd.read_csv(
        file_name,
        dtype=data_types,  # type: ignore
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunk_size,
    )  # type: ignore

    first = True

    for df_chunk in df_iter:
        if first:
            df_chunk.head(0).to_sql(
                name=target_table, con=engine, if_exists="replace"
            )
            first = False
            print(f"Table ('yellow_taxi_data') created!")

        df_chunk.to_sql(name=target_table, con=engine, if_exists="append")
        print(f"Inserted: {len(df_chunk)}")


if __name__ == "__main__":
    run()
