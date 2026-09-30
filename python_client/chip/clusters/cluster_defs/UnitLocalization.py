"""UnitLocalization cluster definition (auto-generated, DO NOT edit)."""

from __future__ import annotations

import typing
from dataclasses import dataclass, field
from enum import IntFlag

from ... import ChipUtility
from ...clusters.enum import MatterIntEnum
from ...tlv import float32, uint
from ..ClusterObjects import (Cluster, ClusterAttributeDescriptor, ClusterCommand, ClusterEvent, ClusterObject,
                              ClusterObjectDescriptor, ClusterObjectFieldDescriptor, _attr)
from ..Types import Nullable, NullValue


@dataclass
class UnitLocalization(Cluster):
    id: typing.ClassVar[int] = 0x0000002D

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="temperatureUnit", Tag=0x00000000, Type=typing.Optional[UnitLocalization.Enums.TempUnitEnum]),
                ClusterObjectFieldDescriptor(Label="supportedTemperatureUnits", Tag=0x00000001, Type=typing.Optional[typing.List[UnitLocalization.Enums.TempUnitEnum]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    temperatureUnit: typing.Optional[UnitLocalization.Enums.TempUnitEnum] = None
    supportedTemperatureUnits: typing.Optional[typing.List[UnitLocalization.Enums.TempUnitEnum]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class TempUnitEnum(MatterIntEnum):
            kFahrenheit = 0x00
            kCelsius = 0x01
            kKelvin = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

    class Bitmaps:
        class Feature(IntFlag):
            kTemperatureUnit = 0x1

    class Attributes:
        TemperatureUnit = _attr(__module__, __qualname__, "TemperatureUnit", 0x0000002D, 0x00000000, "typing.Optional[UnitLocalization.Enums.TempUnitEnum]", None)

        SupportedTemperatureUnits = _attr(__module__, __qualname__, "SupportedTemperatureUnits", 0x0000002D, 0x00000001, "typing.Optional[typing.List[UnitLocalization.Enums.TempUnitEnum]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000002D, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000002D, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000002D, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000002D, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000002D, 0x0000FFFD, "uint", 0)
