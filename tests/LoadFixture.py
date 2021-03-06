# Future Imports for py2/3 backwards compat.
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import json
import lxml
from os import path
from future import standard_library
standard_library.install_aliases()

_SCRIPT_PATH = path.dirname(path.abspath(__file__))
_FIXTURES_PATH = path.join(_SCRIPT_PATH, "..", "test_fixtures")

XML = 'xml'
JSON = 'json'


def LoadFixture(filename):
    _, _, fixture_type = filename.rpartition('.')
    fixture_path = path.join(_FIXTURES_PATH, filename)
    with open(fixture_path) as data_file:
        if fixture_type == JSON:
            return json.load(data_file)
        if fixture_type == XML:
            return lxml.etree.fromstring(data_file.read())
        raise ValueError("unknown fixture type")


def CreateEmptyFixture(fixture_type):
    if fixture_type == XML:
        return lxml.etree.fromstring('<_ />')
    raise ValueError("unknown fixture type")
