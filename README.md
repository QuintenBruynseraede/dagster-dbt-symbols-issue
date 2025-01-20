# dagster-dbt-symbols-issue

Prereq:

- Have a dbt profile called "test" in ~/.dbt/profiles.yml.
  I used:

  ```
  test:
  target: dev
  outputs:
    dev:
      type: "snowflake"
      account: "12341234"
      user: "user"
      authenticator: "externalbrowser"
      role: "role"
      warehouse: "wh"
      database: "db"
      schema: "schema"
  ```

  To run:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
dbt parse
python3 -m dagster dev -f dbt_assets.py
```
