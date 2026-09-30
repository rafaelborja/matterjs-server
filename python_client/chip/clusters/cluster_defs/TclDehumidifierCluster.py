"""TclDehumidifierCluster cluster definition (auto-generated, DO NOT edit)."""

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
class TclDehumidifierCluster(Cluster):
    id: typing.ClassVar[int] = 0x1334FC03

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="mode", Tag=0x00000000, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="targetHumidity", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentHumidity", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="waterBucketFull", Tag=0x00000003, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="filterAlert", Tag=0x00000004, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="errorCodes", Tag=0x00000005, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="featureSet", Tag=0x00000006, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    mode: typing.Optional[uint] = None
    targetHumidity: typing.Optional[uint] = None
    currentHumidity: typing.Optional[uint] = None
    waterBucketFull: typing.Optional[bool] = None
    filterAlert: typing.Optional[bool] = None
    errorCodes: typing.Optional[str] = None
    featureSet: typing.Optional[str] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        Mode = _attr(__module__, __qualname__, "Mode", 0x1334FC03, 0x00000000, "typing.Optional[uint]", None)

        TargetHumidity = _attr(__module__, __qualname__, "TargetHumidity", 0x1334FC03, 0x00000001, "typing.Optional[uint]", None)

        CurrentHumidity = _attr(__module__, __qualname__, "CurrentHumidity", 0x1334FC03, 0x00000002, "typing.Optional[uint]", None)

        WaterBucketFull = _attr(__module__, __qualname__, "WaterBucketFull", 0x1334FC03, 0x00000003, "typing.Optional[bool]", None)

        FilterAlert = _attr(__module__, __qualname__, "FilterAlert", 0x1334FC03, 0x00000004, "typing.Optional[bool]", None)

        ErrorCodes = _attr(__module__, __qualname__, "ErrorCodes", 0x1334FC03, 0x00000005, "typing.Optional[str]", None)

        FeatureSet = _attr(__module__, __qualname__, "FeatureSet", 0x1334FC03, 0x00000006, "typing.Optional[str]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x1334FC03, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x1334FC03, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x1334FC03, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x1334FC03, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x1334FC03, 0x0000FFFD, "uint", 0)
