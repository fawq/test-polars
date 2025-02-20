# Define the possible variants
$variants = @(
    "--python"
    "--python-module"
    "--rust"
    "--rust-release"
    "--all"
)

# Check if the correct number of arguments is provided
if ($args.Count -ne 3) {
    Write-Host "Usage: $PSCommandPath [-python|-python-module|-rust|-rust-release|-all] <request.csv> <response.csv>"
    exit 1
}

# Get the variant and CSV file paths from the arguments
$variant = $args[0]
$requestCsv = $args[1]
$responseCsv = $args[2]

# Run the corresponding command based on the variant
switch ($variant) {
    "--python" {
        # Run using uv with Python
        uv run test-polars $requestCsv $responseCsv
    }
    "--python-module" {
        # Run using uv with Python module
        uv run -m test_polars $requestCsv $responseCsv
    }
    "--rust" {
        # Run using cargo development mode
        cargo run $requestCsv $responseCsv
    }
    "--rust-release" {
        # Run using cargo release mode
        cargo run --release $requestCsv $responseCsv
    }
    "--all" {
        # Run all variants
        uv run test-polars $requestCsv $responseCsv
        uv run -m test_polars $requestCsv $responseCsv
        cargo run $requestCsv $responseCsv
        cargo run --release $requestCsv $responseCsv
    }
    default {
        Write-Host "Invalid variant: $variant"
        exit 1
    }
}