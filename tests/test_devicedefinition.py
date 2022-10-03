# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic.validators import bytes_validator  # noqa: F401
from fhir.resources import fhirtypes  # noqa: F401
from fhir.resources import devicedefinition


def impl_devicedefinition_1(inst):
    assert inst.id == "example"
    assert inst.identifier[0].value == "0"
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    assert inst.text.status == "generated"


def test_devicedefinition_1(base_settings):
    """No. 1 tests collection for DeviceDefinition.
    Test File: devicedefinition-example.json
    """
    filename = (
        base_settings["unittest_data_dir"] / "devicedefinition-example.json"
    )
    inst = devicedefinition.DeviceDefinition.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceDefinition" == inst.resource_type

    impl_devicedefinition_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceDefinition" == data["resourceType"]

    inst2 = devicedefinition.DeviceDefinition(**data)
    impl_devicedefinition_1(inst2)