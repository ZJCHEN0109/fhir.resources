# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Count
Release: 2022Sep
Version: 5.0.0-ballot
Build ID: 1505a88
Last updated: 2022-09-10T04:52:37.223+10:00
"""
from pydantic import Field

from . import quantity

class Count(quantity.Quantity):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A measured or measurable amount.
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    resource_type = Field("Count", const=True)
    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Count`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "value", "comparator", "unit", "system", "code"]

