"""Constants file for Agilent OpenLab CDS Adapter"""

from allotropy.allotrope.models.shared.components.plate_reader import SampleRoleType

DISPLAY_NAME = "Waters Acquity"
PRODUCT_MANUFACTURER = "Waters"
SAMPLE_ROLE_TYPE = {
    "Blank": SampleRoleType.blank_role.value,
    "Sample": SampleRoleType.sample_role.value,
}
