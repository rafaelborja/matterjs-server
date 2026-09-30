"""TemperatureMeasurement cluster definition (auto-generated, DO NOT edit)."""

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
class TemperatureMeasurement(Cluster):
    id: typing.ClassVar[int] = 0x00000402

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="measuredValue", Tag=0x00000000, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="minMeasuredValue", Tag=0x00000001, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="maxMeasuredValue", Tag=0x00000002, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="tolerance", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    measuredValue: typing.Union[Nullable, int] = NullValue
    minMeasuredValue: typing.Union[Nullable, int] = NullValue
    maxMeasuredValue: typing.Union[Nullable, int] = NullValue
    tolerance: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        MeasuredValue = _attr(__module__, __qualname__, "MeasuredValue", 0x00000402, 0x00000000, "typing.Union[Nullable, int]", NullValue)

        MinMeasuredValue = _attr(__module__, __qualname__, "MinMeasuredValue", 0x00000402, 0x00000001, "typing.Union[Nullable, int]", NullValue)

        MaxMeasuredValue = _attr(__module__, __qualname__, "MaxMeasuredValue", 0x00000402, 0x00000002, "typing.Union[Nullable, int]", NullValue)

        Tolerance = _attr(__module__, __qualname__, "Tolerance", 0x00000402, 0x00000003, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000402, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000402, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000402, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000402, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000402, 0x0000FFFD, "uint", 0)
