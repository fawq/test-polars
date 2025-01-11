from pathlib import Path

import polars as pl

from test_polars.utils.csv import get_csv
from test_polars.utils.process_data import (
    join_anti,
    join_full,
    join_inner,
    join_left,
    join_outer,
    join_right,
    join_semi,
)


def check_join(csv_request_path: Path, csv_response_path: Path) -> None:
    pl.Config.set_tbl_formatting("ASCII_MARKDOWN")

    csv_request_dataframe: pl.DataFrame = get_csv(csv_request_path.absolute())
    csv_response_dataframe: pl.DataFrame = get_csv(csv_response_path.absolute())

    print(f"Full request dataframe: {csv_request_dataframe}")
    print(f"Full response dataframe: {csv_response_dataframe}")

    print(f"Inner: {join_inner(csv_request_dataframe, csv_response_dataframe)}")
    print(f"Outer: {join_outer(csv_request_dataframe, csv_response_dataframe)}")

    print(f"Left: {join_left(csv_request_dataframe, csv_response_dataframe)}")
    print(f"Right: {join_right(csv_request_dataframe, csv_response_dataframe)}")

    print(f"Full: {join_full(csv_request_dataframe, csv_response_dataframe)}")

    print(f"Semi: {join_semi(csv_request_dataframe, csv_response_dataframe)}")
    print(f"Anti: {join_anti(csv_request_dataframe, csv_response_dataframe)}")
