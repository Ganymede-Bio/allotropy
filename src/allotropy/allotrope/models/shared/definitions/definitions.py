from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any

from allotropy.exceptions import AllotropeConversionError


@dataclass(kw_only=True)
class TBooleanValueItem:
    field_type: TClass
    value: bool


@dataclass(kw_only=True)
class TIntValueItem:
    value: int
    field_type: str


TIntValue = int | TIntValueItem
TIntegerValue = TIntValue


@dataclass(kw_only=True)
class TDoubleValueItem:
    value: float
    field_type: str


TDoubleValue = float | TDoubleValueItem
TFloatValue = TDoubleValue
TDecimalValue = TDoubleValue


@dataclass(kw_only=True)
class TDateTimeValueItem:
    field_type: TClass
    value: str


@dataclass(kw_only=True)
class TStringValueItem:
    value: str
    field_type: str


TBooleanArray = list[bool]
TBooleanOrNullArray = list[bool | None]
TBooleanValue = bool | TBooleanValueItem
TClass = str
TDateTimeValue = str | TDateTimeValueItem
TDateTimeStampValue = TDateTimeValue
TNumberArray = list[float]
TNumberOrNullArray = list[float | None]
TStringArray = list[str]
TStringOrNullArray = list[str | None]
TStringValue = str | TStringValueItem
TTupleData = list[float | bool | str | None]
TUnit = str


class TStatisticDatumRole(Enum):
    arithmetic_mean_role = "arithmetic mean role"
    median_role = "median role"
    relative_standard_deviation_role = "relative standard deviation role"
    skewness_role = "skewness role"
    standard_deviation_role = "standard deviation role"
    variance_role = "variance role"
    maximum_value_role = "maximum value role"
    minimum_value_role = "minimum value role"
    final_value_role = "final value role"
    coefficient_of_variation_role = "coefficient of variation role"
    robust_coefficient_of_variation_role = "robust coefficient of variation role"
    geometric_mean_role = "geometric mean role"
    percentile_role = "percentile role"
    median_absolute_deviation_percentile_role = (
        "median absolute deviation percentile role"
    )
    robust_standard_deviation_role = "robust standard deviation role"
    median_absolute_deviation_role = "median absolute deviation role"
    frequency_of_parent_role = "frequency of parent role"
    frequency_of_grandparent_role = "frequency of grandparent role"
    frequency_of_total_role = "frequency of total role"


class InvalidJsonFloat(Enum):
    """Enum to represent valid float values that are invalid in JSON.

    Values were automatically generated by schema generation code."""

    NaN = "NaN"
    field_Infinity = "+Infinity"
    field_Infinity_1 = "-Infinity"

    def __truediv__(self, other: Any) -> InvalidJsonFloat:
        # The logic here is that: NaN/Any = NaN, +Infinity/Any = +Infinity, -Infinity/Any = -Infinity
        return self


# For convenience
JsonFloat = float | InvalidJsonFloat
NaN = InvalidJsonFloat.NaN


@dataclass(frozen=True, kw_only=True)
class TQuantityValue:
    value: JsonFloat
    unit: TUnit
    has_statistic_datum_role: TStatisticDatumRole | None = None
    field_type: TClass | None = None


@dataclass(frozen=True, kw_only=True)
class TNullableQuantityValue:
    value: float | None
    unit: TUnit
    has_statistic_datum_role: TStatisticDatumRole | None = None
    field_type: TClass | None = None


class FieldComponentDatatype(Enum):
    double = "double"
    float = "float"
    decimal = "decimal"
    integer = "integer"
    byte = "byte"
    int = "int"
    short = "short"
    long = "long"
    string = "string"
    boolean = "boolean"
    dateTime = "dateTime"


class Scale(Enum):
    nominal = "nominal"
    ordinal = "ordinal"
    cardinal = "cardinal"
    interval = "interval"
    range = "range"


class Type(Enum):
    linear = "linear"
    logarithmic = "logarithmic"


@dataclass(kw_only=True)
class TFunction:
    type: Type | None = Type.linear
    start: float | None = 1
    length: float | None = None
    incr: float | None = 1


@dataclass(kw_only=True)
class TDatacubeComponent:
    field_componentDatatype: FieldComponentDatatype
    concept: TClass
    unit: TUnit | None = None
    scale: Scale | None = None
    field_asm_fill_value: str | float | int | bool | None = None


TDimensionArray = TNumberArray | TBooleanArray | TStringArray


TMeasureArray = TNumberOrNullArray | TBooleanOrNullArray | TStringOrNullArray


@dataclass(kw_only=True)
class TDatacubeStructure:
    dimensions: list[TDatacubeComponent]
    measures: list[TDatacubeComponent]


"""
TODO: datamodel-codegen cannot properly generate the models for TDatacubeData with the
oneOf{measures, points} constraint. I can't figure out how to do it correctly right now either.
We need to either figure this out and file a bug with datamodel-codegen or fix the schema.

@dataclass(kw_only=True)
class TDimensionData:
    dimensions: list[TDimensionArray | TFunction]


@dataclass(kw_only=True)
class TMeasureDatum:
    measures: list[TMeasureArray]


@dataclass(kw_only=True)
class TMeasureDatum1:
    points: list[TTupleData]


TMeasureData = TMeasureDatum | TMeasureDatum1


@dataclass(kw_only=True)
class TDatacubeData(TDimensionData):
    pass
"""


@dataclass(kw_only=True)
class TDatacubeData:
    dimensions: list[TDimensionArray | TFunction]
    measures: list[TMeasureArray] | None = None
    points: list[TTupleData] | None = None

    def __post_init__(self) -> None:
        # Logic for enforcing oneOf
        if not (self.measures is None) ^ (self.points is None):
            msg = "Exactly one of measures or points must be set on a datacube."
            raise AllotropeConversionError(msg)


@dataclass(kw_only=True)
class TDatacube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class OrderedItem:
    field_index: int | None = None
