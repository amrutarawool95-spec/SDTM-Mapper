import os
import pandas as pd

SDTM_DIR = "data/sdtm"

os.makedirs(
    "output",
    exist_ok=True
)

results = []


def check(
    domain,
    rule_id,
    description,
    status,
    details=""
):

    results.append({
        "DOMAIN": domain,
        "RULE_ID": rule_id,
        "DESCRIPTION": description,
        "STATUS": status,
        "DETAILS": details
    })


def required_columns(
    df,
    domain,
    columns
):

    missing = [
        c for c in columns
        if c not in df.columns
    ]

    check(
        domain,
        "STRUCT-001",
        "Required variables exist",
        "PASS" if not missing else "FAIL",
        str(missing)
    )
