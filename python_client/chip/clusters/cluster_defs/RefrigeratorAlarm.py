"""RefrigeratorAlarm cluster definition (auto-generated, DO NOT edit)."""

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
class RefrigeratorAlarm(Cluster):
    id: typing.ClassVar[int] = 0x00000057

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="mask", Tag=0x00000000, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                ClusterObjectFieldDescriptor(Label="latch", Tag=0x00000001, Type=typing.Optional[RefrigeratorAlarm.Bitmaps.AlarmBitmap]),
                ClusterObjectFieldDescriptor(Label="state", Tag=0x00000002, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                ClusterObjectFieldDescriptor(Label="supported", Tag=0x00000003, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    mask: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
    latch: typing.Optional[RefrigeratorAlarm.Bitmaps.AlarmBitmap] = None
    state: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
    supported: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kReset = 0x1

        class AlarmBitmap(IntFlag):
            kDoorOpen = 0x1

    class Commands:
        @dataclass
        class ModifyEnabledAlarms(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000057
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mask", Tag=0, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                    ])

            mask: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0

        @dataclass
        class Reset(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000057
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="alarms", Tag=0, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                    ])

            alarms: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0

    class Attributes:
        Mask = _attr(__module__, __qualname__, "Mask", 0x00000057, 0x00000000, "RefrigeratorAlarm.Bitmaps.AlarmBitmap", 0)

        Latch = _attr(__module__, __qualname__, "Latch", 0x00000057, 0x00000001, "typing.Optional[RefrigeratorAlarm.Bitmaps.AlarmBitmap]", None)

        State = _attr(__module__, __qualname__, "State", 0x00000057, 0x00000002, "RefrigeratorAlarm.Bitmaps.AlarmBitmap", 0)

        Supported = _attr(__module__, __qualname__, "Supported", 0x00000057, 0x00000003, "RefrigeratorAlarm.Bitmaps.AlarmBitmap", 0)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000057, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000057, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000057, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000057, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000057, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class Notify(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000057

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="active", Tag=0, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                        ClusterObjectFieldDescriptor(Label="inactive", Tag=1, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                        ClusterObjectFieldDescriptor(Label="state", Tag=2, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                        ClusterObjectFieldDescriptor(Label="mask", Tag=3, Type=RefrigeratorAlarm.Bitmaps.AlarmBitmap),
                    ])

            active: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
            inactive: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
            state: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
            mask: RefrigeratorAlarm.Bitmaps.AlarmBitmap = 0
