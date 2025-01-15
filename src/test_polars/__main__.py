"""Main module for test_polars."""

import logging
from pathlib import Path

import polars as pl
import typer

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


def setup_logging() -> None:
    """Configure logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_polars() -> None:
    """Configure polars."""
    pl.Config.set_tbl_formatting("ASCII_MARKDOWN")
    pl.Config.set_tbl_rows(200)
    pl.Config.set_tbl_cols(200)
    pl.Config.set_fmt_str_lengths(200)


def check_join(csv_request_path: Path, csv_response_path: Path) -> None:
    """
    Run the main function.

    Parameters
    ----------
    csv_request_path: Path
        The path to the request CSV file.
    csv_response_path: Path
        The path to the response CSV file.

    """
    setup_logging()
    setup_polars()

    csv_request_dataframe: pl.DataFrame = get_csv(csv_request_path.absolute())
    csv_response_dataframe: pl.DataFrame = get_csv(csv_response_path.absolute())

    logging.info("Full request dataframe: %s", csv_request_dataframe)
    logging.info("Full response dataframe: %s", csv_response_dataframe)

    logging.info("Inner: %s", join_inner(csv_request_dataframe, csv_response_dataframe))
    logging.info("Outer: %s", join_outer(csv_request_dataframe, csv_response_dataframe))

    logging.info("Left: %s", join_left(csv_request_dataframe, csv_response_dataframe))
    logging.info("Right: %s", join_right(csv_request_dataframe, csv_response_dataframe))

    logging.info("Full: %s", join_full(csv_request_dataframe, csv_response_dataframe))

    logging.info("Semi: %s", join_semi(csv_request_dataframe, csv_response_dataframe))
    logging.info("Anti: %s", join_anti(csv_request_dataframe, csv_response_dataframe))

def main() -> None:
    """Entry point for test_polars."""
    typer.run(check_join)


if __name__ == "__main__":
    main()
