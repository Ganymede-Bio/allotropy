# generated by datamodel-codegen:
#   filename:  liquid-chromatography.schema.json
#   timestamp: 2025-01-13T17:54:16+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from allotropy.allotrope.models.shared.definitions.custom import (
    TQuantityValueCentimeter,
    TQuantityValueCounts,
    TQuantityValueCountsTimesSecond,
    TQuantityValueCubicMillimeter,
    TQuantityValueHertz,
    TQuantityValueMicrometer,
    TQuantityValueMilliAbsorbanceUnit,
    TQuantityValueMilliAbsorbanceUnitTimesMilliliter,
    TQuantityValueMilliAbsorbanceUnitTimesSecond,
    TQuantityValueMilliliter,
    TQuantityValueMillimeter,
    TQuantityValueMillivolt,
    TQuantityValueMillivoltTimesSecond,
    TQuantityValueNanoCoulomb,
    TQuantityValueNanoCoulombTimesSecond,
    TQuantityValueNanometer,
    TQuantityValueNumber,
    TQuantityValuePercent,
    TQuantityValuePicoAmpere,
    TQuantityValuePicoAmpereTimesSecond,
    TQuantityValueSecondTime,
    TQuantityValueUnitless,
)
from allotropy.allotrope.models.shared.definitions.definitions import (
    TClass,
    TDatacube,
    TDatacubeData,
    TDatacubeStructure,
    TDateTimeStampValue,
    TDateTimeValue,
    TQuantityValue,
    TStringValue,
)


@dataclass(kw_only=True)
class DiagnosticTraceDocumentItem:
    description: Any


@dataclass(kw_only=True)
class DiagnosticTraceAggregateDocument:
    diagnostic_trace_document: list[DiagnosticTraceDocumentItem] | None = None


@dataclass(kw_only=True)
class AdmCoreREC202309ManifestSchema:
    vocabulary: list[str]
    json_schemas: list[str]
    field_id: str | None = None
    field_type: str | None = None
    shapes: list[str] | None = None


@dataclass(kw_only=True)
class StatisticsDocumentItem:
    statistical_feature: TClass


@dataclass(kw_only=True)
class StatisticsAggregateDocument:
    statistics_document: list[StatisticsDocumentItem] | None = None


@dataclass(kw_only=True)
class DataSystemDocument:
    ASM_converter_name: TStringValue | None = None
    ASM_converter_version: TStringValue | None = None
    data_system_instance_identifier: TStringValue | None = None
    file_name: TStringValue | None = None
    software_name: TStringValue | None = None
    software_version: TStringValue | None = None
    UNC_path: TStringValue | None = None


@dataclass(kw_only=True)
class DeviceDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class DeviceSystemDocument:
    asset_management_identifier: TStringValue
    description: Any | None = None
    brand_name: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    device_identifier: TStringValue | None = None
    model_number: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    device_document: list[DeviceDocumentItem] | None = None
    pump_model_number: TStringValue | None = None
    detector_model_number: TStringValue | None = None


@dataclass(kw_only=True)
class DeviceControlDocumentItem:
    device_type: TStringValue
    device_identifier: TStringValue | None = None
    detection_type: TStringValue | None = None
    product_manufacturer: TStringValue | None = None
    brand_name: TStringValue | None = None
    equipment_serial_number: TStringValue | None = None
    model_number: TStringValue | None = None
    firmware_version: TStringValue | None = None
    start_time_setting: TDateTimeStampValue | None = None
    field_index: int | None = None
    detector_offset_setting: TQuantityValue | None = None
    detector_sampling_rate_setting: TQuantityValueHertz | None = None
    detector_wavelength_setting: TQuantityValueNanometer | None = None
    detector_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_wavelength_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_bandwidth_setting: TQuantityValueNanometer | None = None
    electronic_absorbance_reference_bandwidth_setting: TQuantityValueNanometer | None = (
        None
    )
    electronic_absorbance_reference_wavelength_setting: TQuantityValueNanometer | None = (
        None
    )
    solvent_concentration_data_cube: SolventConcentrationDataCube | None = None
    pre_column_pressure_data_cube: PreColumnPressureDataCube | None = None
    post_column_pressure_data_cube: PostColumnPressureDataCube | None = None
    sample_pressure_data_cube: SamplePressureDataCube | None = None
    system_pressure_data_cube: SystemPressureDataCube | None = None
    excitation_wavelength_setting: TQuantityValueNanometer | None = None
    excitation_bandwidth_setting: TQuantityValueNanometer | None = None
    total_measurement_time_setting: TQuantityValueSecondTime | None = None
    read_interval_setting: TQuantityValueSecondTime | None = None
    number_of_scans_setting: TQuantityValueNumber | None = None
    system_flow_rate_data_cube: SystemFlowRateDataCube | None = None
    sample_flow_rate_data_cube: SampleFlowRateDataCube | None = None
    temperature_profile_data_cube: TemperatureProfileDataCube | None = None


@dataclass(kw_only=True)
class DeviceControlAggregateDocument:
    device_control_document: list[DeviceControlDocumentItem]


@dataclass(kw_only=True)
class SampleDocument:
    sample_identifier: TStringValue
    description: Any | None = None
    batch_identifier: TStringValue | None = None
    sample_role_type: TClass | None = None
    written_name: TStringValue | None = None


@dataclass(kw_only=True)
class Peak:
    peak_end: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    identifier: TStringValue | None = None
    relative_peak_height: TQuantityValuePercent | None = None
    written_name: TStringValue | None = None
    peak_height: TQuantityValue | TQuantityValueCounts | TQuantityValueMilliAbsorbanceUnit | TQuantityValueMillivolt | TQuantityValueNanoCoulomb | TQuantityValuePicoAmpere | None = (
        None
    )
    capacity_factor__chromatography_: TQuantityValueUnitless | None = None
    peak_area: TQuantityValue | TQuantityValueCountsTimesSecond | TQuantityValueMilliAbsorbanceUnitTimesMilliliter | TQuantityValueMilliAbsorbanceUnitTimesSecond | TQuantityValueMillivoltTimesSecond | TQuantityValueNanoCoulombTimesSecond | TQuantityValuePicoAmpereTimesSecond | None = (
        None
    )
    relative_peak_area: TQuantityValuePercent | None = None
    retention_time: TQuantityValueSecondTime | None = None
    retention_volume: TQuantityValueMilliliter | None = None
    peak_start: TQuantityValueMilliliter | TQuantityValueSecondTime | None = None
    peak_selectivity__chromatography_: TQuantityValueUnitless | None = None
    peak_index: TStringValue | None = None
    chromatographic_peak_resolution: TQuantityValueUnitless | None = None
    field_index: int | None = None
    chromatographic_peak_resolution_using_baseline_peak_widths: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_peak_width_at_half_height__JP14_: TQuantityValueUnitless | None = (
        None
    )
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
    asymmetry_factor_measured_at_baseline: TQuantityValueUnitless | None = None
    chromatographic_peak_asymmetry_factor: TQuantityValueUnitless | None = None
    chromatographic_peak_resolution_using_peak_width_at_half_height: TQuantityValueUnitless | None = (
        None
    )
    chromatographic_peak_resolution_using_statistical_moments: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates__chromatography_: TQuantityValueUnitless | None = None
    number_of_theoretical_plates_measured_at_60_7___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_32_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_13_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_measured_at_4_4___of_peak_height: TQuantityValueUnitless | None = (
        None
    )
    number_of_theoretical_plates_by_tangent_method: TQuantityValueUnitless | None = None
    chromatogram_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class PeakList:
    peak: list[Peak] | None = None


@dataclass(kw_only=True)
class ChromatographyColumnDocument:
    chromatography_column_part_number: TStringValue | None = None
    chromatography_column_serial_number: TStringValue | None = None
    chromatography_column_length: TQuantityValueCentimeter | None = None
    column_inner_diameter: TQuantityValueMillimeter | None = None
    chromatography_column_chemistry_type: TStringValue | None = None
    chromatography_column_particle_size: TQuantityValueMicrometer | None = None
    product_manufacturer: TStringValue | None = None


@dataclass(kw_only=True)
class InjectionDocument:
    autosampler_injection_volume_setting__chromatography_: TQuantityValueCubicMillimeter | None = (
        None
    )
    injection_identifier: TStringValue | None = None
    injection_time: TDateTimeValue | None = None


@dataclass(kw_only=True)
class DataSourceDocumentItem:
    data_source_identifier: TStringValue
    data_source_feature: TStringValue
    field_index: int | None = None


@dataclass(kw_only=True)
class DataSourceAggregateDocument:
    data_source_document: list[DataSourceDocumentItem]


@dataclass(kw_only=True)
class ProcessedDataAggregateDocument:
    processed_data_document: list[ProcessedDataDocumentItem]


@dataclass(kw_only=True)
class ProcessedDataDocumentItem:
    data_processing_document: dict[str, Any] | None = None
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    processed_data_identifier: TStringValue | None = None
    field_index: int | None = None
    peak_list: PeakList | None = None
    derived_column_pressure_data_cube: DerivedColumnPressureDataCube | None = None
    chromatogram_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class CalculatedDataDocumentItem:
    calculated_data_name: TStringValue
    calculated_result: TQuantityValue
    data_source_aggregate_document: DataSourceAggregateDocument | None = None
    calculated_data_identifier: TStringValue | None = None
    calculation_description: TStringValue | None = None
    field_index: int | None = None


@dataclass(kw_only=True)
class CalculatedDataAggregateDocument:
    calculated_data_document: list[CalculatedDataDocumentItem]


@dataclass(kw_only=True)
class ChromatogramDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class SystemFlowRateDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class SampleFlowRateDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class TemperatureProfileDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class SolventConcentrationDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class PreColumnPressureDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class PostColumnPressureDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class SamplePressureDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class SystemPressureDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class DerivedColumnPressureDataCube:
    label: str | None = None
    cube_structure: TDatacubeStructure | None = None
    data: TDatacubeData | None = None


@dataclass(kw_only=True)
class MeasurementDocument:
    device_control_aggregate_document: DeviceControlAggregateDocument
    sample_document: SampleDocument
    chromatography_column_document: ChromatographyColumnDocument
    measurement_time: TDateTimeStampValue | None = None
    measurement_identifier: TStringValue | None = None
    detection_type: TStringValue | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None
    injection_document: InjectionDocument | None = None
    chromatogram_data_cube: ChromatogramDataCube | TDatacube | None = None
    three_dimensional_ultraviolet_spectrum_data_cube: TDatacube | None = None
    electropherogram_data_cube: TDatacube | None = None
    fluorescence_emission_profile_data_cube: TDatacube | None = None
    mass_chromatogram_data_cube: TDatacube | None = None


@dataclass(kw_only=True)
class MeasurementAggregateDocument:
    measurement_document: list[MeasurementDocument]
    diagnostic_trace_aggregate_document: DiagnosticTraceAggregateDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class LiquidChromatographyDocumentItem:
    measurement_aggregate_document: MeasurementAggregateDocument
    analyst: TStringValue | None = None
    submitter: TStringValue | None = None


@dataclass(kw_only=True)
class LiquidChromatographyAggregateDocument:
    liquid_chromatography_document: list[LiquidChromatographyDocumentItem]
    data_system_document: DataSystemDocument | None = None
    device_system_document: DeviceSystemDocument | None = None
    processed_data_aggregate_document: ProcessedDataAggregateDocument | None = None
    calculated_data_aggregate_document: CalculatedDataAggregateDocument | None = None
    statistics_aggregate_document: StatisticsAggregateDocument | None = None


@dataclass(kw_only=True)
class Model:
    field_asm_manifest: AdmCoreREC202309ManifestSchema | str
    liquid_chromatography_aggregate_document: LiquidChromatographyAggregateDocument | None = (
        None
    )
