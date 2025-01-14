"""Main module for test_polars."""

import typer

from test_polars._cli import check_join


def main() -> None:
    """Entry point for test_polars."""
    typer.run(check_join)


if __name__ == "__main__":
    main()
