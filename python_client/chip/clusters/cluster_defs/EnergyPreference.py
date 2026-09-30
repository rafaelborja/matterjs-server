"""EnergyPreference cluster definition (auto-generated, DO NOT edit)."""

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
class EnergyPreference(Cluster):
    id: typing.ClassVar[int] = 0x0000009B

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="energyBalances", Tag=0x00000000, Type=typing.Optional[typing.List[EnergyPreference.Structs.BalanceStruct]]),
                ClusterObjectFieldDescriptor(Label="currentEnergyBalance", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="energyPriorities", Tag=0x00000002, Type=typing.Optional[typing.List[EnergyPreference.Enums.EnergyPriorityEnum]]),
                ClusterObjectFieldDescriptor(Label="lowPowerModeSensitivities", Tag=0x00000003, Type=typing.Optional[typing.List[EnergyPreference.Structs.BalanceStruct]]),
                ClusterObjectFieldDescriptor(Label="currentLowPowerModeSensitivity", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    energyBalances: typing.Optional[typing.List[EnergyPreference.Structs.BalanceStruct]] = None
    currentEnergyBalance: typing.Optional[uint] = None
    energyPriorities: typing.Optional[typing.List[EnergyPreference.Enums.EnergyPriorityEnum]] = None
    lowPowerModeSensitivities: typing.Optional[typing.List[EnergyPreference.Structs.BalanceStruct]] = None
    currentLowPowerModeSensitivity: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class EnergyPriorityEnum(MatterIntEnum):
            kComfort = 0x00
            kSpeed = 0x01
            kEfficiency = 0x02
            kWaterConsumption = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Bitmaps:
        class Feature(IntFlag):
            kEnergyBalance = 0x1
            kLowPowerModeSensitivity = 0x2

    class Structs:
        @dataclass
        class BalanceStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="step", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="label", Tag=1, Type=typing.Optional[str]),
                    ])

            step: uint = 0
            label: typing.Optional[str] = None

    class Attributes:
        EnergyBalances = _attr(__module__, __qualname__, "EnergyBalances", 0x0000009B, 0x00000000, "typing.Optional[typing.List[EnergyPreference.Structs.BalanceStruct]]", None)

        CurrentEnergyBalance = _attr(__module__, __qualname__, "CurrentEnergyBalance", 0x0000009B, 0x00000001, "typing.Optional[uint]", None)

        EnergyPriorities = _attr(__module__, __qualname__, "EnergyPriorities", 0x0000009B, 0x00000002, "typing.Optional[typing.List[EnergyPreference.Enums.EnergyPriorityEnum]]", None)

        LowPowerModeSensitivities = _attr(__module__, __qualname__, "LowPowerModeSensitivities", 0x0000009B, 0x00000003, "typing.Optional[typing.List[EnergyPreference.Structs.BalanceStruct]]", None)

        CurrentLowPowerModeSensitivity = _attr(__module__, __qualname__, "CurrentLowPowerModeSensitivity", 0x0000009B, 0x00000004, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000009B, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000009B, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000009B, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000009B, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000009B, 0x0000FFFD, "uint", 0)
