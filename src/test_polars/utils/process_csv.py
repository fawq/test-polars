"""Module contains functions for reading CSV files into Polars DataFrames."""

from pathlib import Path

import polars as pl


def get_csv(file_path: Path) -> pl.DataFrame:
    """
    Read a CSV file into a Polars DataFrame.

    Parameters
    ----------
    file_path: Path
        The path to the CSV file.

    Returns
    -------
    polars.DataFrame
        The Polars DataFrame.

    """
    return pl.read_csv(file_path)
