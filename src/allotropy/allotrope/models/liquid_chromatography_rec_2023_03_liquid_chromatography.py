# generated by datamodel-codegen:
#   filename:  liquid-chromatography.json
#   timestamp: 2024-01-12T14:18:37+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.components.liquid_chromatography import (
    PeakList,
)
from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCentimeter,
    TQuantityValueCubicMillimeter,
    TQuantityValueHertz,
    TQuantityValueMicrometer,
    TQuantityValueMillimeter,
    TQuantityValueNanometer,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TDatacube,
    TDateTimeValue,
    TQuantityValue,
    TStringValue,
)


@dataclass
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    field_index: int | None = None


@dataclass
class DeviceSystemDocument:
    asset_management_identifier: TStringValue
    description: Any | None = None
    brand_name: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    pump_model_number: TStringValue | None = None
    detector_model_number: TStringValue | None = None
    device_document: list[DeviceDocumentItem] | None = None


@dataclass
class ChromatographyColumnDocument:
    chromatography_column_particle_size: TQuantityValueMicrometer | None = None
    chromatography_column_chemistry_type: TStringValue | None = None
    chromatography_column_serial_number: TStringValue | None = None
    column_inner_diameter: TQuantityValueMillimeter | None = None
    product_manufacturer: TStringValue | None = None
    chromatography_column_length: TQuantityValueCentimeter | None = None
    chromatography_column_part_number: TStringValue | None = None


@dataclass
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    model_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    detection_type: TStringValue | None = None
    electronic_absorbance_wavelength_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_wavelength_setting: TQuantityValueNanometer | None = None
    detector_offset_setting: TQuantityValue | None = None
    detector_sampling_rate_setting: TQuantityValueHertz | None = None
    field_index: int | None = None


@dataclass
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]


@dataclass
class SampleDocument:
    sample_identifier: TStringValue
    description: Any | None = None
    written_name: TStringValue | None = None


@dataclass
class InjectionDocument:
    autosampler_injection_volume_setting__chromatography_: TQuantityValueCubicMillimeter
    injection_identifier: TStringValue
    injection_time: TDateTimeValue


@dataclass
class ProcessedDataDocument:
    peak_list: PeakList | None = None


@dataclass
class DiagnosticTraceDocumentItem:
    description: Any
    data_cube: TDatacube | None = None


@dataclass
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None


@dataclass
class MeasurementDocumentItem:
    chromatography_column_document: ChromatographyColumnDocument
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    injection_document: InjectionDocument
    detection_type: TStringValue
    chromatogram_data_cube: TDatacube
    measurement_identifier: TStringValue | None = None
    three_dimensional_ultraviolet_spectrum_data_cube: TDatacube | None = None
    processed_data_document: ProcessedDataDocument | None = None
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None


@dataclass
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocumentItem]


@dataclass
class LiquidChromatographyDocumentItem:
    analyst: TStringValue
    measurement_aggregate_document: MeasurementAggregateDocument
    submitter: TStringValue | None = None


@dataclass
class LiquidChromatographyAggregateDocument:
    device_system_document: DeviceSystemDocument
    liquid_chromatography_document: list[LiquidChromatographyDocumentItem]


@dataclass
class Model:
    liquid_chromatography_aggregate_document: LiquidChromatographyAggregateDocument | None = None
    manifest: str = "http://purl.allotrope.org/manifests/liquid-chromatography/REC/2023/03/liquid-chromatography.manifest"
