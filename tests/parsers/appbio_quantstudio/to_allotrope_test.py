from allotropy.parser_factory import Vendor
from tests.to_allotrope_test import ParserTest


class TestParser(ParserTest):
    VENDOR = Vendor.APPBIO_QUANTSTUDIO
    OVERWRITE_ON_FAILURE = True
