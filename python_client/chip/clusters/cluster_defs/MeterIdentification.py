"""MeterIdentification cluster definition (auto-generated, DO NOT edit)."""

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
from .Globals import Globals


@dataclass
class MeterIdentification(Cluster):
    id: typing.ClassVar[int] = 0x00000B06

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="meterType", Tag=0x00000000, Type=typing.Union[Nullable, MeterIdentification.Enums.MeterTypeEnum]),
                ClusterObjectFieldDescriptor(Label="pointOfDelivery", Tag=0x00000001, Type=typing.Union[Nullable, str]),
                ClusterObjectFieldDescriptor(Label="meterSerialNumber", Tag=0x00000002, Type=typing.Union[Nullable, str]),
                ClusterObjectFieldDescriptor(Label="protocolVersion", Tag=0x00000003, Type=typing.Union[None, Nullable, str]),
                ClusterObjectFieldDescriptor(Label="powerThreshold", Tag=0x00000004, Type=typing.Union[None, Nullable, Globals.Structs.PowerThresholdStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    meterType: typing.Union[Nullable, MeterIdentification.Enums.MeterTypeEnum] = NullValue
    pointOfDelivery: typing.Union[Nullable, str] = NullValue
    meterSerialNumber: typing.Union[Nullable, str] = NullValue
    protocolVersion: typing.Union[None, Nullable, str] = None
    powerThreshold: typing.Union[None, Nullable, Globals.Structs.PowerThresholdStruct] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class MeterTypeEnum(MatterIntEnum):
            kUtility = 0x00
            kPrivate = 0x01
            kGeneric = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

    class Bitmaps:
        class Feature(IntFlag):
            kPowerThreshold = 0x1

    class Attributes:
        MeterType = _attr(__module__, __qualname__, "MeterType", 0x00000B06, 0x00000000, "typing.Union[Nullable, MeterIdentification.Enums.MeterTypeEnum]", NullValue)

        PointOfDelivery = _attr(__module__, __qualname__, "PointOfDelivery", 0x00000B06, 0x00000001, "typing.Union[Nullable, str]", NullValue)

        MeterSerialNumber = _attr(__module__, __qualname__, "MeterSerialNumber", 0x00000B06, 0x00000002, "typing.Union[Nullable, str]", NullValue)

        ProtocolVersion = _attr(__module__, __qualname__, "ProtocolVersion", 0x00000B06, 0x00000003, "typing.Union[None, Nullable, str]", None)

        PowerThreshold = _attr(__module__, __qualname__, "PowerThreshold", 0x00000B06, 0x00000004, "typing.Union[None, Nullable, Globals.Structs.PowerThresholdStruct]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000B06, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000B06, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000B06, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000B06, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000B06, 0x0000FFFD, "uint", 0)
