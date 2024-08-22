import json
from pathlib import Path
from typing import Any


def unit_name_from_iri(unit_iri: str) -> str:
    return Path(unit_iri).name.split("#")[-1]


UNIT_STRING_OVERRIDES = {"(unitless)": "UNITLESS"}


def _update_unit_models(
    units_schema: dict[str, Any],
    units_models_path: Path,
    custom_models_path: Path,
) -> None:
    with open(units_models_path, "w") as f:
        f.write(
            """# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.
from dataclasses import dataclass

"""
        )
        for unit_name, override in UNIT_STRING_OVERRIDES.items():
            f.write(f'{override} = "{unit_name}"')

        f.write(
            """
@dataclass(frozen=True, kw_only=True)
class HasUnit:
    unit: str
"""
        )
        for unit_name, unit_schema in units_schema.items():
            unit = unit_schema["properties"]["unit"]["const"]
            unit_str = f"'{unit}'" if '"' in unit else f'"{unit}"'
            f.write(
                f"""


@dataclass(frozen=True, kw_only=True)
class {unit_name}(HasUnit):
    unit: str = {UNIT_STRING_OVERRIDES.get(unit, unit_str)}"""
            )

    with open(custom_models_path, "w") as f:
        f.write(
            """# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.
from dataclasses import dataclass

from allotropy.allotrope.models.shared.definitions.definitions import (
    TNullableQuantityValue,
    TQuantityValue,
)
from allotropy.allotrope.models.shared.definitions.units import (
"""
        )
        for unit_name in units_schema:
            f.write(f"    {unit_name},\n")
        f.write(")\n")

        for unit_name in units_schema:
            f.write(
                f"""

@dataclass(frozen=True, kw_only=True)
class TQuantityValue{unit_name}({unit_name}, TQuantityValue):
    pass


@dataclass(frozen=True, kw_only=True)
class TNullableQuantityValue{unit_name}({unit_name}, TNullableQuantityValue):
    pass
"""
            )


def _get_unit_schema(unit: str, unit_iri: str) -> dict[str, Any]:
    return {
        "properties": {
            "unit": {"type": "string", "const": unit, "$asm.unit-iri": unit_iri}
        },
        "required": ["unit"],
    }


def _get_quantity_value_schema(
    unit_name: str, prefix: str | None = ""
) -> dict[str, Any]:
    return {
        "allOf": [
            {"$ref": f"#/$defs/t{prefix}QuantityValue"},
            {"$ref": f"#/$defs/{unit_name}"},
        ]
    }


def update_unit_files(
    unit_to_iri: dict[str, str],
    unit_schemas_path: Path,
    units_models_path: Path,
    custom_schemas_path: Path,
    custom_models_path: Path,
) -> None:
    with open(unit_schemas_path) as f:
        units_schema = json.load(f)

    for unit, unit_iri in unit_to_iri.items():
        units_schema[unit_name_from_iri(unit_iri)] = _get_unit_schema(unit, unit_iri)

    units_schema = dict(sorted(units_schema.items()))
    with open(unit_schemas_path, "w") as f:
        json.dump(units_schema, f, indent=2, ensure_ascii=False)

    with open(unit_schemas_path) as f:
        units_schema = json.load(f)

    custom_schema = {}
    for unit_name in units_schema:
        custom_schema[f"tQuantityValue{unit_name}"] = _get_quantity_value_schema(
            unit_name
        )
        custom_schema[
            f"tNullableQuantityValue{unit_name}"
        ] = _get_quantity_value_schema(unit_name, "Nullable")

    with open(custom_schemas_path, "w") as f:
        json.dump(custom_schema, f, indent=2, ensure_ascii=False)

    _update_unit_models(units_schema, units_models_path, custom_models_path)
