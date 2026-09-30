"""TimeFormatLocalization cluster definition (auto-generated, DO NOT edit)."""

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
class TimeFormatLocalization(Cluster):
    id: typing.ClassVar[int] = 0x0000002C

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="hourFormat", Tag=0x00000000, Type=TimeFormatLocalization.Enums.HourFormatEnum),
                ClusterObjectFieldDescriptor(Label="activeCalendarType", Tag=0x00000001, Type=typing.Optional[TimeFormatLocalization.Enums.CalendarTypeEnum]),
                ClusterObjectFieldDescriptor(Label="supportedCalendarTypes", Tag=0x00000002, Type=typing.Optional[typing.List[TimeFormatLocalization.Enums.CalendarTypeEnum]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    hourFormat: TimeFormatLocalization.Enums.HourFormatEnum = 0
    activeCalendarType: typing.Optional[TimeFormatLocalization.Enums.CalendarTypeEnum] = None
    supportedCalendarTypes: typing.Optional[typing.List[TimeFormatLocalization.Enums.CalendarTypeEnum]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class HourFormatEnum(MatterIntEnum):
            k12hr = 0x00
            k24hr = 0x01
            kUseActiveLocale = 0xFF
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 256

        class CalendarTypeEnum(MatterIntEnum):
            kBuddhist = 0x00
            kChinese = 0x01
            kCoptic = 0x02
            kEthiopian = 0x03
            kGregorian = 0x04
            kHebrew = 0x05
            kIndian = 0x06
            kIslamic = 0x07
            kJapanese = 0x08
            kKorean = 0x09
            kPersian = 0x0A
            kTaiwanese = 0x0B
            kUseActiveLocale = 0xFF
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 256

    class Bitmaps:
        class Feature(IntFlag):
            kCalendarFormat = 0x1

    class Attributes:
        HourFormat = _attr(__module__, __qualname__, "HourFormat", 0x0000002C, 0x00000000, "TimeFormatLocalization.Enums.HourFormatEnum", 0)

        ActiveCalendarType = _attr(__module__, __qualname__, "ActiveCalendarType", 0x0000002C, 0x00000001, "typing.Optional[TimeFormatLocalization.Enums.CalendarTypeEnum]", None)

        SupportedCalendarTypes = _attr(__module__, __qualname__, "SupportedCalendarTypes", 0x0000002C, 0x00000002, "typing.Optional[typing.List[TimeFormatLocalization.Enums.CalendarTypeEnum]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000002C, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000002C, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000002C, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000002C, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000002C, 0x0000FFFD, "uint", 0)
