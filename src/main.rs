mod utils;
use core::panic;
use std::env;
use std::path::PathBuf;

use crate::utils::process_csv::get_csv;
use crate::utils::process_data::{
    join_anti, join_full, join_inner, join_left, join_outer, join_right, join_semi,
};
use chrono::Local;
use env_logger::Builder;
use log::{LevelFilter, info};
use std::io::Write;

/// Configure logging.
fn setup_logging() {
    let mut builder = Builder::from_default_env();

    builder
        .format(|buf, record| {
            writeln!(
                buf,
                "{} - {} - {}",
                Local::now().format("%Y-%m-%d %H:%M:%S"),
                record.level(),
                record.args()
            )
        })
        .filter(None, LevelFilter::Info)
        .init();
}

/// Configure polars.
fn setup_polars() {
    unsafe {
        env::set_var("POLARS_FMT_MAX_ROWS", "200");
        env::set_var("POLARS_FMT_MAX_COLS", "200");
        env::set_var("POLARS_FMT_STR_LEN", "200");
    }
}

/// Run the main function.
fn main() {
    setup_logging();
    setup_polars();

    let args: Vec<String> = std::env::args().collect();

    if args.len() != 3 {
        panic!("Usage: {} <request.csv> <response.csv>", args[0]);
    }

    let df1 = get_csv(PathBuf::from(&args[1]));
    let df2 = get_csv(PathBuf::from(&args[2]));

    info!("Full request dataframe: {df1}");
    info!("Full response dataframe: {df2}");

    info!("Inner: {}", join_inner(&df1, &df2));
    info!("Outer: {}", join_outer(&df1, &df2));

    info!("Left: {}", join_left(&df1, &df2));
    info!("Right: {}", join_right(&df1, &df2));

    info!("Full: {}", join_full(&df1, &df2));

    info!("Semi: {}", join_semi(&df1, &df2));
    info!("Anti: {}", join_anti(&df1, &df2));
}
