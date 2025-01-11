# Test Polars

## How to run

```shell
uv run -m test_polars
```

## Results

### Data

Full request dataframe: shape: (5, 4)

| src_ip  | dst_ip  | seq_num | index_request |
| ---     | ---     | ---     | ---           |
| str     | str     | i64     | i64           |
|---------|---------|---------|---------------|
| A.A.A.A | A.A.A.B | 1       | 0             |
| B.B.B.A | B.B.B.B | 2       | 1             |
| B.B.B.A | B.B.B.B | 2       | 2             |
| C.C.C.A | C.C.C.B | 4       | 3             |
| D.D.D.A | D.D.D.B | 5       | 4             |

Full response dataframe: shape: (6, 4)

| src_ip  | dst_ip  | seq_num | index_response |
| ---     | ---     | ---     | ---            |
| str     | str     | i64     | i64            |
|---------|---------|---------|----------------|
| A.A.A.B | A.A.A.A | 1       | 0              |
| B.B.B.B | B.B.B.A | 2       | 1              |
| B.B.B.B | B.B.B.A | 3       | 2              |
| C.C.C.C | C.C.C.A | 4       | 3              |
| D.D.D.B | D.D.D.A | 5       | 4              |
| D.D.D.B | D.D.D.A | 5       | 5              |

### Joins

Inner: shape: (5, 5)

| src_ip  | dst_ip  | seq_num | index_request | index_response |
| ---     | ---     | ---     | ---           | ---            |
| str     | str     | i64     | i64           | i64            |
|---------|---------|---------|---------------|----------------|
| A.A.A.A | A.A.A.B | 1       | 0             | 0              |
| B.B.B.A | B.B.B.B | 2       | 1             | 1              |
| B.B.B.A | B.B.B.B | 2       | 2             | 1              |
| D.D.D.A | D.D.D.B | 5       | 4             | 4              |
| D.D.D.A | D.D.D.B | 5       | 4             | 5              |

Outer: shape: (8, 8)

| src_ip  | dst_ip  | seq_num | index_request | src_ip_right | dst_ip_right | seq_num_right | index_response |
| ---     | ---     | ---     | ---           | ---          | ---          | ---           | ---            |
| str     | str     | i64     | i64           | str          | str          | i64           | i64            |
|---------|---------|---------|---------------|--------------|--------------|---------------|----------------|
| A.A.A.A | A.A.A.B | 1       | 0             | A.A.A.B      | A.A.A.A      | 1             | 0              |
| B.B.B.A | B.B.B.B | 2       | 1             | B.B.B.B      | B.B.B.A      | 2             | 1              |
| B.B.B.A | B.B.B.B | 2       | 2             | B.B.B.B      | B.B.B.A      | 2             | 1              |
| null    | null    | null    | null          | B.B.B.B      | B.B.B.A      | 3             | 2              |
| null    | null    | null    | null          | C.C.C.C      | C.C.C.A      | 4             | 3              |
| D.D.D.A | D.D.D.B | 5       | 4             | D.D.D.B      | D.D.D.A      | 5             | 4              |
| D.D.D.A | D.D.D.B | 5       | 4             | D.D.D.B      | D.D.D.A      | 5             | 5              |
| C.C.C.A | C.C.C.B | 4       | 3             | null         | null         | null          | null           |

Left: shape: (6, 5)

| src_ip  | dst_ip  | seq_num | index_request | index_response |
| ---     | ---     | ---     | ---           | ---            |
| str     | str     | i64     | i64           | i64            |
|---------|---------|---------|---------------|----------------|
| A.A.A.A | A.A.A.B | 1       | 0             | 0              |
| B.B.B.A | B.B.B.B | 2       | 1             | 1              |
| B.B.B.A | B.B.B.B | 2       | 2             | 1              |
| C.C.C.A | C.C.C.B | 4       | 3             | null           |
| D.D.D.A | D.D.D.B | 5       | 4             | 4              |
| D.D.D.A | D.D.D.B | 5       | 4             | 5              |

Right: shape: (7, 5)

| index_request | src_ip  | dst_ip  | seq_num | index_response |
| ---           | ---     | ---     | ---     | ---            |
| i64           | str     | str     | i64     | i64            |
|---------------|---------|---------|---------|----------------|
| 0             | A.A.A.B | A.A.A.A | 1       | 0              |
| 1             | B.B.B.B | B.B.B.A | 2       | 1              |
| 2             | B.B.B.B | B.B.B.A | 2       | 1              |
| null          | B.B.B.B | B.B.B.A | 3       | 2              |
| null          | C.C.C.C | C.C.C.A | 4       | 3              |
| 4             | D.D.D.B | D.D.D.A | 5       | 4              |
| 4             | D.D.D.B | D.D.D.A | 5       | 5              |

Full: shape: (8, 8)

| src_ip  | dst_ip  | seq_num | index_request | src_ip_right | dst_ip_right | seq_num_right | index_response |
| ---     | ---     | ---     | ---           | ---          | ---          | ---           | ---            |
| str     | str     | i64     | i64           | str          | str          | i64           | i64            |
|---------|---------|---------|---------------|--------------|--------------|---------------|----------------|
| A.A.A.A | A.A.A.B | 1       | 0             | A.A.A.B      | A.A.A.A      | 1             | 0              |
| B.B.B.A | B.B.B.B | 2       | 1             | B.B.B.B      | B.B.B.A      | 2             | 1              |
| B.B.B.A | B.B.B.B | 2       | 2             | B.B.B.B      | B.B.B.A      | 2             | 1              |
| null    | null    | null    | null          | B.B.B.B      | B.B.B.A      | 3             | 2              |
| null    | null    | null    | null          | C.C.C.C      | C.C.C.A      | 4             | 3              |
| D.D.D.A | D.D.D.B | 5       | 4             | D.D.D.B      | D.D.D.A      | 5             | 4              |
| D.D.D.A | D.D.D.B | 5       | 4             | D.D.D.B      | D.D.D.A      | 5             | 5              |
| C.C.C.A | C.C.C.B | 4       | 3             | null         | null         | null          | null           |

Semi: shape: (4, 4)

| src_ip  | dst_ip  | seq_num | index_request |
| ---     | ---     | ---     | ---           |
| str     | str     | i64     | i64           |
|---------|---------|---------|---------------|
| A.A.A.A | A.A.A.B | 1       | 0             |
| B.B.B.A | B.B.B.B | 2       | 1             |
| B.B.B.A | B.B.B.B | 2       | 2             |
| D.D.D.A | D.D.D.B | 5       | 4             |

Anti: shape: (1, 4)

| src_ip  | dst_ip  | seq_num | index_request |
| ---     | ---     | ---     | ---           |
| str     | str     | i64     | i64           |
|---------|---------|---------|---------------|
| C.C.C.A | C.C.C.B | 4       | 3             |
