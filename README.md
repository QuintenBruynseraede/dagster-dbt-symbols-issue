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

This shows the following error:

```
dagster._core.errors.DagsterInvalidDefinitionError: "test_source_table_with_dollarsign_$" is not a valid name in Dagster. Names must be in regex ^[A-Za-z0-9_]+$.
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_grpc/server.py", line 408, in __init__
    self._loaded_repositories: Optional[LoadedRepositories] = LoadedRepositories(
                                                              ~~~~~~~~~~~~~~~~~~^
        loadable_target_origin,
        ^^^^^^^^^^^^^^^^^^^^^^^
        self._entry_point,
        ^^^^^^^^^^^^^^^^^^
        self._container_image,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_grpc/server.py", line 242, in __init__
    loadable_targets = get_loadable_targets(
        loadable_target_origin.python_file,
    ...<3 lines>...
        loadable_target_origin.attribute,
    )
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_grpc/utils.py", line 40, in get_loadable_targets
    else loadable_targets_from_python_file(python_file, working_directory)
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/workspace/autodiscovery.py", line 26, in loadable_targets_from_python_file
    loaded_module = load_python_file(python_file, working_directory)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/code_pointer.py", line 83, in load_python_file
    return import_module_from_path(module_name, python_file)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_seven/__init__.py", line 48, in import_module_from_path
    spec.loader.exec_module(module)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
  File "<frozen importlib._bootstrap_external>", line 1022, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/dbt_assets.py", line 7, in <module>
    @dbt_assets(manifest=Path.cwd() / "target" / "manifest.json")
     ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster_dbt/asset_decorator.py", line 350, in inner
    asset_definition = multi_asset(
    ...<10 lines>...
        backfill_policy=backfill_policy,
    )(fn)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/decorators/asset_decorator.py", line 781, in inner
    op = _Op(
    ...<11 lines>...
        code_version=code_version,
    )(fn)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/decorators/op_decorator.py", line 127, in __call__
    op_def = OpDefinition.dagster_internal_init(
        name=self.name,
    ...<9 lines>...
        version=None,  # code_version has replaced version
    )
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/op_definition.py", line 205, in dagster_internal_init
    return OpDefinition(
        compute_fn=compute_fn,
    ...<9 lines>...
        code_version=code_version,
    )
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/decorator_utils.py", line 203, in wrapped_with_pre_call_fn
    return fn(*args, **kwargs)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/op_definition.py", line 139, in __init__
    inp.to_definition(name) for name, inp in sorted(ins.items(), key=lambda inp: inp[0])
    ~~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/input.py", line 504, in to_definition
    return InputDefinition(
        name=name,
    ...<6 lines>...
        input_manager_key=self.input_manager_key,
    )
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/decorator_utils.py", line 203, in wrapped_with_pre_call_fn
    return fn(*args, **kwargs)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/decorator_utils.py", line 203, in wrapped_with_pre_call_fn
    return fn(*args, **kwargs)
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/input.py", line 114, in __init__
    self._name = check_valid_name(name, allow_list=["config"])
                 ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/utils.py", line 64, in check_valid_name
    check_valid_chars(name)
    ~~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/quinten.bruynseraede/git/dagster-dbt-symbols-issue/.venv/lib/python3.13/site-packages/dagster/_core/definitions/utils.py", line 72, in check_valid_chars
    raise DagsterInvalidDefinitionError(
    ...<2 lines>...
    )
```
