"""InovelliCluster cluster definition (auto-generated, DO NOT edit)."""

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
class InovelliCluster(Cluster):
    id: typing.ClassVar[int] = 0x122FFC31

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="ledIndicatorIntensityOn", Tag=0x122F0061, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="ledIndicatorIntensityOff", Tag=0x122F0062, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="clearNotificationWithConfigDoubleTap", Tag=0x122F0106, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    ledIndicatorIntensityOn: typing.Optional[uint] = None
    ledIndicatorIntensityOff: typing.Optional[uint] = None
    clearNotificationWithConfigDoubleTap: typing.Optional[bool] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        LEDIndicatorIntensityOn = _attr(__module__, __qualname__, "LEDIndicatorIntensityOn", 0x122FFC31, 0x122F0061, "typing.Optional[uint]", None)

        LEDIndicatorIntensityOff = _attr(__module__, __qualname__, "LEDIndicatorIntensityOff", 0x122FFC31, 0x122F0062, "typing.Optional[uint]", None)

        ClearNotificationWithConfigDoubleTap = _attr(__module__, __qualname__, "ClearNotificationWithConfigDoubleTap", 0x122FFC31, 0x122F0106, "typing.Optional[bool]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x122FFC31, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x122FFC31, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x122FFC31, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x122FFC31, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x122FFC31, 0x0000FFFD, "uint", 0)
