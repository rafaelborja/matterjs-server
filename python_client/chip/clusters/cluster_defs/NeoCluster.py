"""NeoCluster cluster definition (auto-generated, DO NOT edit)."""

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
class NeoCluster(Cluster):
    id: typing.ClassVar[int] = 0x125DFC11

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="wattAccumulated", Tag=0x125D0021, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="current", Tag=0x125D0022, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="watt", Tag=0x125D0023, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="voltage", Tag=0x125D0024, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    wattAccumulated: typing.Optional[uint] = None
    current: typing.Optional[uint] = None
    watt: typing.Optional[uint] = None
    voltage: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        WattAccumulated = _attr(__module__, __qualname__, "WattAccumulated", 0x125DFC11, 0x125D0021, "typing.Optional[uint]", None)

        Current = _attr(__module__, __qualname__, "Current", 0x125DFC11, 0x125D0022, "typing.Optional[uint]", None)

        Watt = _attr(__module__, __qualname__, "Watt", 0x125DFC11, 0x125D0023, "typing.Optional[uint]", None)

        Voltage = _attr(__module__, __qualname__, "Voltage", 0x125DFC11, 0x125D0024, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x125DFC11, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x125DFC11, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x125DFC11, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x125DFC11, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x125DFC11, 0x0000FFFD, "uint", 0)
