use polars::prelude::{DataFrame, DataFrameJoinOps, JoinArgs, JoinType};

/// Perform an inner join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_inner(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Inner),
        None,
    )
    .unwrap_or(DataFrame::default())
}

/// Perform a right join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_right(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Right),
        None,
    )
    .unwrap_or(DataFrame::default())
}

/// Perform a left join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_left(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Left),
        None,
    )
    .unwrap_or(DataFrame::default())
}

/// Perform a full join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_full(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Full),
        None,
    )
    .unwrap_or(DataFrame::default())
}

/// Perform an outer join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_outer(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Full),
        None,
    )
    .unwrap_or(DataFrame::default())
}

/// Perform a semi join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_semi(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Semi),
        None,
    )
    .unwrap_or(DataFrame::default())
}

/// Perform an anti join on two dataframes.
///
/// # Errors
///
/// If the join fails (because the column names do not exist, for example), an empty
/// dataframe is returned.
pub fn join_anti(df1: &DataFrame, df2: &DataFrame) -> DataFrame {
    df1.join(
        df2,
        ["src_ip", "dst_ip", "seq_num"],
        ["dst_ip", "src_ip", "seq_num"],
        JoinArgs::new(JoinType::Anti),
        None,
    )
    .unwrap_or(DataFrame::default())
}
