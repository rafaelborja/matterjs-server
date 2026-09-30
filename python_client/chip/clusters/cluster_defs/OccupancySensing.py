"""OccupancySensing cluster definition (auto-generated, DO NOT edit)."""

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
class OccupancySensing(Cluster):
    id: typing.ClassVar[int] = 0x00000406

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="occupancy", Tag=0x00000000, Type=OccupancySensing.Bitmaps.OccupancyBitmap),
                ClusterObjectFieldDescriptor(Label="occupancySensorType", Tag=0x00000001, Type=OccupancySensing.Enums.OccupancySensorTypeEnum),
                ClusterObjectFieldDescriptor(Label="occupancySensorTypeBitmap", Tag=0x00000002, Type=OccupancySensing.Bitmaps.OccupancySensorTypeBitmap),
                ClusterObjectFieldDescriptor(Label="holdTime", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="holdTimeLimits", Tag=0x00000004, Type=typing.Optional[OccupancySensing.Structs.HoldTimeLimitsStruct]),
                ClusterObjectFieldDescriptor(Label="PIROccupiedToUnoccupiedDelay", Tag=0x00000010, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="PIRUnoccupiedToOccupiedDelay", Tag=0x00000011, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="PIRUnoccupiedToOccupiedThreshold", Tag=0x00000012, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="ultrasonicOccupiedToUnoccupiedDelay", Tag=0x00000020, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="ultrasonicUnoccupiedToOccupiedDelay", Tag=0x00000021, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="ultrasonicUnoccupiedToOccupiedThreshold", Tag=0x00000022, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="physicalContactOccupiedToUnoccupiedDelay", Tag=0x00000030, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="physicalContactUnoccupiedToOccupiedDelay", Tag=0x00000031, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="physicalContactUnoccupiedToOccupiedThreshold", Tag=0x00000032, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    occupancy: OccupancySensing.Bitmaps.OccupancyBitmap = 0
    occupancySensorType: OccupancySensing.Enums.OccupancySensorTypeEnum = 0
    occupancySensorTypeBitmap: OccupancySensing.Bitmaps.OccupancySensorTypeBitmap = 0
    holdTime: typing.Optional[uint] = None
    holdTimeLimits: typing.Optional[OccupancySensing.Structs.HoldTimeLimitsStruct] = None
    PIROccupiedToUnoccupiedDelay: typing.Optional[uint] = None
    PIRUnoccupiedToOccupiedDelay: typing.Optional[uint] = None
    PIRUnoccupiedToOccupiedThreshold: typing.Optional[uint] = None
    ultrasonicOccupiedToUnoccupiedDelay: typing.Optional[uint] = None
    ultrasonicUnoccupiedToOccupiedDelay: typing.Optional[uint] = None
    ultrasonicUnoccupiedToOccupiedThreshold: typing.Optional[uint] = None
    physicalContactOccupiedToUnoccupiedDelay: typing.Optional[uint] = None
    physicalContactUnoccupiedToOccupiedDelay: typing.Optional[uint] = None
    physicalContactUnoccupiedToOccupiedThreshold: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class OccupancySensorTypeEnum(MatterIntEnum):
            kPir = 0x00
            kUltrasonic = 0x01
            kPIRAndUltrasonic = 0x02
            kPhysicalContact = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Bitmaps:
        class Feature(IntFlag):
            kOther = 0x1
            kPassiveInfrared = 0x2
            kUltrasonic = 0x4
            kPhysicalContact = 0x8
            kActiveInfrared = 0x10
            kRadar = 0x20
            kRFSensing = 0x40
            kVision = 0x80
            kOccupancyEvent = 0x200

        class OccupancyBitmap(IntFlag):
            kOccupied = 0x1

        class OccupancySensorTypeBitmap(IntFlag):
            kPir = 0x1
            kUltrasonic = 0x2
            kPhysicalContact = 0x4

    class Structs:
        @dataclass
        class HoldTimeLimitsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="holdTimeMin", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="holdTimeMax", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="holdTimeDefault", Tag=2, Type=uint),
                    ])

            holdTimeMin: uint = 0
            holdTimeMax: uint = 0
            holdTimeDefault: uint = 0

    class Attributes:
        Occupancy = _attr(__module__, __qualname__, "Occupancy", 0x00000406, 0x00000000, "OccupancySensing.Bitmaps.OccupancyBitmap", 0)

        OccupancySensorType = _attr(__module__, __qualname__, "OccupancySensorType", 0x00000406, 0x00000001, "OccupancySensing.Enums.OccupancySensorTypeEnum", 0)

        OccupancySensorTypeBitmap = _attr(__module__, __qualname__, "OccupancySensorTypeBitmap", 0x00000406, 0x00000002, "OccupancySensing.Bitmaps.OccupancySensorTypeBitmap", 0)

        HoldTime = _attr(__module__, __qualname__, "HoldTime", 0x00000406, 0x00000003, "typing.Optional[uint]", None)

        HoldTimeLimits = _attr(__module__, __qualname__, "HoldTimeLimits", 0x00000406, 0x00000004, "typing.Optional[OccupancySensing.Structs.HoldTimeLimitsStruct]", None)

        PIROccupiedToUnoccupiedDelay = _attr(__module__, __qualname__, "PIROccupiedToUnoccupiedDelay", 0x00000406, 0x00000010, "typing.Optional[uint]", None)

        PIRUnoccupiedToOccupiedDelay = _attr(__module__, __qualname__, "PIRUnoccupiedToOccupiedDelay", 0x00000406, 0x00000011, "typing.Optional[uint]", None)

        PIRUnoccupiedToOccupiedThreshold = _attr(__module__, __qualname__, "PIRUnoccupiedToOccupiedThreshold", 0x00000406, 0x00000012, "typing.Optional[uint]", None)

        UltrasonicOccupiedToUnoccupiedDelay = _attr(__module__, __qualname__, "UltrasonicOccupiedToUnoccupiedDelay", 0x00000406, 0x00000020, "typing.Optional[uint]", None)

        UltrasonicUnoccupiedToOccupiedDelay = _attr(__module__, __qualname__, "UltrasonicUnoccupiedToOccupiedDelay", 0x00000406, 0x00000021, "typing.Optional[uint]", None)

        UltrasonicUnoccupiedToOccupiedThreshold = _attr(__module__, __qualname__, "UltrasonicUnoccupiedToOccupiedThreshold", 0x00000406, 0x00000022, "typing.Optional[uint]", None)

        PhysicalContactOccupiedToUnoccupiedDelay = _attr(__module__, __qualname__, "PhysicalContactOccupiedToUnoccupiedDelay", 0x00000406, 0x00000030, "typing.Optional[uint]", None)

        PhysicalContactUnoccupiedToOccupiedDelay = _attr(__module__, __qualname__, "PhysicalContactUnoccupiedToOccupiedDelay", 0x00000406, 0x00000031, "typing.Optional[uint]", None)

        PhysicalContactUnoccupiedToOccupiedThreshold = _attr(__module__, __qualname__, "PhysicalContactUnoccupiedToOccupiedThreshold", 0x00000406, 0x00000032, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000406, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000406, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000406, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000406, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000406, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class OccupancyChanged(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000406

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="occupancy", Tag=0, Type=OccupancySensing.Bitmaps.OccupancyBitmap),
                    ])

            occupancy: OccupancySensing.Bitmaps.OccupancyBitmap = 0
