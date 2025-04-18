"""Maps the intermediate json to liquid chromatograhy mapper fields"""

import os
from typing import Any

from allotropy.allotrope.models.shared.definitions.definitions import (
    FieldComponentDatatype,
)
from allotropy.allotrope.schema_mappers.adm.liquid_chromatography.benchling._2023._09.liquid_chromatography import (
    DeviceControlDoc,
    Measurement,
    MeasurementGroup,
    Metadata,
)
from allotropy.allotrope.schema_mappers.data_cube import DataCube, DataCubeComponent
from allotropy.named_file_contents import NamedFileContents
from allotropy.parsers.constants import NOT_APPLICABLE
from allotropy.parsers.utils.uuids import random_uuid_str
from allotropy.parsers.utils.values import (
    assert_not_none,
    quantity_or_none,
)
from allotropy.parsers.waters_acquity import constants


def create_data_cube(
    label: str,
    dimension_value: list[float],
    measures_value: list[float],
    data_cube_component: DataCubeComponent,
) -> DataCube:
    return DataCube(
        label=label,
        structure_dimensions=[
            DataCubeComponent(
                type_=FieldComponentDatatype.double,
                concept="retention time",
                unit="s",
            ),
        ],
        structure_measures=[data_cube_component],
        dimensions=[dimension_value],
        measures=[measures_value],
    )


def create_metadata(
    intermediate_structured_data: dict[str, Any], named_file_contents: NamedFileContents
) -> Metadata:
    return Metadata(
        asset_management_identifier=NOT_APPLICABLE,
        analyst=intermediate_structured_data["chromatogram_data_info"].get("Operator"),
        detection_type=intermediate_structured_data["chromatogram_data_info"].get("Detector"),
        software_name=constants.SOFTWARE_NAME,
        file_name=os.path.basename(named_file_contents.original_file_path),
        data_system_instance_identifier=NOT_APPLICABLE,
        software_version=intermediate_structured_data["chromatogram_data_info"].get(
            "Generating Data System"
        ),
        product_manufacturer=constants.PRODUCT_MANUFACTURER,
        brand_name=constants.DISPLAY_NAME,
    )


def create_measurements(intermediate_structured_data: dict[str, Any]) -> list[Measurement]:
    injection_volume_name = [
        c
        for c in intermediate_structured_data["injection_info"].keys()
        if c.startswith("Injection Volume")
    ]

    return [
        Measurement(
            measurement_identifier=random_uuid_str(),
            processed_data_identifier=random_uuid_str(),
            injection_identifier=assert_not_none(
                intermediate_structured_data["injection_info"].get("Injection")
            ),
            injection_time=assert_not_none(
                (
                    intermediate_structured_data["injection_info"].get("Injection Date")
                    + " "
                    + intermediate_structured_data["injection_info"].get("Injection Time")
                ).strip()
            ),
            device_control_docs=[DeviceControlDoc(device_type="pump")],
            sample_identifier=intermediate_structured_data["injection_info"].get(
                "Injection Number"
            ),
            description=intermediate_structured_data["injection_info"].get("Comment"),
            location_identifier=intermediate_structured_data["injection_info"].get("Position"),
            injection_volume_setting=float(
                intermediate_structured_data["injection_info"].get(injection_volume_name[0])
            ),
        )
    ]


def create_measurement_groups(intermediate_structured_data: dict[str, Any]) -> MeasurementGroup:
    return MeasurementGroup(
        measurements=create_measurements(intermediate_structured_data),
        measurement_aggregate_custom_info={
            "analytical method identifier": intermediate_structured_data["injection_info"].get(
                "Processing Method"
            )
        },
    )
