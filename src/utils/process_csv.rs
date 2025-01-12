use std::path::PathBuf;

use polars::{
    io::SerReader,
    prelude::{CsvReadOptions, DataFrame},
};

/// Reads a CSV file into a Polars DataFrame.
///
/// # Errors
///
/// If there is an error while reading the file, an empty DataFrame is returned.
pub fn get_csv(path: PathBuf) -> DataFrame {
    match CsvReadOptions::default()
        .with_has_header(true)
        .try_into_reader_with_file_path(Some(path))
    {
        Ok(csv_reader) => csv_reader.finish().unwrap_or(DataFrame::empty()),
        Err(_) => DataFrame::empty(),
    }
}
