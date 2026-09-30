"""HeimanCluster cluster definition (auto-generated, DO NOT edit)."""

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
class HeimanCluster(Cluster):
    id: typing.ClassVar[int] = 0x120BFC01

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="tamperAlarm", Tag=0x00000010, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="preheatingState", Tag=0x00000011, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="noDisturbingState", Tag=0x00000012, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="sensorType", Tag=0x00000013, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="sirenActive", Tag=0x00000014, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="alarmMute", Tag=0x00000015, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="lowPowerMode", Tag=0x00000016, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    tamperAlarm: typing.Optional[uint] = None
    preheatingState: typing.Optional[uint] = None
    noDisturbingState: typing.Optional[uint] = None
    sensorType: typing.Optional[uint] = None
    sirenActive: typing.Optional[uint] = None
    alarmMute: typing.Optional[uint] = None
    lowPowerMode: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Commands:
        @dataclass
        class MutingSensor(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x120BFC01
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mutingTime", Tag=0, Type=typing.Optional[uint]),
                    ])

            mutingTime: typing.Optional[uint] = None

    class Attributes:
        TamperAlarm = _attr(__module__, __qualname__, "TamperAlarm", 0x120BFC01, 0x00000010, "typing.Optional[uint]", None)

        PreheatingState = _attr(__module__, __qualname__, "PreheatingState", 0x120BFC01, 0x00000011, "typing.Optional[uint]", None)

        NoDisturbingState = _attr(__module__, __qualname__, "NoDisturbingState", 0x120BFC01, 0x00000012, "typing.Optional[uint]", None)

        SensorType = _attr(__module__, __qualname__, "SensorType", 0x120BFC01, 0x00000013, "typing.Optional[uint]", None)

        SirenActive = _attr(__module__, __qualname__, "SirenActive", 0x120BFC01, 0x00000014, "typing.Optional[uint]", None)

        AlarmMute = _attr(__module__, __qualname__, "AlarmMute", 0x120BFC01, 0x00000015, "typing.Optional[uint]", None)

        LowPowerMode = _attr(__module__, __qualname__, "LowPowerMode", 0x120BFC01, 0x00000016, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x120BFC01, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x120BFC01, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x120BFC01, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x120BFC01, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x120BFC01, 0x0000FFFD, "uint", 0)
