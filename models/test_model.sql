select count(1) as cnt
from {{ source("test_source", "table_with_dollarsign_$") }}

