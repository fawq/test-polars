import polars as pl


def join_inner(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="inner",
    )


def join_right(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="right",
    )


def join_left(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="left",
    )


def join_full(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="full",
    )


def join_outer(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="outer",
    )


def join_cross(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="cross",
    )


def join_semi(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="semi",
    )


def join_anti(df1: pl.DataFrame, df2: pl.DataFrame) -> pl.DataFrame:
    return df1.join(
        df2,
        left_on=["src_ip", "dst_ip", "seq_num"],
        right_on=["dst_ip", "src_ip", "seq_num"],
        how="anti",
    )
