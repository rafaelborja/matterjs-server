"""Thermostat cluster definition (auto-generated, DO NOT edit)."""

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
class Thermostat(Cluster):
    id: typing.ClassVar[int] = 0x00000201

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="localTemperature", Tag=0x00000000, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="outdoorTemperature", Tag=0x00000001, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="occupancy", Tag=0x00000002, Type=typing.Optional[Thermostat.Bitmaps.OccupancyBitmap]),
                ClusterObjectFieldDescriptor(Label="absMinHeatSetpointLimit", Tag=0x00000003, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="absMaxHeatSetpointLimit", Tag=0x00000004, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="absMinCoolSetpointLimit", Tag=0x00000005, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="absMaxCoolSetpointLimit", Tag=0x00000006, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="PICoolingDemand", Tag=0x00000007, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="PIHeatingDemand", Tag=0x00000008, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="HVACSystemTypeConfiguration", Tag=0x00000009, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="localTemperatureCalibration", Tag=0x00000010, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="occupiedCoolingSetpoint", Tag=0x00000011, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="occupiedHeatingSetpoint", Tag=0x00000012, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="unoccupiedCoolingSetpoint", Tag=0x00000013, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="unoccupiedHeatingSetpoint", Tag=0x00000014, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="minHeatSetpointLimit", Tag=0x00000015, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="maxHeatSetpointLimit", Tag=0x00000016, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="minCoolSetpointLimit", Tag=0x00000017, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="maxCoolSetpointLimit", Tag=0x00000018, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="minSetpointDeadBand", Tag=0x00000019, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="remoteSensing", Tag=0x0000001A, Type=typing.Optional[Thermostat.Bitmaps.RemoteSensingBitmap]),
                ClusterObjectFieldDescriptor(Label="controlSequenceOfOperation", Tag=0x0000001B, Type=Thermostat.Enums.ControlSequenceOfOperationEnum),
                ClusterObjectFieldDescriptor(Label="systemMode", Tag=0x0000001C, Type=Thermostat.Enums.SystemModeEnum),
                ClusterObjectFieldDescriptor(Label="thermostatRunningMode", Tag=0x0000001E, Type=typing.Optional[Thermostat.Enums.ThermostatRunningModeEnum]),
                ClusterObjectFieldDescriptor(Label="temperatureSetpointHold", Tag=0x00000023, Type=typing.Optional[Thermostat.Enums.TemperatureSetpointHoldEnum]),
                ClusterObjectFieldDescriptor(Label="temperatureSetpointHoldDuration", Tag=0x00000024, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="thermostatProgrammingOperationMode", Tag=0x00000025, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="thermostatRunningState", Tag=0x00000029, Type=typing.Optional[Thermostat.Bitmaps.RelayStateBitmap]),
                ClusterObjectFieldDescriptor(Label="setpointChangeSource", Tag=0x00000030, Type=typing.Optional[Thermostat.Enums.SetpointChangeSourceEnum]),
                ClusterObjectFieldDescriptor(Label="setpointChangeAmount", Tag=0x00000031, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="setpointChangeSourceTimestamp", Tag=0x00000032, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="occupiedSetback", Tag=0x00000034, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="occupiedSetbackMin", Tag=0x00000035, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="occupiedSetbackMax", Tag=0x00000036, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="unoccupiedSetback", Tag=0x00000037, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="unoccupiedSetbackMin", Tag=0x00000038, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="unoccupiedSetbackMax", Tag=0x00000039, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="emergencyHeatDelta", Tag=0x0000003A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="ACType", Tag=0x00000040, Type=typing.Optional[Thermostat.Enums.ACTypeEnum]),
                ClusterObjectFieldDescriptor(Label="ACCapacity", Tag=0x00000041, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="ACRefrigerantType", Tag=0x00000042, Type=typing.Optional[Thermostat.Enums.ACRefrigerantTypeEnum]),
                ClusterObjectFieldDescriptor(Label="ACCompressorType", Tag=0x00000043, Type=typing.Optional[Thermostat.Enums.ACCompressorTypeEnum]),
                ClusterObjectFieldDescriptor(Label="ACErrorCode", Tag=0x00000044, Type=typing.Optional[Thermostat.Bitmaps.ACErrorCodeBitmap]),
                ClusterObjectFieldDescriptor(Label="ACLouverPosition", Tag=0x00000045, Type=typing.Optional[Thermostat.Enums.ACLouverPositionEnum]),
                ClusterObjectFieldDescriptor(Label="ACCoilTemperature", Tag=0x00000046, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="ACCapacityformat", Tag=0x00000047, Type=typing.Optional[Thermostat.Enums.ACCapacityFormatEnum]),
                ClusterObjectFieldDescriptor(Label="presetTypes", Tag=0x00000048, Type=typing.Optional[typing.List[Thermostat.Structs.PresetTypeStruct]]),
                ClusterObjectFieldDescriptor(Label="scheduleTypes", Tag=0x00000049, Type=typing.Optional[typing.List[Thermostat.Structs.ScheduleTypeStruct]]),
                ClusterObjectFieldDescriptor(Label="numberOfPresets", Tag=0x0000004A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="numberOfSchedules", Tag=0x0000004B, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="numberOfScheduleTransitions", Tag=0x0000004C, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="numberOfScheduleTransitionPerDay", Tag=0x0000004D, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="activePresetHandle", Tag=0x0000004E, Type=typing.Union[None, Nullable, bytes]),
                ClusterObjectFieldDescriptor(Label="activeScheduleHandle", Tag=0x0000004F, Type=typing.Union[None, Nullable, bytes]),
                ClusterObjectFieldDescriptor(Label="presets", Tag=0x00000050, Type=typing.Optional[typing.List[Thermostat.Structs.PresetStruct]]),
                ClusterObjectFieldDescriptor(Label="schedules", Tag=0x00000051, Type=typing.Optional[typing.List[Thermostat.Structs.ScheduleStruct]]),
                ClusterObjectFieldDescriptor(Label="setpointHoldExpiryTimestamp", Tag=0x00000052, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="maxThermostatSuggestions", Tag=0x00000053, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="thermostatSuggestions", Tag=0x00000054, Type=typing.Optional[typing.List[Thermostat.Structs.ThermostatSuggestionStruct]]),
                ClusterObjectFieldDescriptor(Label="currentThermostatSuggestion", Tag=0x00000055, Type=typing.Union[None, Nullable, Thermostat.Structs.ThermostatSuggestionStruct]),
                ClusterObjectFieldDescriptor(Label="thermostatSuggestionNotFollowingReason", Tag=0x00000056, Type=typing.Union[None, Nullable, Thermostat.Bitmaps.ThermostatSuggestionNotFollowingReasonBitmap]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    localTemperature: typing.Union[Nullable, int] = NullValue
    outdoorTemperature: typing.Union[None, Nullable, int] = None
    occupancy: typing.Optional[Thermostat.Bitmaps.OccupancyBitmap] = None
    absMinHeatSetpointLimit: typing.Optional[int] = None
    absMaxHeatSetpointLimit: typing.Optional[int] = None
    absMinCoolSetpointLimit: typing.Optional[int] = None
    absMaxCoolSetpointLimit: typing.Optional[int] = None
    PICoolingDemand: typing.Optional[uint] = None
    PIHeatingDemand: typing.Optional[uint] = None
    HVACSystemTypeConfiguration: typing.Optional[uint] = None
    localTemperatureCalibration: typing.Optional[int] = None
    occupiedCoolingSetpoint: typing.Optional[int] = None
    occupiedHeatingSetpoint: typing.Optional[int] = None
    unoccupiedCoolingSetpoint: typing.Optional[int] = None
    unoccupiedHeatingSetpoint: typing.Optional[int] = None
    minHeatSetpointLimit: typing.Optional[int] = None
    maxHeatSetpointLimit: typing.Optional[int] = None
    minCoolSetpointLimit: typing.Optional[int] = None
    maxCoolSetpointLimit: typing.Optional[int] = None
    minSetpointDeadBand: typing.Optional[int] = None
    remoteSensing: typing.Optional[Thermostat.Bitmaps.RemoteSensingBitmap] = None
    controlSequenceOfOperation: Thermostat.Enums.ControlSequenceOfOperationEnum = 0
    systemMode: Thermostat.Enums.SystemModeEnum = 0
    thermostatRunningMode: typing.Optional[Thermostat.Enums.ThermostatRunningModeEnum] = None
    temperatureSetpointHold: typing.Optional[Thermostat.Enums.TemperatureSetpointHoldEnum] = None
    temperatureSetpointHoldDuration: typing.Union[None, Nullable, uint] = None
    thermostatProgrammingOperationMode: typing.Optional[uint] = None
    thermostatRunningState: typing.Optional[Thermostat.Bitmaps.RelayStateBitmap] = None
    setpointChangeSource: typing.Optional[Thermostat.Enums.SetpointChangeSourceEnum] = None
    setpointChangeAmount: typing.Union[None, Nullable, int] = None
    setpointChangeSourceTimestamp: typing.Optional[uint] = None
    occupiedSetback: typing.Optional[uint] = None
    occupiedSetbackMin: typing.Optional[uint] = None
    occupiedSetbackMax: typing.Optional[uint] = None
    unoccupiedSetback: typing.Optional[uint] = None
    unoccupiedSetbackMin: typing.Optional[uint] = None
    unoccupiedSetbackMax: typing.Optional[uint] = None
    emergencyHeatDelta: typing.Optional[uint] = None
    ACType: typing.Optional[Thermostat.Enums.ACTypeEnum] = None
    ACCapacity: typing.Optional[uint] = None
    ACRefrigerantType: typing.Optional[Thermostat.Enums.ACRefrigerantTypeEnum] = None
    ACCompressorType: typing.Optional[Thermostat.Enums.ACCompressorTypeEnum] = None
    ACErrorCode: typing.Optional[Thermostat.Bitmaps.ACErrorCodeBitmap] = None
    ACLouverPosition: typing.Optional[Thermostat.Enums.ACLouverPositionEnum] = None
    ACCoilTemperature: typing.Union[None, Nullable, int] = None
    ACCapacityformat: typing.Optional[Thermostat.Enums.ACCapacityFormatEnum] = None
    presetTypes: typing.Optional[typing.List[Thermostat.Structs.PresetTypeStruct]] = None
    scheduleTypes: typing.Optional[typing.List[Thermostat.Structs.ScheduleTypeStruct]] = None
    numberOfPresets: typing.Optional[uint] = None
    numberOfSchedules: typing.Optional[uint] = None
    numberOfScheduleTransitions: typing.Optional[uint] = None
    numberOfScheduleTransitionPerDay: typing.Union[None, Nullable, uint] = None
    activePresetHandle: typing.Union[None, Nullable, bytes] = None
    activeScheduleHandle: typing.Union[None, Nullable, bytes] = None
    presets: typing.Optional[typing.List[Thermostat.Structs.PresetStruct]] = None
    schedules: typing.Optional[typing.List[Thermostat.Structs.ScheduleStruct]] = None
    setpointHoldExpiryTimestamp: typing.Union[None, Nullable, uint] = None
    maxThermostatSuggestions: typing.Optional[uint] = None
    thermostatSuggestions: typing.Optional[typing.List[Thermostat.Structs.ThermostatSuggestionStruct]] = None
    currentThermostatSuggestion: typing.Union[None, Nullable, Thermostat.Structs.ThermostatSuggestionStruct] = None
    thermostatSuggestionNotFollowingReason: typing.Union[None, Nullable, Thermostat.Bitmaps.ThermostatSuggestionNotFollowingReasonBitmap] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class ACCapacityFormatEnum(MatterIntEnum):
            kBTUh = 0x00
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 1

        class ACCompressorTypeEnum(MatterIntEnum):
            kUnknown = 0x00
            kT1 = 0x01
            kT2 = 0x02
            kT3 = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class ACLouverPositionEnum(MatterIntEnum):
            kClosed = 0x01
            kOpen = 0x02
            kQuarter = 0x03
            kHalf = 0x04
            kThreeQuarters = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

        class ACRefrigerantTypeEnum(MatterIntEnum):
            kUnknown = 0x00
            kR22 = 0x01
            kR410a = 0x02
            kR407c = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class ACTypeEnum(MatterIntEnum):
            kUnknown = 0x00
            kCoolingFixed = 0x01
            kHeatPumpFixed = 0x02
            kCoolingInverter = 0x03
            kHeatPumpInverter = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

        class SetpointRaiseLowerModeEnum(MatterIntEnum):
            kHeat = 0x00
            kCool = 0x01
            kBoth = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class ControlSequenceOfOperationEnum(MatterIntEnum):
            kCoolingOnly = 0x00
            kCoolingWithReheat = 0x01
            kHeatingOnly = 0x02
            kHeatingWithReheat = 0x03
            kCoolingAndHeating = 0x04
            kCoolingAndHeatingWithReheat = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

        class PresetScenarioEnum(MatterIntEnum):
            kOccupied = 0x01
            kUnoccupied = 0x02
            kSleep = 0x03
            kWake = 0x04
            kVacation = 0x05
            kGoingToSleep = 0x06
            kUserDefined = 0xFE
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 255

        class SetpointChangeSourceEnum(MatterIntEnum):
            kManual = 0x00
            kSchedule = 0x01
            kExternal = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class StartOfWeekEnum(MatterIntEnum):
            kSunday = 0x00
            kMonday = 0x01
            kTuesday = 0x02
            kWednesday = 0x03
            kThursday = 0x04
            kFriday = 0x05
            kSaturday = 0x06
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 7

        class SystemModeEnum(MatterIntEnum):
            kOff = 0x00
            kAuto = 0x01
            kCool = 0x03
            kHeat = 0x04
            kEmergencyHeat = 0x05
            kPrecooling = 0x06
            kFanOnly = 0x07
            kDry = 0x08
            kSleep = 0x09
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 10

        class ThermostatRunningModeEnum(MatterIntEnum):
            kOff = 0x00
            kCool = 0x03
            kHeat = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

        class TemperatureSetpointHoldEnum(MatterIntEnum):
            kSetpointHoldOff = 0x00
            kSetpointHoldOn = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Bitmaps:
        class Feature(IntFlag):
            kHeating = 0x1
            kCooling = 0x2
            kOccupancy = 0x4
            kSetback = 0x10
            kAutoMode = 0x20
            kLocalTemperatureNotExposed = 0x40
            kMatterScheduleConfiguration = 0x80
            kPresets = 0x100
            kEvents = 0x200
            kThermostatSuggestions = 0x400

        class ACErrorCodeBitmap(IntFlag):
            kCompressorFail = 0x1
            kRoomSensorFail = 0x2
            kOutdoorSensorFail = 0x4
            kCoilSensorFail = 0x8
            kFanFail = 0x10

        class OccupancyBitmap(IntFlag):
            kOccupied = 0x1

        class PresetTypeFeaturesBitmap(IntFlag):
            kAutomatic = 0x1
            kSupportsNames = 0x2

        class RelayStateBitmap(IntFlag):
            kHeat = 0x1
            kCool = 0x2
            kFan = 0x4
            kHeatStage2 = 0x8
            kCoolStage2 = 0x10
            kFanStage2 = 0x20
            kFanStage3 = 0x40

        class RemoteSensingBitmap(IntFlag):
            kLocalTemperature = 0x1
            kOutdoorTemperature = 0x2
            kOccupancy = 0x4

        class ScheduleTypeFeaturesBitmap(IntFlag):
            kSupportsPresets = 0x1
            kSupportsSetpoints = 0x2
            kSupportsNames = 0x4
            kSupportsOff = 0x8

        class ScheduleDayOfWeekBitmap(IntFlag):
            kSunday = 0x1
            kMonday = 0x2
            kTuesday = 0x4
            kWednesday = 0x8
            kThursday = 0x10
            kFriday = 0x20
            kSaturday = 0x40
            kAway = 0x80

        class ScheduleModeBitmap(IntFlag):
            kHeatSetpointPresent = 0x1
            kCoolSetpointPresent = 0x2

        class ThermostatSuggestionNotFollowingReasonBitmap(IntFlag):
            kDemandResponseEvent = 0x1
            kOngoingHold = 0x2
            kSchedule = 0x4
            kOccupancy = 0x8
            kVacationMode = 0x10
            kTimeOfUseCostSavings = 0x20
            kPreCoolingOrPreHeating = 0x40
            kConflictingSuggestions = 0x80

    class Structs:
        @dataclass
        class PresetStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="presetHandle", Tag=0, Type=typing.Union[Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="presetScenario", Tag=1, Type=Thermostat.Enums.PresetScenarioEnum),
                        ClusterObjectFieldDescriptor(Label="name", Tag=2, Type=typing.Union[None, Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="coolingSetpoint", Tag=3, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="heatingSetpoint", Tag=4, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="builtIn", Tag=5, Type=typing.Union[Nullable, bool]),
                    ])

            presetHandle: typing.Union[Nullable, bytes] = NullValue
            presetScenario: Thermostat.Enums.PresetScenarioEnum = 0
            name: typing.Union[None, Nullable, str] = None
            coolingSetpoint: typing.Optional[int] = None
            heatingSetpoint: typing.Optional[int] = None
            builtIn: typing.Union[Nullable, bool] = NullValue

        @dataclass
        class PresetTypeStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="presetScenario", Tag=0, Type=Thermostat.Enums.PresetScenarioEnum),
                        ClusterObjectFieldDescriptor(Label="numberOfPresets", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="presetTypeFeatures", Tag=2, Type=Thermostat.Bitmaps.PresetTypeFeaturesBitmap),
                    ])

            presetScenario: Thermostat.Enums.PresetScenarioEnum = 0
            numberOfPresets: uint = 0
            presetTypeFeatures: Thermostat.Bitmaps.PresetTypeFeaturesBitmap = 0

        @dataclass
        class WeeklyScheduleTransitionStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="heatSetpoint", Tag=1, Type=typing.Union[Nullable, int]),
                        ClusterObjectFieldDescriptor(Label="coolSetpoint", Tag=2, Type=typing.Union[Nullable, int]),
                    ])

            transitionTime: uint = 0
            heatSetpoint: typing.Union[Nullable, int] = NullValue
            coolSetpoint: typing.Union[Nullable, int] = NullValue

        @dataclass
        class ScheduleStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="scheduleHandle", Tag=0, Type=typing.Union[Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="systemMode", Tag=1, Type=Thermostat.Enums.SystemModeEnum),
                        ClusterObjectFieldDescriptor(Label="name", Tag=2, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="presetHandle", Tag=3, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="transitions", Tag=4, Type=typing.List[Thermostat.Structs.ScheduleTransitionStruct]),
                        ClusterObjectFieldDescriptor(Label="builtIn", Tag=5, Type=typing.Union[Nullable, bool]),
                    ])

            scheduleHandle: typing.Union[Nullable, bytes] = NullValue
            systemMode: Thermostat.Enums.SystemModeEnum = 0
            name: typing.Optional[str] = None
            presetHandle: typing.Optional[bytes] = None
            transitions: typing.List[Thermostat.Structs.ScheduleTransitionStruct] = field(default_factory=lambda: [])
            builtIn: typing.Union[Nullable, bool] = NullValue

        @dataclass
        class ScheduleTransitionStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dayOfWeek", Tag=0, Type=Thermostat.Bitmaps.ScheduleDayOfWeekBitmap),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="presetHandle", Tag=2, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="systemMode", Tag=3, Type=typing.Optional[Thermostat.Enums.SystemModeEnum]),
                        ClusterObjectFieldDescriptor(Label="coolingSetpoint", Tag=4, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="heatingSetpoint", Tag=5, Type=typing.Optional[int]),
                    ])

            dayOfWeek: Thermostat.Bitmaps.ScheduleDayOfWeekBitmap = 0
            transitionTime: uint = 0
            presetHandle: typing.Optional[bytes] = None
            systemMode: typing.Optional[Thermostat.Enums.SystemModeEnum] = None
            coolingSetpoint: typing.Optional[int] = None
            heatingSetpoint: typing.Optional[int] = None

        @dataclass
        class ScheduleTypeStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="systemMode", Tag=0, Type=Thermostat.Enums.SystemModeEnum),
                        ClusterObjectFieldDescriptor(Label="numberOfSchedules", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="scheduleTypeFeatures", Tag=2, Type=Thermostat.Bitmaps.ScheduleTypeFeaturesBitmap),
                    ])

            systemMode: Thermostat.Enums.SystemModeEnum = 0
            numberOfSchedules: uint = 0
            scheduleTypeFeatures: Thermostat.Bitmaps.ScheduleTypeFeaturesBitmap = 0

        @dataclass
        class ThermostatSuggestionStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="uniqueID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="presetHandle", Tag=1, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="effectiveTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="expirationTime", Tag=3, Type=uint),
                    ])

            uniqueID: uint = 0
            presetHandle: bytes = b""
            effectiveTime: uint = 0
            expirationTime: uint = 0

    class Commands:
        @dataclass
        class SetpointRaiseLower(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mode", Tag=0, Type=Thermostat.Enums.SetpointRaiseLowerModeEnum),
                        ClusterObjectFieldDescriptor(Label="amount", Tag=1, Type=int),
                    ])

            mode: Thermostat.Enums.SetpointRaiseLowerModeEnum = 0
            amount: int = 0

        @dataclass
        class SetActiveScheduleRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="scheduleHandle", Tag=0, Type=bytes),
                    ])

            scheduleHandle: bytes = b""

        @dataclass
        class SetActivePresetRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="presetHandle", Tag=0, Type=typing.Union[Nullable, bytes]),
                    ])

            presetHandle: typing.Union[Nullable, bytes] = NullValue

        @dataclass
        class AddThermostatSuggestion(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'AddThermostatSuggestionResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="presetHandle", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="effectiveTime", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="expirationInMinutes", Tag=2, Type=uint),
                    ])

            presetHandle: bytes = b""
            effectiveTime: typing.Union[Nullable, uint] = NullValue
            expirationInMinutes: uint = 0

        @dataclass
        class RemoveThermostatSuggestion(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x00000008
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="uniqueID", Tag=0, Type=uint),
                    ])

            uniqueID: uint = 0

        @dataclass
        class AtomicRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x000000FE
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'AtomicResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="requestType", Tag=0, Type=Globals.Enums.enum8),
                        ClusterObjectFieldDescriptor(Label="attributeRequests", Tag=1, Type=typing.List[uint]),
                        ClusterObjectFieldDescriptor(Label="timeout", Tag=2, Type=typing.Optional[uint]),
                    ])

            requestType: Globals.Enums.enum8 = 0
            attributeRequests: typing.List[uint] = field(default_factory=lambda: [])
            timeout: typing.Optional[uint] = None

        @dataclass
        class AddThermostatSuggestionResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="uniqueID", Tag=0, Type=uint),
                    ])

            uniqueID: uint = 0

        @dataclass
        class AtomicResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000201
            command_id: typing.ClassVar[int] = 0x000000FD
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="statusCode", Tag=0, Type=Globals.Enums.status),
                        ClusterObjectFieldDescriptor(Label="attributeStatus", Tag=1, Type=typing.List[Globals.Structs.struct]),
                        ClusterObjectFieldDescriptor(Label="timeout", Tag=2, Type=typing.Optional[uint]),
                    ])

            statusCode: Globals.Enums.status = 0
            attributeStatus: typing.List[Globals.Structs.struct] = field(default_factory=lambda: [])
            timeout: typing.Optional[uint] = None

    class Attributes:
        LocalTemperature = _attr(__module__, __qualname__, "LocalTemperature", 0x00000201, 0x00000000, "typing.Union[Nullable, int]", NullValue)

        OutdoorTemperature = _attr(__module__, __qualname__, "OutdoorTemperature", 0x00000201, 0x00000001, "typing.Union[None, Nullable, int]", None)

        Occupancy = _attr(__module__, __qualname__, "Occupancy", 0x00000201, 0x00000002, "typing.Optional[Thermostat.Bitmaps.OccupancyBitmap]", None)

        AbsMinHeatSetpointLimit = _attr(__module__, __qualname__, "AbsMinHeatSetpointLimit", 0x00000201, 0x00000003, "typing.Optional[int]", None)

        AbsMaxHeatSetpointLimit = _attr(__module__, __qualname__, "AbsMaxHeatSetpointLimit", 0x00000201, 0x00000004, "typing.Optional[int]", None)

        AbsMinCoolSetpointLimit = _attr(__module__, __qualname__, "AbsMinCoolSetpointLimit", 0x00000201, 0x00000005, "typing.Optional[int]", None)

        AbsMaxCoolSetpointLimit = _attr(__module__, __qualname__, "AbsMaxCoolSetpointLimit", 0x00000201, 0x00000006, "typing.Optional[int]", None)

        PICoolingDemand = _attr(__module__, __qualname__, "PICoolingDemand", 0x00000201, 0x00000007, "typing.Optional[uint]", None)

        PIHeatingDemand = _attr(__module__, __qualname__, "PIHeatingDemand", 0x00000201, 0x00000008, "typing.Optional[uint]", None)

        HVACSystemTypeConfiguration = _attr(__module__, __qualname__, "HVACSystemTypeConfiguration", 0x00000201, 0x00000009, "typing.Optional[uint]", None)

        LocalTemperatureCalibration = _attr(__module__, __qualname__, "LocalTemperatureCalibration", 0x00000201, 0x00000010, "typing.Optional[int]", None)

        OccupiedCoolingSetpoint = _attr(__module__, __qualname__, "OccupiedCoolingSetpoint", 0x00000201, 0x00000011, "typing.Optional[int]", None)

        OccupiedHeatingSetpoint = _attr(__module__, __qualname__, "OccupiedHeatingSetpoint", 0x00000201, 0x00000012, "typing.Optional[int]", None)

        UnoccupiedCoolingSetpoint = _attr(__module__, __qualname__, "UnoccupiedCoolingSetpoint", 0x00000201, 0x00000013, "typing.Optional[int]", None)

        UnoccupiedHeatingSetpoint = _attr(__module__, __qualname__, "UnoccupiedHeatingSetpoint", 0x00000201, 0x00000014, "typing.Optional[int]", None)

        MinHeatSetpointLimit = _attr(__module__, __qualname__, "MinHeatSetpointLimit", 0x00000201, 0x00000015, "typing.Optional[int]", None)

        MaxHeatSetpointLimit = _attr(__module__, __qualname__, "MaxHeatSetpointLimit", 0x00000201, 0x00000016, "typing.Optional[int]", None)

        MinCoolSetpointLimit = _attr(__module__, __qualname__, "MinCoolSetpointLimit", 0x00000201, 0x00000017, "typing.Optional[int]", None)

        MaxCoolSetpointLimit = _attr(__module__, __qualname__, "MaxCoolSetpointLimit", 0x00000201, 0x00000018, "typing.Optional[int]", None)

        MinSetpointDeadBand = _attr(__module__, __qualname__, "MinSetpointDeadBand", 0x00000201, 0x00000019, "typing.Optional[int]", None)

        RemoteSensing = _attr(__module__, __qualname__, "RemoteSensing", 0x00000201, 0x0000001A, "typing.Optional[Thermostat.Bitmaps.RemoteSensingBitmap]", None)

        ControlSequenceOfOperation = _attr(__module__, __qualname__, "ControlSequenceOfOperation", 0x00000201, 0x0000001B, "Thermostat.Enums.ControlSequenceOfOperationEnum", 0)

        SystemMode = _attr(__module__, __qualname__, "SystemMode", 0x00000201, 0x0000001C, "Thermostat.Enums.SystemModeEnum", 0)

        ThermostatRunningMode = _attr(__module__, __qualname__, "ThermostatRunningMode", 0x00000201, 0x0000001E, "typing.Optional[Thermostat.Enums.ThermostatRunningModeEnum]", None)

        TemperatureSetpointHold = _attr(__module__, __qualname__, "TemperatureSetpointHold", 0x00000201, 0x00000023, "typing.Optional[Thermostat.Enums.TemperatureSetpointHoldEnum]", None)

        TemperatureSetpointHoldDuration = _attr(__module__, __qualname__, "TemperatureSetpointHoldDuration", 0x00000201, 0x00000024, "typing.Union[None, Nullable, uint]", None)

        ThermostatProgrammingOperationMode = _attr(__module__, __qualname__, "ThermostatProgrammingOperationMode", 0x00000201, 0x00000025, "typing.Optional[uint]", None)

        ThermostatRunningState = _attr(__module__, __qualname__, "ThermostatRunningState", 0x00000201, 0x00000029, "typing.Optional[Thermostat.Bitmaps.RelayStateBitmap]", None)

        SetpointChangeSource = _attr(__module__, __qualname__, "SetpointChangeSource", 0x00000201, 0x00000030, "typing.Optional[Thermostat.Enums.SetpointChangeSourceEnum]", None)

        SetpointChangeAmount = _attr(__module__, __qualname__, "SetpointChangeAmount", 0x00000201, 0x00000031, "typing.Union[None, Nullable, int]", None)

        SetpointChangeSourceTimestamp = _attr(__module__, __qualname__, "SetpointChangeSourceTimestamp", 0x00000201, 0x00000032, "typing.Optional[uint]", None)

        OccupiedSetback = _attr(__module__, __qualname__, "OccupiedSetback", 0x00000201, 0x00000034, "typing.Optional[uint]", None)

        OccupiedSetbackMin = _attr(__module__, __qualname__, "OccupiedSetbackMin", 0x00000201, 0x00000035, "typing.Optional[uint]", None)

        OccupiedSetbackMax = _attr(__module__, __qualname__, "OccupiedSetbackMax", 0x00000201, 0x00000036, "typing.Optional[uint]", None)

        UnoccupiedSetback = _attr(__module__, __qualname__, "UnoccupiedSetback", 0x00000201, 0x00000037, "typing.Optional[uint]", None)

        UnoccupiedSetbackMin = _attr(__module__, __qualname__, "UnoccupiedSetbackMin", 0x00000201, 0x00000038, "typing.Optional[uint]", None)

        UnoccupiedSetbackMax = _attr(__module__, __qualname__, "UnoccupiedSetbackMax", 0x00000201, 0x00000039, "typing.Optional[uint]", None)

        EmergencyHeatDelta = _attr(__module__, __qualname__, "EmergencyHeatDelta", 0x00000201, 0x0000003A, "typing.Optional[uint]", None)

        ACType = _attr(__module__, __qualname__, "ACType", 0x00000201, 0x00000040, "typing.Optional[Thermostat.Enums.ACTypeEnum]", None)

        ACCapacity = _attr(__module__, __qualname__, "ACCapacity", 0x00000201, 0x00000041, "typing.Optional[uint]", None)

        ACRefrigerantType = _attr(__module__, __qualname__, "ACRefrigerantType", 0x00000201, 0x00000042, "typing.Optional[Thermostat.Enums.ACRefrigerantTypeEnum]", None)

        ACCompressorType = _attr(__module__, __qualname__, "ACCompressorType", 0x00000201, 0x00000043, "typing.Optional[Thermostat.Enums.ACCompressorTypeEnum]", None)

        ACErrorCode = _attr(__module__, __qualname__, "ACErrorCode", 0x00000201, 0x00000044, "typing.Optional[Thermostat.Bitmaps.ACErrorCodeBitmap]", None)

        ACLouverPosition = _attr(__module__, __qualname__, "ACLouverPosition", 0x00000201, 0x00000045, "typing.Optional[Thermostat.Enums.ACLouverPositionEnum]", None)

        ACCoilTemperature = _attr(__module__, __qualname__, "ACCoilTemperature", 0x00000201, 0x00000046, "typing.Union[None, Nullable, int]", None)

        ACCapacityformat = _attr(__module__, __qualname__, "ACCapacityformat", 0x00000201, 0x00000047, "typing.Optional[Thermostat.Enums.ACCapacityFormatEnum]", None)

        PresetTypes = _attr(__module__, __qualname__, "PresetTypes", 0x00000201, 0x00000048, "typing.Optional[typing.List[Thermostat.Structs.PresetTypeStruct]]", None)

        ScheduleTypes = _attr(__module__, __qualname__, "ScheduleTypes", 0x00000201, 0x00000049, "typing.Optional[typing.List[Thermostat.Structs.ScheduleTypeStruct]]", None)

        NumberOfPresets = _attr(__module__, __qualname__, "NumberOfPresets", 0x00000201, 0x0000004A, "typing.Optional[uint]", None)

        NumberOfSchedules = _attr(__module__, __qualname__, "NumberOfSchedules", 0x00000201, 0x0000004B, "typing.Optional[uint]", None)

        NumberOfScheduleTransitions = _attr(__module__, __qualname__, "NumberOfScheduleTransitions", 0x00000201, 0x0000004C, "typing.Optional[uint]", None)

        NumberOfScheduleTransitionPerDay = _attr(__module__, __qualname__, "NumberOfScheduleTransitionPerDay", 0x00000201, 0x0000004D, "typing.Union[None, Nullable, uint]", None)

        ActivePresetHandle = _attr(__module__, __qualname__, "ActivePresetHandle", 0x00000201, 0x0000004E, "typing.Union[None, Nullable, bytes]", None)

        ActiveScheduleHandle = _attr(__module__, __qualname__, "ActiveScheduleHandle", 0x00000201, 0x0000004F, "typing.Union[None, Nullable, bytes]", None)

        Presets = _attr(__module__, __qualname__, "Presets", 0x00000201, 0x00000050, "typing.Optional[typing.List[Thermostat.Structs.PresetStruct]]", None)

        Schedules = _attr(__module__, __qualname__, "Schedules", 0x00000201, 0x00000051, "typing.Optional[typing.List[Thermostat.Structs.ScheduleStruct]]", None)

        SetpointHoldExpiryTimestamp = _attr(__module__, __qualname__, "SetpointHoldExpiryTimestamp", 0x00000201, 0x00000052, "typing.Union[None, Nullable, uint]", None)

        MaxThermostatSuggestions = _attr(__module__, __qualname__, "MaxThermostatSuggestions", 0x00000201, 0x00000053, "typing.Optional[uint]", None)

        ThermostatSuggestions = _attr(__module__, __qualname__, "ThermostatSuggestions", 0x00000201, 0x00000054, "typing.Optional[typing.List[Thermostat.Structs.ThermostatSuggestionStruct]]", None)

        CurrentThermostatSuggestion = _attr(__module__, __qualname__, "CurrentThermostatSuggestion", 0x00000201, 0x00000055, "typing.Union[None, Nullable, Thermostat.Structs.ThermostatSuggestionStruct]", None)

        ThermostatSuggestionNotFollowingReason = _attr(__module__, __qualname__, "ThermostatSuggestionNotFollowingReason", 0x00000201, 0x00000056, "typing.Union[None, Nullable, Thermostat.Bitmaps.ThermostatSuggestionNotFollowingReasonBitmap]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000201, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000201, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000201, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000201, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000201, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class SystemModeChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousSystemMode", Tag=0, Type=typing.Optional[Thermostat.Enums.SystemModeEnum]),
                        ClusterObjectFieldDescriptor(Label="currentSystemMode", Tag=1, Type=Thermostat.Enums.SystemModeEnum),
                    ])

            previousSystemMode: typing.Optional[Thermostat.Enums.SystemModeEnum] = None
            currentSystemMode: Thermostat.Enums.SystemModeEnum = 0

        @dataclass
        class LocalTemperatureChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="currentLocalTemperature", Tag=0, Type=typing.Union[Nullable, int]),
                    ])

            currentLocalTemperature: typing.Union[Nullable, int] = NullValue

        @dataclass
        class OccupancyChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000002

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousOccupancy", Tag=0, Type=typing.Optional[Thermostat.Bitmaps.OccupancyBitmap]),
                        ClusterObjectFieldDescriptor(Label="currentOccupancy", Tag=1, Type=Thermostat.Bitmaps.OccupancyBitmap),
                    ])

            previousOccupancy: typing.Optional[Thermostat.Bitmaps.OccupancyBitmap] = None
            currentOccupancy: Thermostat.Bitmaps.OccupancyBitmap = 0

        @dataclass
        class SetpointChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000003

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="systemMode", Tag=0, Type=Thermostat.Enums.SystemModeEnum),
                        ClusterObjectFieldDescriptor(Label="occupancy", Tag=1, Type=typing.Optional[Thermostat.Bitmaps.OccupancyBitmap]),
                        ClusterObjectFieldDescriptor(Label="previousSetpoint", Tag=2, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="currentSetpoint", Tag=3, Type=int),
                    ])

            systemMode: Thermostat.Enums.SystemModeEnum = 0
            occupancy: typing.Optional[Thermostat.Bitmaps.OccupancyBitmap] = None
            previousSetpoint: typing.Optional[int] = None
            currentSetpoint: int = 0

        @dataclass
        class RunningStateChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000004

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousRunningState", Tag=0, Type=typing.Optional[Thermostat.Bitmaps.RelayStateBitmap]),
                        ClusterObjectFieldDescriptor(Label="currentRunningState", Tag=1, Type=Thermostat.Bitmaps.RelayStateBitmap),
                    ])

            previousRunningState: typing.Optional[Thermostat.Bitmaps.RelayStateBitmap] = None
            currentRunningState: Thermostat.Bitmaps.RelayStateBitmap = 0

        @dataclass
        class RunningModeChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000005

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousRunningMode", Tag=0, Type=typing.Optional[Thermostat.Enums.ThermostatRunningModeEnum]),
                        ClusterObjectFieldDescriptor(Label="currentRunningMode", Tag=1, Type=Thermostat.Enums.ThermostatRunningModeEnum),
                    ])

            previousRunningMode: typing.Optional[Thermostat.Enums.ThermostatRunningModeEnum] = None
            currentRunningMode: Thermostat.Enums.ThermostatRunningModeEnum = 0

        @dataclass
        class ActiveScheduleChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000006

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousScheduleHandle", Tag=0, Type=typing.Union[None, Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="currentScheduleHandle", Tag=1, Type=typing.Union[Nullable, bytes]),
                    ])

            previousScheduleHandle: typing.Union[None, Nullable, bytes] = None
            currentScheduleHandle: typing.Union[Nullable, bytes] = NullValue

        @dataclass
        class ActivePresetChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000201

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000007

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="previousPresetHandle", Tag=0, Type=typing.Union[None, Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="currentPresetHandle", Tag=1, Type=typing.Union[Nullable, bytes]),
                    ])

            previousPresetHandle: typing.Union[None, Nullable, bytes] = None
            currentPresetHandle: typing.Union[Nullable, bytes] = NullValue
