"""ThermostatUserInterfaceConfiguration cluster definition (auto-generated, DO NOT edit)."""

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
class ThermostatUserInterfaceConfiguration(Cluster):
    id: typing.ClassVar[int] = 0x00000204

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="temperatureDisplayMode", Tag=0x00000000, Type=ThermostatUserInterfaceConfiguration.Enums.TemperatureDisplayModeEnum),
                ClusterObjectFieldDescriptor(Label="keypadLockout", Tag=0x00000001, Type=ThermostatUserInterfaceConfiguration.Enums.KeypadLockoutEnum),
                ClusterObjectFieldDescriptor(Label="scheduleProgrammingVisibility", Tag=0x00000002, Type=typing.Optional[ThermostatUserInterfaceConfiguration.Enums.ScheduleProgrammingVisibilityEnum]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    temperatureDisplayMode: ThermostatUserInterfaceConfiguration.Enums.TemperatureDisplayModeEnum = 0
    keypadLockout: ThermostatUserInterfaceConfiguration.Enums.KeypadLockoutEnum = 0
    scheduleProgrammingVisibility: typing.Optional[ThermostatUserInterfaceConfiguration.Enums.ScheduleProgrammingVisibilityEnum] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class TemperatureDisplayModeEnum(MatterIntEnum):
            kCelsius = 0x00
            kFahrenheit = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class KeypadLockoutEnum(MatterIntEnum):
            kNoLockout = 0x00
            kLockout1 = 0x01
            kLockout2 = 0x02
            kLockout3 = 0x03
            kLockout4 = 0x04
            kLockout5 = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

        class ScheduleProgrammingVisibilityEnum(MatterIntEnum):
            kScheduleProgrammingPermitted = 0x00
            kScheduleProgrammingDenied = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Attributes:
        TemperatureDisplayMode = _attr(__module__, __qualname__, "TemperatureDisplayMode", 0x00000204, 0x00000000, "ThermostatUserInterfaceConfiguration.Enums.TemperatureDisplayModeEnum", 0)

        KeypadLockout = _attr(__module__, __qualname__, "KeypadLockout", 0x00000204, 0x00000001, "ThermostatUserInterfaceConfiguration.Enums.KeypadLockoutEnum", 0)

        ScheduleProgrammingVisibility = _attr(__module__, __qualname__, "ScheduleProgrammingVisibility", 0x00000204, 0x00000002, "typing.Optional[ThermostatUserInterfaceConfiguration.Enums.ScheduleProgrammingVisibilityEnum]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000204, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000204, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000204, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000204, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000204, 0x0000FFFD, "uint", 0)
