"""Switch cluster definition (auto-generated, DO NOT edit)."""

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
class Switch(Cluster):
    id: typing.ClassVar[int] = 0x0000003B

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="numberOfPositions", Tag=0x00000000, Type=uint),
                ClusterObjectFieldDescriptor(Label="currentPosition", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="multiPressMax", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    numberOfPositions: uint = 0
    currentPosition: uint = 0
    multiPressMax: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kLatchingSwitch = 0x1
            kMomentarySwitch = 0x2
            kMomentarySwitchRelease = 0x4
            kMomentarySwitchLongPress = 0x8
            kMomentarySwitchMultiPress = 0x10
            kActionSwitch = 0x20

    class Attributes:
        NumberOfPositions = _attr(__module__, __qualname__, "NumberOfPositions", 0x0000003B, 0x00000000, "uint", 0)

        CurrentPosition = _attr(__module__, __qualname__, "CurrentPosition", 0x0000003B, 0x00000001, "uint", 0)

        MultiPressMax = _attr(__module__, __qualname__, "MultiPressMax", 0x0000003B, 0x00000002, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000003B, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000003B, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000003B, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000003B, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000003B, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class SwitchLatched(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newPosition", Tag=0, Type=uint),
                    ])

            newPosition: uint = 0

        @dataclass
        class InitialPress(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newPosition", Tag=0, Type=uint),
                    ])

            newPosition: uint = 0

        @dataclass
        class LongPress(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000002

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newPosition", Tag=0, Type=uint),
                    ])

            newPosition: uint = 0

        @dataclass
        class ShortRelease(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000003

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousPosition", Tag=0, Type=uint),
                    ])

            previousPosition: uint = 0

        @dataclass
        class LongRelease(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000004

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousPosition", Tag=0, Type=uint),
                    ])

            previousPosition: uint = 0

        @dataclass
        class MultiPressOngoing(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000005

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newPosition", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="currentNumberOfPressesCounted", Tag=1, Type=uint),
                    ])

            newPosition: uint = 0
            currentNumberOfPressesCounted: uint = 0

        @dataclass
        class MultiPressComplete(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000003B

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000006

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousPosition", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="totalNumberOfPressesCounted", Tag=1, Type=uint),
                    ])

            previousPosition: uint = 0
            totalNumberOfPressesCounted: uint = 0
