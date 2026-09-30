"""CommodityTariff cluster definition (auto-generated, DO NOT edit)."""

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
from .Globals import Globals


@dataclass
class CommodityTariff(Cluster):
    id: typing.ClassVar[int] = 0x00000700

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="tariffInfo", Tag=0x00000000, Type=typing.Union[Nullable, CommodityTariff.Structs.TariffInformationStruct]),
                ClusterObjectFieldDescriptor(Label="tariffUnit", Tag=0x00000001, Type=typing.Union[Nullable, Globals.Enums.TariffUnitEnum]),
                ClusterObjectFieldDescriptor(Label="startDate", Tag=0x00000002, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="dayEntries", Tag=0x00000003, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayEntryStruct]]),
                ClusterObjectFieldDescriptor(Label="dayPatterns", Tag=0x00000004, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayPatternStruct]]),
                ClusterObjectFieldDescriptor(Label="calendarPeriods", Tag=0x00000005, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.CalendarPeriodStruct]]),
                ClusterObjectFieldDescriptor(Label="individualDays", Tag=0x00000006, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayStruct]]),
                ClusterObjectFieldDescriptor(Label="currentDay", Tag=0x00000007, Type=typing.Union[Nullable, CommodityTariff.Structs.DayStruct]),
                ClusterObjectFieldDescriptor(Label="nextDay", Tag=0x00000008, Type=typing.Union[Nullable, CommodityTariff.Structs.DayStruct]),
                ClusterObjectFieldDescriptor(Label="currentDayEntry", Tag=0x00000009, Type=typing.Union[Nullable, CommodityTariff.Structs.DayEntryStruct]),
                ClusterObjectFieldDescriptor(Label="currentDayEntryDate", Tag=0x0000000A, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="nextDayEntry", Tag=0x0000000B, Type=typing.Union[Nullable, CommodityTariff.Structs.DayEntryStruct]),
                ClusterObjectFieldDescriptor(Label="nextDayEntryDate", Tag=0x0000000C, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="tariffComponents", Tag=0x0000000D, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]]),
                ClusterObjectFieldDescriptor(Label="tariffPeriods", Tag=0x0000000E, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffPeriodStruct]]),
                ClusterObjectFieldDescriptor(Label="currentTariffComponents", Tag=0x0000000F, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]]),
                ClusterObjectFieldDescriptor(Label="nextTariffComponents", Tag=0x00000010, Type=typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]]),
                ClusterObjectFieldDescriptor(Label="defaultRandomizationOffset", Tag=0x00000011, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="defaultRandomizationType", Tag=0x00000012, Type=typing.Union[None, Nullable, CommodityTariff.Enums.DayEntryRandomizationTypeEnum]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    tariffInfo: typing.Union[Nullable, CommodityTariff.Structs.TariffInformationStruct] = NullValue
    tariffUnit: typing.Union[Nullable, Globals.Enums.TariffUnitEnum] = NullValue
    startDate: typing.Union[Nullable, uint] = NullValue
    dayEntries: typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayEntryStruct]] = NullValue
    dayPatterns: typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayPatternStruct]] = NullValue
    calendarPeriods: typing.Union[Nullable, typing.List[CommodityTariff.Structs.CalendarPeriodStruct]] = NullValue
    individualDays: typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayStruct]] = NullValue
    currentDay: typing.Union[Nullable, CommodityTariff.Structs.DayStruct] = NullValue
    nextDay: typing.Union[Nullable, CommodityTariff.Structs.DayStruct] = NullValue
    currentDayEntry: typing.Union[Nullable, CommodityTariff.Structs.DayEntryStruct] = NullValue
    currentDayEntryDate: typing.Union[Nullable, uint] = NullValue
    nextDayEntry: typing.Union[Nullable, CommodityTariff.Structs.DayEntryStruct] = NullValue
    nextDayEntryDate: typing.Union[Nullable, uint] = NullValue
    tariffComponents: typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]] = NullValue
    tariffPeriods: typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffPeriodStruct]] = NullValue
    currentTariffComponents: typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]] = NullValue
    nextTariffComponents: typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]] = NullValue
    defaultRandomizationOffset: typing.Union[None, Nullable, int] = None
    defaultRandomizationType: typing.Union[None, Nullable, CommodityTariff.Enums.DayEntryRandomizationTypeEnum] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class AuxiliaryLoadSettingEnum(MatterIntEnum):
            kOff = 0x00
            kOn = 0x01
            kNone = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class DayTypeEnum(MatterIntEnum):
            kStandard = 0x00
            kHoliday = 0x01
            kDynamic = 0x02
            kEvent = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class PeakPeriodSeverityEnum(MatterIntEnum):
            kUnused = 0x00
            kLow = 0x01
            kMedium = 0x02
            kHigh = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class DayEntryRandomizationTypeEnum(MatterIntEnum):
            kNone = 0x00
            kFixed = 0x01
            kRandom = 0x02
            kRandomPositive = 0x03
            kRandomNegative = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

        class BlockModeEnum(MatterIntEnum):
            kNoBlock = 0x00
            kCombined = 0x01
            kIndividual = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

    class Bitmaps:
        class Feature(IntFlag):
            kPricing = 0x1
            kFriendlyCredit = 0x2
            kAuxiliaryLoad = 0x4
            kPeakPeriod = 0x8
            kPowerThreshold = 0x10
            kRandomization = 0x20

        class DayPatternDayOfWeekBitmap(IntFlag):
            kSunday = 0x1
            kMonday = 0x2
            kTuesday = 0x4
            kWednesday = 0x8
            kThursday = 0x10
            kFriday = 0x20
            kSaturday = 0x40

    class Structs:
        @dataclass
        class AuxiliaryLoadSwitchSettingsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="number", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="requiredState", Tag=1, Type=CommodityTariff.Enums.AuxiliaryLoadSettingEnum),
                    ])

            number: uint = 0
            requiredState: CommodityTariff.Enums.AuxiliaryLoadSettingEnum = 0

        @dataclass
        class AuxiliaryLoadSwitchesSettingsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="switchStates", Tag=0, Type=typing.List[CommodityTariff.Structs.AuxiliaryLoadSwitchSettingsStruct]),
                    ])

            switchStates: typing.List[CommodityTariff.Structs.AuxiliaryLoadSwitchSettingsStruct] = field(default_factory=lambda: [])

        @dataclass
        class CalendarPeriodStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="startDate", Tag=0, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="dayPatternIDs", Tag=1, Type=typing.List[uint]),
                    ])

            startDate: typing.Union[Nullable, uint] = NullValue
            dayPatternIDs: typing.List[uint] = field(default_factory=lambda: [])

        @dataclass
        class DayEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dayEntryID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="startTime", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="duration", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="randomizationOffset", Tag=3, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="randomizationType", Tag=4, Type=typing.Optional[CommodityTariff.Enums.DayEntryRandomizationTypeEnum]),
                    ])

            dayEntryID: uint = 0
            startTime: uint = 0
            duration: typing.Optional[uint] = None
            randomizationOffset: typing.Optional[int] = None
            randomizationType: typing.Optional[CommodityTariff.Enums.DayEntryRandomizationTypeEnum] = None

        @dataclass
        class DayStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="date", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="dayType", Tag=1, Type=CommodityTariff.Enums.DayTypeEnum),
                        ClusterObjectFieldDescriptor(Label="dayEntryIDs", Tag=2, Type=typing.List[uint]),
                    ])

            date: uint = 0
            dayType: CommodityTariff.Enums.DayTypeEnum = 0
            dayEntryIDs: typing.List[uint] = field(default_factory=lambda: [])

        @dataclass
        class DayPatternStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dayPatternID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="daysOfWeek", Tag=1, Type=CommodityTariff.Bitmaps.DayPatternDayOfWeekBitmap),
                        ClusterObjectFieldDescriptor(Label="dayEntryIDs", Tag=2, Type=typing.List[uint]),
                    ])

            dayPatternID: uint = 0
            daysOfWeek: CommodityTariff.Bitmaps.DayPatternDayOfWeekBitmap = 0
            dayEntryIDs: typing.List[uint] = field(default_factory=lambda: [])

        @dataclass
        class PeakPeriodStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="severity", Tag=0, Type=CommodityTariff.Enums.PeakPeriodSeverityEnum),
                        ClusterObjectFieldDescriptor(Label="peakPeriod", Tag=1, Type=uint),
                    ])

            severity: CommodityTariff.Enums.PeakPeriodSeverityEnum = 0
            peakPeriod: uint = 0

        @dataclass
        class TariffInformationStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="tariffLabel", Tag=0, Type=typing.Union[Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="providerName", Tag=1, Type=typing.Union[Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="currency", Tag=2, Type=typing.Union[None, Nullable, Globals.Structs.currency]),
                        ClusterObjectFieldDescriptor(Label="blockMode", Tag=3, Type=typing.Union[Nullable, CommodityTariff.Enums.BlockModeEnum]),
                    ])

            tariffLabel: typing.Union[Nullable, str] = NullValue
            providerName: typing.Union[Nullable, str] = NullValue
            currency: typing.Union[None, Nullable, Globals.Structs.currency] = None
            blockMode: typing.Union[Nullable, CommodityTariff.Enums.BlockModeEnum] = NullValue

        @dataclass
        class TariffPriceStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="priceType", Tag=0, Type=Globals.Enums.TariffPriceTypeEnum),
                        ClusterObjectFieldDescriptor(Label="price", Tag=1, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="priceLevel", Tag=2, Type=typing.Optional[int]),
                    ])

            priceType: Globals.Enums.TariffPriceTypeEnum = 0
            price: typing.Optional[int] = None
            priceLevel: typing.Optional[int] = None

        @dataclass
        class TariffComponentStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="tariffComponentID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="price", Tag=1, Type=typing.Union[None, Nullable, CommodityTariff.Structs.TariffPriceStruct]),
                        ClusterObjectFieldDescriptor(Label="friendlyCredit", Tag=2, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="auxiliaryLoad", Tag=3, Type=typing.Optional[CommodityTariff.Structs.AuxiliaryLoadSwitchSettingsStruct]),
                        ClusterObjectFieldDescriptor(Label="peakPeriod", Tag=4, Type=typing.Optional[CommodityTariff.Structs.PeakPeriodStruct]),
                        ClusterObjectFieldDescriptor(Label="powerThreshold", Tag=5, Type=typing.Optional[Globals.Structs.PowerThresholdStruct]),
                        ClusterObjectFieldDescriptor(Label="threshold", Tag=6, Type=typing.Union[Nullable, int]),
                        ClusterObjectFieldDescriptor(Label="label", Tag=7, Type=typing.Union[None, Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="predicted", Tag=8, Type=typing.Optional[bool]),
                    ])

            tariffComponentID: uint = 0
            price: typing.Union[None, Nullable, CommodityTariff.Structs.TariffPriceStruct] = None
            friendlyCredit: typing.Optional[bool] = None
            auxiliaryLoad: typing.Optional[CommodityTariff.Structs.AuxiliaryLoadSwitchSettingsStruct] = None
            peakPeriod: typing.Optional[CommodityTariff.Structs.PeakPeriodStruct] = None
            powerThreshold: typing.Optional[Globals.Structs.PowerThresholdStruct] = None
            threshold: typing.Union[Nullable, int] = NullValue
            label: typing.Union[None, Nullable, str] = None
            predicted: typing.Optional[bool] = None

        @dataclass
        class TariffPeriodStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="label", Tag=0, Type=typing.Union[Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="dayEntryIDs", Tag=1, Type=typing.List[uint]),
                        ClusterObjectFieldDescriptor(Label="tariffComponentIDs", Tag=2, Type=typing.List[uint]),
                    ])

            label: typing.Union[Nullable, str] = NullValue
            dayEntryIDs: typing.List[uint] = field(default_factory=lambda: [])
            tariffComponentIDs: typing.List[uint] = field(default_factory=lambda: [])

    class Commands:
        @dataclass
        class GetTariffComponent(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000700
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'GetTariffComponentResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="tariffComponentID", Tag=0, Type=uint),
                    ])

            tariffComponentID: uint = 0

        @dataclass
        class GetDayEntry(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000700
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'GetDayEntryResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dayEntryID", Tag=0, Type=uint),
                    ])

            dayEntryID: uint = 0

        @dataclass
        class GetTariffComponentResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000700
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="label", Tag=0, Type=typing.Union[Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="dayEntryIDs", Tag=1, Type=typing.List[uint]),
                        ClusterObjectFieldDescriptor(Label="tariffComponent", Tag=2, Type=CommodityTariff.Structs.TariffComponentStruct),
                    ])

            label: typing.Union[Nullable, str] = NullValue
            dayEntryIDs: typing.List[uint] = field(default_factory=lambda: [])
            tariffComponent: CommodityTariff.Structs.TariffComponentStruct = field(default_factory=lambda: CommodityTariff.Structs.TariffComponentStruct())

        @dataclass
        class GetDayEntryResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000700
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dayEntry", Tag=0, Type=CommodityTariff.Structs.DayEntryStruct),
                    ])

            dayEntry: CommodityTariff.Structs.DayEntryStruct = field(default_factory=lambda: CommodityTariff.Structs.DayEntryStruct())

    class Attributes:
        TariffInfo = _attr(__module__, __qualname__, "TariffInfo", 0x00000700, 0x00000000, "typing.Union[Nullable, CommodityTariff.Structs.TariffInformationStruct]", NullValue)

        TariffUnit = _attr(__module__, __qualname__, "TariffUnit", 0x00000700, 0x00000001, "typing.Union[Nullable, Globals.Enums.TariffUnitEnum]", NullValue)

        StartDate = _attr(__module__, __qualname__, "StartDate", 0x00000700, 0x00000002, "typing.Union[Nullable, uint]", NullValue)

        DayEntries = _attr(__module__, __qualname__, "DayEntries", 0x00000700, 0x00000003, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayEntryStruct]]", NullValue)

        DayPatterns = _attr(__module__, __qualname__, "DayPatterns", 0x00000700, 0x00000004, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayPatternStruct]]", NullValue)

        CalendarPeriods = _attr(__module__, __qualname__, "CalendarPeriods", 0x00000700, 0x00000005, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.CalendarPeriodStruct]]", NullValue)

        IndividualDays = _attr(__module__, __qualname__, "IndividualDays", 0x00000700, 0x00000006, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.DayStruct]]", NullValue)

        CurrentDay = _attr(__module__, __qualname__, "CurrentDay", 0x00000700, 0x00000007, "typing.Union[Nullable, CommodityTariff.Structs.DayStruct]", NullValue)

        NextDay = _attr(__module__, __qualname__, "NextDay", 0x00000700, 0x00000008, "typing.Union[Nullable, CommodityTariff.Structs.DayStruct]", NullValue)

        CurrentDayEntry = _attr(__module__, __qualname__, "CurrentDayEntry", 0x00000700, 0x00000009, "typing.Union[Nullable, CommodityTariff.Structs.DayEntryStruct]", NullValue)

        CurrentDayEntryDate = _attr(__module__, __qualname__, "CurrentDayEntryDate", 0x00000700, 0x0000000A, "typing.Union[Nullable, uint]", NullValue)

        NextDayEntry = _attr(__module__, __qualname__, "NextDayEntry", 0x00000700, 0x0000000B, "typing.Union[Nullable, CommodityTariff.Structs.DayEntryStruct]", NullValue)

        NextDayEntryDate = _attr(__module__, __qualname__, "NextDayEntryDate", 0x00000700, 0x0000000C, "typing.Union[Nullable, uint]", NullValue)

        TariffComponents = _attr(__module__, __qualname__, "TariffComponents", 0x00000700, 0x0000000D, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]]", NullValue)

        TariffPeriods = _attr(__module__, __qualname__, "TariffPeriods", 0x00000700, 0x0000000E, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffPeriodStruct]]", NullValue)

        CurrentTariffComponents = _attr(__module__, __qualname__, "CurrentTariffComponents", 0x00000700, 0x0000000F, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]]", NullValue)

        NextTariffComponents = _attr(__module__, __qualname__, "NextTariffComponents", 0x00000700, 0x00000010, "typing.Union[Nullable, typing.List[CommodityTariff.Structs.TariffComponentStruct]]", NullValue)

        DefaultRandomizationOffset = _attr(__module__, __qualname__, "DefaultRandomizationOffset", 0x00000700, 0x00000011, "typing.Union[None, Nullable, int]", None)

        DefaultRandomizationType = _attr(__module__, __qualname__, "DefaultRandomizationType", 0x00000700, 0x00000012, "typing.Union[None, Nullable, CommodityTariff.Enums.DayEntryRandomizationTypeEnum]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000700, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000700, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000700, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000700, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000700, 0x0000FFFD, "uint", 0)
