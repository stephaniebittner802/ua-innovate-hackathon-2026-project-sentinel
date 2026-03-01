# imports
from app.config import VALID_LOCATIONS, VALID_RESOURCE_TYPES
from app.routers.HistoricStockLevels import list_HistoricStockLevels_location_and_type
from fastapi import APIRouter, Depends, status, HTTPException, Form
from sqlmodel import Session, select
from app.services.database.session import get_session

import polars as pl
import numpy as np
# from sklearn.linear_model import LinearRegression   # good for outliers
import statsmodels.formula.api as smf


def take_after_true(df: pl.DataFrame, ts_col: str = "timestamp", flag_col: str = "snap_event") -> pl.DataFrame:

    # Get the timestamp of the True row (if any)
    true_row = df.filter(pl.col(flag_col))
    if true_row.height == 0:
        # No True -> return original (per your description)
        return df

    true_ts = true_row.select(pl.col(ts_col)).item()  # assumes only one True

    # Keep rows with timestamps AFTER (>=) the True row (including the True row)
    return df.filter(pl.col(ts_col) >= true_ts)
    




def time_to_zero(resource_type: str, location: str, session: Session = Depends(get_session)):
    if resource_type not in VALID_RESOURCE_TYPES:
        print("Not valid resource type")
        return 
    if location not in VALID_LOCATIONS:
        print("Not valid location")
        return
    
    data = list_HistoricStockLevels_location_and_type(
        location=location,
        resource_type=resource_type,
        session=session
        )
    # print(type(data))

    df = pl.from_dicts(data)

    # print(df.shape)
    # print(df.head())

    df = df.sort(pl.col('timestamp'),descending=True).head(20)

    # print("BEFORE")
    # print(df)
    
    # forces one to be true (just to test)
    # df = df.with_columns(
    #     pl.when(pl.arange(0, df.height) == 7)
    #     .then(True)
    #     .otherwise(pl.col("snap_event"))
    #     .alias("snap_event")
    # )


    df = take_after_true(df)

    df = df.with_columns(
        ((pl.col('timestamp').dt.epoch("s") - pl.col("timestamp").dt.epoch("s").first()) / 3600).alias('time_in_hours')
    )

    # print(df)
    
    model = smf.ols(
        data=df,
        formula='stock_level ~ time_in_hours'
    )

    model = model.fit()

    b0 = model.params['Intercept']
    b1 = model.params['time_in_hours']

    if b1 >= 0:
        print("Warning: slope >= 0; the fitted line does not decrease to 0.")
    
    hours = -b0 / b1

    # days = seconds / 24


    # return days for time to zero and potentially the date that the potential exhaustion data occurs
    # its just days 
    return hours


