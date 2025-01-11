"""Module contains functions for joining dataframes."""

import polars as pl


def join_inner(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform an inner join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="inner",
    )


def join_right(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform a right join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="right",
    )


def join_left(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform a left join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="left",
    )


def join_full(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform a full join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="full",
    )


def join_outer(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform an outer join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="outer",
    )


def join_semi(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform a semi join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="semi",
    )


def join_anti(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    """
    Perform an anti join on two dataframes.

    Parameters
    ----------
    df1: polars.DataFrame
        The left DataFrame to join.
    df2: polars.DataFrame
        The right DataFrame to join.

    Returns
    -------
    polars.DataFrame
        The joined DataFrame.

    """
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="anti",
    )
