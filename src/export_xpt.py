import os
import pandas as pd
import pyreadstat

os.makedirs(
    "output/xpt",
    exist_ok=True
)

domains = [
    "dm",
    "ae",
    "vs",
    "lb",
    "cm",
    "ex"
]

for domain in domains:

    df = pd.read_csv(
        f"data/sdtm/{domain}.csv"
    )

    output = (
        f"output/xpt/"
        f"{domain}.xpt"
    )

    pyreadstat.write_xport(
        df,
        output,
        table_name=domain.upper()
    )

    print(
        f"Created {output}"
    )
