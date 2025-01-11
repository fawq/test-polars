import logging
from pathlib import Path

import polars as pl

from test_polars.utils.process_csv import get_csv
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
    pl.Config.set_tbl_cols(-1)
    pl.Config.set_tbl_rows(-1)
    pl.Config.set_fmt_str_lengths(100)

    csv_request_dataframe: pl.DataFrame = get_csv(csv_request_path.absolute())
    csv_response_dataframe: pl.DataFrame = get_csv(csv_response_path.absolute())

    logging.debug("Full request dataframe: %s", csv_request_dataframe)
    logging.debug("Full response dataframe: %s", csv_response_dataframe)

    logging.debug(
        "Inner: %s", join_inner(csv_request_dataframe, csv_response_dataframe)
    )
    logging.debug(
        "Outer: %s", join_outer(csv_request_dataframe, csv_response_dataframe)
    )

    logging.debug("Left: %s", join_left(csv_request_dataframe, csv_response_dataframe))
    logging.debug(
        "Right: %s", join_right(csv_request_dataframe, csv_response_dataframe)
    )

    logging.debug("Full: %s", join_full(csv_request_dataframe, csv_response_dataframe))

    logging.debug("Semi: %s", join_semi(csv_request_dataframe, csv_response_dataframe))
    logging.debug("Anti: %s", join_anti(csv_request_dataframe, csv_response_dataframe))
