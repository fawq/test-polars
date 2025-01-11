from pathlib import Path

import polars as pl


def get_csv(file_path: Path) -> pl.DataFrame:
    return pl.read_csv(file_path)
