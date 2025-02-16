#!/bin/bash

# Run all the possible variants.
#
# Usage: ./run.sh [--python|--python-module|--rust|--rust-release|--all] <request.csv> <response.csv>
#
# Examples:
#   ./run.sh --python test/data/request.csv test/data/response.csv
#   ./run.sh --python-module test/data/request.csv test/data/response.csv
#   ./run.sh --rust test/data/request.csv test/data/response.csv
#   ./run.sh --rust-release test/data/request.csv test/data/response.csv
#   ./run.sh --all test/data/request.csv test/data/response.csv
main() {
    if [ "$#" -ne 3 ]; then
        echo "Usage: $0 [--python|--python-module|--rust|--rust-release|--all] <request.csv> <response.csv>"
        exit 1
    fi

    if [ "$1" == "--python" ]; then
        uv run test-polars "$2" "$3"
    elif [ "$1" == "--python-module" ]; then
        uv run -m test_polars "$2" "$3"
    elif [ "$1" == "--rust" ]; then
        cargo run "$2" "$3"
    elif [ "$1" == "--rust-release" ]; then
        cargo run --release "$2" "$3"
    elif [ "$1" == "--all" ]; then
        uv run test-polars "$2" "$3"
        uv run -m test_polars "$2" "$3"
        cargo run "$2" "$3"
        cargo run --release "$2" "$3"
    fi
}

main "$@"