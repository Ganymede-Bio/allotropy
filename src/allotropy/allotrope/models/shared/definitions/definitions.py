from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Union

from allotropy.exceptions import AllotropeConversionError


@dataclass
class TBooleanValueItem:
    field_type: TClass
    value: bool


@dataclass
class TDateTimeValueItem:
    field_type: TClass
    value: str


@dataclass
class TStringValueItem:
    value: str
    field_type: str


TBooleanArray = list[bool]
TBooleanOrNullArray = list[bool | None]
TBooleanValue = Union[bool, TBooleanValueItem]
TClass = str
TDateTimeValue = Union[str, TDateTimeValueItem]
# TODO(brian): inline this
TDateTimeStampValue = TDateTimeValue
TNumberArray = list[float]
TNumberOrNullArray = list[float | None]
TStringArray = list[str]
TStringOrNullArray = list[str | None]
TStringValue = Union[str, TStringValueItem]
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


class InvalidJsonFloat(Enum):
    """Enum to represent valid float values that are invalid in JSON.

    Values were automatically generated by schema generation code."""

    NaN = "NaN"
    field_Infinity = "+Infinity"
    field_Infinity_1 = "-Infinity"


JsonFloat = Union[float, InvalidJsonFloat]


@dataclass
class TQuantityValue:
    value: JsonFloat
    unit: TUnit
    has_statistic_datum_role: TStatisticDatumRole | None = None
    field_type: TClass | None = None


@dataclass
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


@dataclass
class TFunction:
    type: Type | None = Type.linear
    start: float | None = 1
    length: float | None = None
    incr: float | None = 1


@dataclass
class TDatacubeComponent:
    field_componentDatatype: FieldComponentDatatype
    concept: TClass
    unit: TUnit | None = None
    scale: Scale | None = None
    field_asm_fill_value: str | float | int | bool | None = None


TDimensionArray = Union[TNumberArray, TBooleanArray, TStringArray]


TMeasureArray = Union[TNumberOrNullArray, TBooleanOrNullArray, TStringOrNullArray]


@dataclass
class TDatacubeStructure:
    dimensions: list[TDatacubeComponent]
    measures: list[TDatacubeComponent]


"""
TODO: datamodel-codegen cannot properly generate the models for TDatacubeData with the
oneOf{measures, points} constraint. I can't figure out how to do it correctly right now either.
We need to either figure this out and file a bug with datamodel-codegen or fix the schema.

@dataclass
class TDimensionData:
    dimensions: List[Union[TDimensionArray, TFunction]]


@dataclass
class TMeasureDatum:
    measures: List[TMeasureArray]


@dataclass
class TMeasureDatum1:
    points: List[TTupleData]


TMeasureData = Union[TMeasureDatum, TMeasureDatum1]


@dataclass
class TDatacubeData(TDimensionData):
    pass
"""


@dataclass
class TDatacubeData:
    dimensions: list[TDimensionArray | TFunction]
    measures: list[TMeasureArray] | None = None
    points: list[TTupleData] | None = None

    def __post_init__(self) -> None:
        # Logic for enforcing oneOf
        if not (self.measures is None) ^ (self.points is None):
            error = "Exactly one of measures or points must be set on a datacube."
            raise AllotropeConversionError(error)


@dataclass
class TDatacube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None
