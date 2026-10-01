import os
import pandas as pd
import numpy as np

STUDYID = "HYPER-P2"

os.makedirs(
    "data/sdtm",
    exist_ok=True
)


def iso_date(value):

    if pd.isna(value):
        return ""

    return pd.to_datetime(
        value
    ).strftime("%Y-%m-%d")


def study_day(date_value, reference_date):

    if pd.isna(date_value):
        return np.nan

    if pd.isna(reference_date):
        return np.nan

    return (
        pd.Timestamp(date_value)
        - pd.Timestamp(reference_date)
    ).days + 1
