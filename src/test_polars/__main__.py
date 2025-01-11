import typer

from test_polars._cli import check_join


if __name__ == "__main__":
    typer.run(check_join)