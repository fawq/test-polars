import polars as pl

from pathlib import Path


def get_csv(file_path: Path) -> pl.DataFrame:
    return pl.read_csv(file_path)