# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE DIRECTLY.
from dataclasses import dataclass

UNITLESS = "(unitless)"


@dataclass(frozen=True, kw_only=True)
class HasUnit:
    unit: str


@dataclass(frozen=True, kw_only=True)
class Cell(HasUnit):
    unit: str = "cell"


@dataclass(frozen=True, kw_only=True)
class Centimeter(HasUnit):
    unit: str = "cm"


@dataclass(frozen=True, kw_only=True)
class Counts(HasUnit):
    unit: str = "Counts"


@dataclass(frozen=True, kw_only=True)
class CountsPerMicroliter(HasUnit):
    unit: str = "Counts/μL"


@dataclass(frozen=True, kw_only=True)
class CountsPerMilliliter(HasUnit):
    unit: str = "Counts/mL"


@dataclass(frozen=True, kw_only=True)
class CountsPerSecond(HasUnit):
    unit: str = "Counts/s"


@dataclass(frozen=True, kw_only=True)
class CountsTimesSecond(HasUnit):
    unit: str = "Counts.s"


@dataclass(frozen=True, kw_only=True)
class CubicMillimeter(HasUnit):
    unit: str = "mm^3"


@dataclass(frozen=True, kw_only=True)
class Dalton(HasUnit):
    unit: str = "Da"


@dataclass(frozen=True, kw_only=True)
class DegreeCelsius(HasUnit):
    unit: str = "degC"


@dataclass(frozen=True, kw_only=True)
class GramPerLiter(HasUnit):
    unit: str = "g/L"


@dataclass(frozen=True, kw_only=True)
class Hertz(HasUnit):
    unit: str = "Hz"


@dataclass(frozen=True, kw_only=True)
class KiloDalton(HasUnit):
    unit: str = "kDa"


@dataclass(frozen=True, kw_only=True)
class MicrogramPerMicroliter(HasUnit):
    unit: str = "ug/µL"


@dataclass(frozen=True, kw_only=True)
class MicrogramPerMilliliter(HasUnit):
    unit: str = "ug/mL"


@dataclass(frozen=True, kw_only=True)
class Microliter(HasUnit):
    unit: str = "μL"


@dataclass(frozen=True, kw_only=True)
class MicroliterPerMinute(HasUnit):
    unit: str = "µL/min"


@dataclass(frozen=True, kw_only=True)
class Micrometer(HasUnit):
    unit: str = "µm"


@dataclass(frozen=True, kw_only=True)
class MilliAbsorbanceUnit(HasUnit):
    unit: str = "mAU"


@dataclass(frozen=True, kw_only=True)
class MilliAbsorbanceUnitTimesMilliliter(HasUnit):
    unit: str = "mAU.mL"


@dataclass(frozen=True, kw_only=True)
class MilliAbsorbanceUnitTimesSecond(HasUnit):
    unit: str = "mAU.s"


@dataclass(frozen=True, kw_only=True)
class MilliOsmolesPerKilogram(HasUnit):
    unit: str = "mosm/kg"


@dataclass(frozen=True, kw_only=True)
class MilliSecond(HasUnit):
    unit: str = "ms"


@dataclass(frozen=True, kw_only=True)
class MilligramPerLiter(HasUnit):
    unit: str = "mg/L"


@dataclass(frozen=True, kw_only=True)
class MilligramPerMilliliter(HasUnit):
    unit: str = "mg/mL"


@dataclass(frozen=True, kw_only=True)
class Milliliter(HasUnit):
    unit: str = "mL"


@dataclass(frozen=True, kw_only=True)
class MilliliterPerLiter(HasUnit):
    unit: str = "mL/L"


@dataclass(frozen=True, kw_only=True)
class MilliliterPerMinute(HasUnit):
    unit: str = "mL/min"


@dataclass(frozen=True, kw_only=True)
class Millimeter(HasUnit):
    unit: str = "mm"


@dataclass(frozen=True, kw_only=True)
class MillimeterOfMercury(HasUnit):
    unit: str = "mmHg"


@dataclass(frozen=True, kw_only=True)
class MillimolePerLiter(HasUnit):
    unit: str = "mmol/L"


@dataclass(frozen=True, kw_only=True)
class MillionCellsPerMilliliter(HasUnit):
    unit: str = "10^6 cells/mL"


@dataclass(frozen=True, kw_only=True)
class Millivolt(HasUnit):
    unit: str = "mV"


@dataclass(frozen=True, kw_only=True)
class MillivoltTimesSecond(HasUnit):
    unit: str = "mV.s"


@dataclass(frozen=True, kw_only=True)
class Molar(HasUnit):
    unit: str = "M"


@dataclass(frozen=True, kw_only=True)
class NanoCoulomb(HasUnit):
    unit: str = "nC"


@dataclass(frozen=True, kw_only=True)
class NanoCoulombTimesSecond(HasUnit):
    unit: str = "nC.s"


@dataclass(frozen=True, kw_only=True)
class NanogramPerMicroliter(HasUnit):
    unit: str = "ng/µL"


@dataclass(frozen=True, kw_only=True)
class NanogramPerMilliliter(HasUnit):
    unit: str = "ng/mL"


@dataclass(frozen=True, kw_only=True)
class Nanometer(HasUnit):
    unit: str = "nm"


@dataclass(frozen=True, kw_only=True)
class Nanomolar(HasUnit):
    unit: str = "nM"


@dataclass(frozen=True, kw_only=True)
class Number(HasUnit):
    unit: str = "#"


@dataclass(frozen=True, kw_only=True)
class NumberPerMicroliter(HasUnit):
    unit: str = "#/μL"


@dataclass(frozen=True, kw_only=True)
class OpticalDensity(HasUnit):
    unit: str = "OD"


@dataclass(frozen=True, kw_only=True)
class PH(HasUnit):
    unit: str = "pH"


@dataclass(frozen=True, kw_only=True)
class PartsPerBillion(HasUnit):
    unit: str = "ppb"


@dataclass(frozen=True, kw_only=True)
class PartsPerMillion(HasUnit):
    unit: str = "ppm"


@dataclass(frozen=True, kw_only=True)
class PerSecond(HasUnit):
    unit: str = "s^-1"


@dataclass(frozen=True, kw_only=True)
class Percent(HasUnit):
    unit: str = "%"


@dataclass(frozen=True, kw_only=True)
class PicoAmpere(HasUnit):
    unit: str = "pA"


@dataclass(frozen=True, kw_only=True)
class PicoAmpereTimesSecond(HasUnit):
    unit: str = "pA.s"


@dataclass(frozen=True, kw_only=True)
class PicogramPerMilliliter(HasUnit):
    unit: str = "pg/mL"


@dataclass(frozen=True, kw_only=True)
class RelativeFluorescenceUnit(HasUnit):
    unit: str = "RFU"


@dataclass(frozen=True, kw_only=True)
class RelativeFluorescenceUnitTimesMilliliter(HasUnit):
    unit: str = "RFU.mL"


@dataclass(frozen=True, kw_only=True)
class RelativeFluorescenceUnitTimesSecond(HasUnit):
    unit: str = "RFU.s"


@dataclass(frozen=True, kw_only=True)
class RelativeLightUnit(HasUnit):
    unit: str = "RLU"


@dataclass(frozen=True, kw_only=True)
class RelativeLightUnitTimesMilliliter(HasUnit):
    unit: str = "RLU.mL"


@dataclass(frozen=True, kw_only=True)
class RelativeLightUnitTimesSecond(HasUnit):
    unit: str = "RLU.s"


@dataclass(frozen=True, kw_only=True)
class ResonanceUnits(HasUnit):
    unit: str = "RU"


@dataclass(frozen=True, kw_only=True)
class SecondTime(HasUnit):
    unit: str = "s"


@dataclass(frozen=True, kw_only=True)
class SeimensPerMeter(HasUnit):
    unit: str = "S/m"


@dataclass(frozen=True, kw_only=True)
class SquareCentimetersPerGram(HasUnit):
    unit: str = "cm^2/g"


@dataclass(frozen=True, kw_only=True)
class SquareCentimetersPerMole(HasUnit):
    unit: str = "cm^2/mol"


@dataclass(frozen=True, kw_only=True)
class TODO(HasUnit):
    unit: str = "TODO"


@dataclass(frozen=True, kw_only=True)
class UnitPerLiter(HasUnit):
    unit: str = "U/L"


@dataclass(frozen=True, kw_only=True)
class Unitless(HasUnit):
    unit: str = UNITLESS
