# Test Polars

## How to run

```shell
uv run -m test_polars test/data/ip_request.csv test/data/ip_response.csv
```

```shell
cargo run --release test/data/ip_request.csv test/data/ip_response.csv
```

## Results

### Data

Full request dataframe: shape: (5, 5)

| src_ip  | dst_ip  | seq_num | index_request | comment_request                            |
| ---     | ---     | ---     | ---           | ---                                        |
| str     | str     | i64     | i64           | str                                        |
|---------|---------|---------|---------------|--------------------------------------------|
| A.A.A.A | A.A.A.B | 1       | 0             | One request from A to B                    |
| B.B.B.A | B.B.B.B | 2       | 1             | First request from A to B                  |
| B.B.B.A | B.B.B.B | 2       | 2             | Second request from A to B                 |
| C.C.C.A | C.C.C.B | 4       | 3             | One request from A to B with wrong seq_num |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B                    |

Full response dataframe: shape: (6, 5)

| src_ip  | dst_ip  | seq_num | index_response | comment_response                               |
| ---     | ---     | ---     | ---            | ---                                            |
| str     | str     | i64     | i64            | str                                            |
|---------|---------|---------|----------------|------------------------------------------------|
| A.A.A.B | A.A.A.A | 1       | 0              | One response from B to A                       |
| B.B.B.B | B.B.B.A | 2       | 1              | First response from B to A                     |
| B.B.B.B | B.B.B.A | 3       | 2              | Second response from B to A with wrong seq_num |
| C.C.C.C | C.C.C.A | 4       | 3              | One response from B to A with wrong seq_num    |
| D.D.D.B | D.D.D.A | 5       | 4              | First response from B to A                     |
| D.D.D.B | D.D.D.A | 5       | 5              | Second response from B to A                    |

### Joins

Inner: shape: (5, 7)

| src_ip  | dst_ip  | seq_num | index_request | comment_request            | index_response | comment_response            |
| ---     | ---     | ---     | ---           | ---                        | ---            | ---                         |
| str     | str     | i64     | i64           | str                        | i64            | str                         |
|---------|---------|---------|---------------|----------------------------|----------------|-----------------------------|
| A.A.A.A | A.A.A.B | 1       | 0             | One request from A to B    | 0              | One response from B to A    |
| B.B.B.A | B.B.B.B | 2       | 1             | First request from A to B  | 1              | First response from B to A  |
| B.B.B.A | B.B.B.B | 2       | 2             | Second request from A to B | 1              | First response from B to A  |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B    | 4              | First response from B to A  |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B    | 5              | Second response from B to A |

Outer: shape: (8, 10)

| src_ip  | dst_ip  | seq_num | index_request | comment_request                      | src_ip_right | dst_ip_right | seq_num_right | index_response | comment_response                     |
| ---     | ---     | ---     | ---           | ---                                  | ---          | ---          | ---           | ---            | ---                                  |
| str     | str     | i64     | i64           | str                                  | str          | str          | i64           | i64            | str                                  |
|---------|---------|---------|---------------|--------------------------------------|--------------|--------------|---------------|----------------|--------------------------------------|
| A.A.A.A | A.A.A.B | 1       | 0             | One request from A to B              | A.A.A.B      | A.A.A.A      | 1             | 0              | One response from B to A             |
| B.B.B.A | B.B.B.B | 2       | 1             | First request from A to B            | B.B.B.B      | B.B.B.A      | 2             | 1              | First response from B to A           |
| B.B.B.A | B.B.B.B | 2       | 2             | Second request from A to B           | B.B.B.B      | B.B.B.A      | 2             | 1              | First response from B to A           |
| null    | null    | null    | null          | null                                 | B.B.B.B      | B.B.B.A      | 3             | 2              | Second response from B to A with     |
|         |         |         |               |                                      |              |              |               |                | wrong seq_num                        |
| null    | null    | null    | null          | null                                 | C.C.C.C      | C.C.C.A      | 4             | 3              | One response from B to A with wrong  |
|         |         |         |               |                                      |              |              |               |                | seq_num                              |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B              | D.D.D.B      | D.D.D.A      | 5             | 4              | First response from B to A           |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B              | D.D.D.B      | D.D.D.A      | 5             | 5              | Second response from B to A          |
| C.C.C.A | C.C.C.B | 4       | 3             | One request from A to B with wrong   | null         | null         | null          | null           | null                                 |
|         |         |         |               | seq_num                              |              |              |               |                |                                      |

Left: shape: (6, 7)

| src_ip  | dst_ip  | seq_num | index_request | comment_request                            | index_response | comment_response            |
| ---     | ---     | ---     | ---           | ---                                        | ---            | ---                         |
| str     | str     | i64     | i64           | str                                        | i64            | str                         |
|---------|---------|---------|---------------|--------------------------------------------|----------------|-----------------------------|
| A.A.A.A | A.A.A.B | 1       | 0             | One request from A to B                    | 0              | One response from B to A    |
| B.B.B.A | B.B.B.B | 2       | 1             | First request from A to B                  | 1              | First response from B to A  |
| B.B.B.A | B.B.B.B | 2       | 2             | Second request from A to B                 | 1              | First response from B to A  |
| C.C.C.A | C.C.C.B | 4       | 3             | One request from A to B with wrong seq_num | null           | null                        |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B                    | 4              | First response from B to A  |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B                    | 5              | Second response from B to A |

Right: shape: (7, 7)

| index_request | comment_request            | src_ip  | dst_ip  | seq_num | index_response | comment_response                               |
| ---           | ---                        | ---     | ---     | ---     | ---            | ---                                            |
| i64           | str                        | str     | str     | i64     | i64            | str                                            |
|---------------|----------------------------|---------|---------|---------|----------------|------------------------------------------------|
| 0             | One request from A to B    | A.A.A.B | A.A.A.A | 1       | 0              | One response from B to A                       |
| 1             | First request from A to B  | B.B.B.B | B.B.B.A | 2       | 1              | First response from B to A                     |
| 2             | Second request from A to B | B.B.B.B | B.B.B.A | 2       | 1              | First response from B to A                     |
| null          | null                       | B.B.B.B | B.B.B.A | 3       | 2              | Second response from B to A with wrong seq_num |
| null          | null                       | C.C.C.C | C.C.C.A | 4       | 3              | One response from B to A with wrong seq_num    |
| 4             | One request from A to B    | D.D.D.B | D.D.D.A | 5       | 4              | First response from B to A                     |
| 4             | One request from A to B    | D.D.D.B | D.D.D.A | 5       | 5              | Second response from B to A                    |

Full: shape: (8, 10)

| src_ip  | dst_ip  | seq_num | index_request | comment_request                      | src_ip_right | dst_ip_right | seq_num_right | index_response | comment_response                     |
| ---     | ---     | ---     | ---           | ---                                  | ---          | ---          | ---           | ---            | ---                                  |
| str     | str     | i64     | i64           | str                                  | str          | str          | i64           | i64            | str                                  |
|---------|---------|---------|---------------|--------------------------------------|--------------|--------------|---------------|----------------|--------------------------------------|
| A.A.A.A | A.A.A.B | 1       | 0             | One request from A to B              | A.A.A.B      | A.A.A.A      | 1             | 0              | One response from B to A             |
| B.B.B.A | B.B.B.B | 2       | 1             | First request from A to B            | B.B.B.B      | B.B.B.A      | 2             | 1              | First response from B to A           |
| B.B.B.A | B.B.B.B | 2       | 2             | Second request from A to B           | B.B.B.B      | B.B.B.A      | 2             | 1              | First response from B to A           |
| null    | null    | null    | null          | null                                 | B.B.B.B      | B.B.B.A      | 3             | 2              | Second response from B to A with     |
|         |         |         |               |                                      |              |              |               |                | wrong seq_num                        |
| null    | null    | null    | null          | null                                 | C.C.C.C      | C.C.C.A      | 4             | 3              | One response from B to A with wrong  |
|         |         |         |               |                                      |              |              |               |                | seq_num                              |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B              | D.D.D.B      | D.D.D.A      | 5             | 4              | First response from B to A           |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B              | D.D.D.B      | D.D.D.A      | 5             | 5              | Second response from B to A          |
| C.C.C.A | C.C.C.B | 4       | 3             | One request from A to B with wrong   | null         | null         | null          | null           | null                                 |
|         |         |         |               | seq_num                              |              |              |               |                |                                      |

Semi: shape: (4, 5)

| src_ip  | dst_ip  | seq_num | index_request | comment_request            |
| ---     | ---     | ---     | ---           | ---                        |
| str     | str     | i64     | i64           | str                        |
|---------|---------|---------|---------------|----------------------------|
| A.A.A.A | A.A.A.B | 1       | 0             | One request from A to B    |
| B.B.B.A | B.B.B.B | 2       | 1             | First request from A to B  |
| B.B.B.A | B.B.B.B | 2       | 2             | Second request from A to B |
| D.D.D.A | D.D.D.B | 5       | 4             | One request from A to B    |

Anti: shape: (1, 5)

| src_ip  | dst_ip  | seq_num | index_request | comment_request                            |
| ---     | ---     | ---     | ---           | ---                                        |
| str     | str     | i64     | i64           | str                                        |
|---------|---------|---------|---------------|--------------------------------------------|
| C.C.C.A | C.C.C.B | 4       | 3             | One request from A to B with wrong seq_num |
