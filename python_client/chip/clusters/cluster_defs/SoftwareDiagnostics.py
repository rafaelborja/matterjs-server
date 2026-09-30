"""SoftwareDiagnostics cluster definition (auto-generated, DO NOT edit)."""

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
class SoftwareDiagnostics(Cluster):
    id: typing.ClassVar[int] = 0x00000034

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="threadMetrics", Tag=0x00000000, Type=typing.Optional[typing.List[SoftwareDiagnostics.Structs.ThreadMetricsStruct]]),
                ClusterObjectFieldDescriptor(Label="currentHeapFree", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentHeapUsed", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentHeapHighWatermark", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    threadMetrics: typing.Optional[typing.List[SoftwareDiagnostics.Structs.ThreadMetricsStruct]] = None
    currentHeapFree: typing.Optional[uint] = None
    currentHeapUsed: typing.Optional[uint] = None
    currentHeapHighWatermark: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kWatermarks = 0x1

    class Structs:
        @dataclass
        class ThreadMetricsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="id", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="name", Tag=1, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="stackFreeCurrent", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="stackFreeMinimum", Tag=3, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="stackSize", Tag=4, Type=typing.Optional[uint]),
                    ])

            id: uint = 0
            name: typing.Optional[str] = None
            stackFreeCurrent: typing.Optional[uint] = None
            stackFreeMinimum: typing.Optional[uint] = None
            stackSize: typing.Optional[uint] = None

    class Commands:
        @dataclass
        class ResetWatermarks(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000034
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


    class Attributes:
        ThreadMetrics = _attr(__module__, __qualname__, "ThreadMetrics", 0x00000034, 0x00000000, "typing.Optional[typing.List[SoftwareDiagnostics.Structs.ThreadMetricsStruct]]", None)

        CurrentHeapFree = _attr(__module__, __qualname__, "CurrentHeapFree", 0x00000034, 0x00000001, "typing.Optional[uint]", None)

        CurrentHeapUsed = _attr(__module__, __qualname__, "CurrentHeapUsed", 0x00000034, 0x00000002, "typing.Optional[uint]", None)

        CurrentHeapHighWatermark = _attr(__module__, __qualname__, "CurrentHeapHighWatermark", 0x00000034, 0x00000003, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000034, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000034, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000034, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000034, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000034, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class SoftwareFault(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000034

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="id", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="name", Tag=1, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="faultRecording", Tag=2, Type=typing.Optional[bytes]),
                    ])

            id: uint = 0
            name: typing.Optional[str] = None
            faultRecording: typing.Optional[bytes] = None
