from pathlib import Path
from dagster_dbt import DbtCliResource, dbt_assets

import dagster as dg


@dbt_assets(manifest=Path.cwd() / "target" / "manifest.json")
def dbt_project_assets(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


defs = dg.Definitions(assets=[dbt_project_assets])
