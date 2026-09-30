"""ThirdRealityMeteringCluster cluster definition (auto-generated, DO NOT edit)."""

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
class ThirdRealityMeteringCluster(Cluster):
    id: typing.ClassVar[int] = 0x130DFC02

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="currentSummationDelivered", Tag=0x00000000, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="multiplier", Tag=0x00000301, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="divisor", Tag=0x00000302, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="instantaneousDemand", Tag=0x00000400, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    currentSummationDelivered: typing.Optional[uint] = None
    multiplier: typing.Optional[uint] = None
    divisor: typing.Optional[uint] = None
    instantaneousDemand: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        CurrentSummationDelivered = _attr(__module__, __qualname__, "CurrentSummationDelivered", 0x130DFC02, 0x00000000, "typing.Optional[uint]", None)

        Multiplier = _attr(__module__, __qualname__, "Multiplier", 0x130DFC02, 0x00000301, "typing.Optional[uint]", None)

        Divisor = _attr(__module__, __qualname__, "Divisor", 0x130DFC02, 0x00000302, "typing.Optional[uint]", None)

        InstantaneousDemand = _attr(__module__, __qualname__, "InstantaneousDemand", 0x130DFC02, 0x00000400, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x130DFC02, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x130DFC02, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x130DFC02, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x130DFC02, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x130DFC02, 0x0000FFFD, "uint", 0)
