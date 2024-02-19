from __future__ import annotations

from dataclasses import dataclass

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValuePercent,
    TQuantityValueSecondTime,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TQuantityValue,
    TStringValue,
)
from allotropy.exceptions import AllotropeConversionError


@dataclass
class PeakItem:
    retention_time: TQuantityValueSecondTime
    peak_end: TQuantityValueSecondTime | None = None
    identifier: TStringValue | None = None
    relative_peak_height: TQuantityValuePercent | None = None
    written_name: TStringValue | None = None
    peak_height: TQuantityValue | None = None
    capacity_factor__chromatography_: TQuantityValueUnitless | None = None
    peak_area: TQuantityValue | None = None
    relative_peak_area: TQuantityValuePercent | None = None
    peak_start: TQuantityValueSecondTime | None = None
    peak_selectivity__chromatography_: TQuantityValueUnitless | None = None

    peak_width_at_4_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_13_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_32_4___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_60_7___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_half_height: TQuantityValueSecondTime | None = None
    peak_width_at_5___of_height: TQuantityValueSecondTime | None = None
    peak_width_at_baseline: TQuantityValueSecondTime | None = None
    peak_width_at_inflection: TQuantityValueSecondTime | None = None
    peak_width_at_10___of_height: TQuantityValueSecondTime | None = None
    peak_width: TQuantityValueSecondTime | None = None
    statistical_skew__chromatography_: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_5___height: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_10___height: TQuantityValueUnitless | None = None
    asymmetry_factor_squared_measured_at_10___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_squared_measured_at_4_4___height: TQuantityValueUnitless | None = (
        None
    )
    asymmetry_factor_measured_at_4_4___height: TQuantityValueUnitless | None = None
    chromatographic_peak_asymmetry_factor: TQuantityValueUnitless | None = None
    asymmetry_factor_measured_at_baseline: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_baseline_peak_widths: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_peak_width_at_half_height: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_statistical_moments: TQuantityValueUnitless | None = None
    number_of_theoretical_plates__chromatography_: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_60_7___of_peak_height: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_32_4___of_peak_height: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_13_4___of_peak_height: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_4_4___of_peak_height: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_by_tangent_method: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_by_peak_width_at_half_height: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_by_peak_width_at_half_height__JP14_: TQuantityValueUnitless | None = None

    def __post_init__(self) -> None:
        any_of_keys = [
            "peak_width_at_4_4___of_height",
            "peak_width_at_13_4___of_height",
            "peak_width_at_32_4___of_height",
            "peak_width_at_60_7___of_height",
            "peak_width_at_half_height",
            "peak_width_at_5___of_height",
            "peak_width_at_baseline",
            "peak_width_at_inflection",
            "peak_width_at_10___of_height",
            "peak_width",
            "statistical_skew__chromatography_",
            "asymmetry_factor_measured_at_5___height",
            "asymmetry_factor_measured_at_10___height",
            "asymmetry_factor_squared_measured_at_10___height",
            "asymmetry_factor_squared_measured_at_4_4___height",
            "asymmetry_factor_measured_at_4_4___height",
            "chromatographic_peak_asymmetry_factor",
            "asymmetry_factor_measured_at_baseline",
            "chromatographic_peak_resolution",
            "chromatographic_peak_resolution_using_baseline_peak_widths",
            "chromatographic_peak_resolution_using_peak_width_at_half_height",
            "chromatographic_peak_resolution_using_statistical_moments",
            "number_of_theoretical_plates__chromatography_",
            "number_of_theoretical_plates_measured_at_60_7___of_peak_height",
            "number_of_theoretical_plates_measured_at_32_4___of_peak_height",
            "number_of_theoretical_plates_measured_at_13_4___of_peak_height",
            "number_of_theoretical_plates_measured_at_4_4___of_peak_height",
            "number_of_theoretical_plates_by_tangent_method",
            "number_of_theoretical_plates_by_peak_width_at_half_height",
            "number_of_theoretical_plates_by_peak_width_at_half_height__JP14_",
        ]
        # Logic for enforcing anyOf
        if all(getattr(self, key) is None for key in any_of_keys):
            error = f"At least one of {any_of_keys} must be set on a peak."
            raise AllotropeConversionError(error)


@dataclass
class PeakList:
    peak: list[PeakItem] | None = None
