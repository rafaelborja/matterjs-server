"""TemperatureAlarm cluster definition (auto-generated, DO NOT edit)."""

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
class TemperatureAlarm(Cluster):
    id: typing.ClassVar[int] = 0x00000064

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="mask", Tag=0x00000000, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                ClusterObjectFieldDescriptor(Label="latch", Tag=0x00000001, Type=typing.Optional[TemperatureAlarm.Bitmaps.AlarmBitmap]),
                ClusterObjectFieldDescriptor(Label="state", Tag=0x00000002, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                ClusterObjectFieldDescriptor(Label="supported", Tag=0x00000003, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                ClusterObjectFieldDescriptor(Label="criticalOverTemperatureThreshold", Tag=0x00000080, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="majorOverTemperatureThreshold", Tag=0x00000081, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="minorOverTemperatureThreshold", Tag=0x00000082, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="minorUnderTemperatureThreshold", Tag=0x00000083, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="majorUnderTemperatureThreshold", Tag=0x00000084, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="criticalUnderTemperatureThreshold", Tag=0x00000085, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    mask: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
    latch: typing.Optional[TemperatureAlarm.Bitmaps.AlarmBitmap] = None
    state: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
    supported: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
    criticalOverTemperatureThreshold: typing.Optional[int] = None
    majorOverTemperatureThreshold: typing.Optional[int] = None
    minorOverTemperatureThreshold: typing.Optional[int] = None
    minorUnderTemperatureThreshold: typing.Optional[int] = None
    majorUnderTemperatureThreshold: typing.Optional[int] = None
    criticalUnderTemperatureThreshold: typing.Optional[int] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kOverTemperature = 0x100000
            kUnderTemperature = 0x200000
            kMajorThreshold = 0x400000
            kMinorThreshold = 0x800000
            kOverCriticalAdjustable = 0x1000000
            kOverMajorAdjustable = 0x2000000
            kOverMinorAdjustable = 0x4000000
            kUnderMinorAdjustable = 0x8000000
            kUnderMajorAdjustable = 0x10000000
            kUnderCriticalAdjustable = 0x20000000
            kReset = 0x1

        class AlarmBitmap(IntFlag):
            kCriticalOverTemperatureAlarm = 0x1
            kMajorOverTemperatureAlarm = 0x2
            kMinorOverTemperatureAlarm = 0x4
            kMinorUnderTemperatureAlarm = 0x8
            kMajorUnderTemperatureAlarm = 0x10
            kCriticalUnderTemperatureAlarm = 0x20

    class Commands:
        @dataclass
        class SetTemperatureAlarmThresholds(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000064
            command_id: typing.ClassVar[int] = 0x00000080
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="criticalOverTemperatureThreshold", Tag=0, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="majorOverTemperatureThreshold", Tag=1, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="minorOverTemperatureThreshold", Tag=2, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="minorUnderTemperatureThreshold", Tag=3, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="majorUnderTemperatureThreshold", Tag=4, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="criticalUnderTemperatureThreshold", Tag=5, Type=typing.Optional[int]),
                    ])

            criticalOverTemperatureThreshold: typing.Optional[int] = None
            majorOverTemperatureThreshold: typing.Optional[int] = None
            minorOverTemperatureThreshold: typing.Optional[int] = None
            minorUnderTemperatureThreshold: typing.Optional[int] = None
            majorUnderTemperatureThreshold: typing.Optional[int] = None
            criticalUnderTemperatureThreshold: typing.Optional[int] = None

        @dataclass
        class Reset(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000064
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="alarms", Tag=0, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                    ])

            alarms: TemperatureAlarm.Bitmaps.AlarmBitmap = 0

        @dataclass
        class ModifyEnabledAlarms(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000064
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mask", Tag=0, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                    ])

            mask: TemperatureAlarm.Bitmaps.AlarmBitmap = 0

    class Attributes:
        Mask = _attr(__module__, __qualname__, "Mask", 0x00000064, 0x00000000, "TemperatureAlarm.Bitmaps.AlarmBitmap", 0)

        Latch = _attr(__module__, __qualname__, "Latch", 0x00000064, 0x00000001, "typing.Optional[TemperatureAlarm.Bitmaps.AlarmBitmap]", None)

        State = _attr(__module__, __qualname__, "State", 0x00000064, 0x00000002, "TemperatureAlarm.Bitmaps.AlarmBitmap", 0)

        Supported = _attr(__module__, __qualname__, "Supported", 0x00000064, 0x00000003, "TemperatureAlarm.Bitmaps.AlarmBitmap", 0)

        CriticalOverTemperatureThreshold = _attr(__module__, __qualname__, "CriticalOverTemperatureThreshold", 0x00000064, 0x00000080, "typing.Optional[int]", None)

        MajorOverTemperatureThreshold = _attr(__module__, __qualname__, "MajorOverTemperatureThreshold", 0x00000064, 0x00000081, "typing.Optional[int]", None)

        MinorOverTemperatureThreshold = _attr(__module__, __qualname__, "MinorOverTemperatureThreshold", 0x00000064, 0x00000082, "typing.Optional[int]", None)

        MinorUnderTemperatureThreshold = _attr(__module__, __qualname__, "MinorUnderTemperatureThreshold", 0x00000064, 0x00000083, "typing.Optional[int]", None)

        MajorUnderTemperatureThreshold = _attr(__module__, __qualname__, "MajorUnderTemperatureThreshold", 0x00000064, 0x00000084, "typing.Optional[int]", None)

        CriticalUnderTemperatureThreshold = _attr(__module__, __qualname__, "CriticalUnderTemperatureThreshold", 0x00000064, 0x00000085, "typing.Optional[int]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000064, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000064, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000064, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000064, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000064, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class Notify(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000064

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="active", Tag=0, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                        ClusterObjectFieldDescriptor(Label="inactive", Tag=1, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                        ClusterObjectFieldDescriptor(Label="state", Tag=2, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                        ClusterObjectFieldDescriptor(Label="mask", Tag=3, Type=TemperatureAlarm.Bitmaps.AlarmBitmap),
                    ])

            active: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
            inactive: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
            state: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
            mask: TemperatureAlarm.Bitmaps.AlarmBitmap = 0
