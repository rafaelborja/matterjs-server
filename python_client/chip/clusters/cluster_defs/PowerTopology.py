"""PowerTopology cluster definition (auto-generated, DO NOT edit)."""

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
class PowerTopology(Cluster):
    id: typing.ClassVar[int] = 0x0000009C

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="availableEndpoints", Tag=0x00000000, Type=typing.Optional[typing.List[uint]]),
                ClusterObjectFieldDescriptor(Label="activeEndpoints", Tag=0x00000001, Type=typing.Optional[typing.List[uint]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    availableEndpoints: typing.Optional[typing.List[uint]] = None
    activeEndpoints: typing.Optional[typing.List[uint]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kNodeTopology = 0x1
            kTreeTopology = 0x2
            kSetTopology = 0x4
            kDynamicPowerFlow = 0x8

    class Attributes:
        AvailableEndpoints = _attr(__module__, __qualname__, "AvailableEndpoints", 0x0000009C, 0x00000000, "typing.Optional[typing.List[uint]]", None)

        ActiveEndpoints = _attr(__module__, __qualname__, "ActiveEndpoints", 0x0000009C, 0x00000001, "typing.Optional[typing.List[uint]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000009C, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000009C, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000009C, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000009C, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000009C, 0x0000FFFD, "uint", 0)
