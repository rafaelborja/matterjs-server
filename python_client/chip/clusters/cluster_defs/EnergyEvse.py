"""EnergyEvse cluster definition (auto-generated, DO NOT edit)."""

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
class EnergyEvse(Cluster):
    id: typing.ClassVar[int] = 0x00000099

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="state", Tag=0x00000000, Type=typing.Union[Nullable, EnergyEvse.Enums.StateEnum]),
                ClusterObjectFieldDescriptor(Label="supplyState", Tag=0x00000001, Type=EnergyEvse.Enums.SupplyStateEnum),
                ClusterObjectFieldDescriptor(Label="faultState", Tag=0x00000002, Type=EnergyEvse.Enums.FaultStateEnum),
                ClusterObjectFieldDescriptor(Label="chargingEnabledUntil", Tag=0x00000003, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="dischargingEnabledUntil", Tag=0x00000004, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="circuitCapacity", Tag=0x00000005, Type=int),
                ClusterObjectFieldDescriptor(Label="minimumChargeCurrent", Tag=0x00000006, Type=int),
                ClusterObjectFieldDescriptor(Label="maximumChargeCurrent", Tag=0x00000007, Type=int),
                ClusterObjectFieldDescriptor(Label="maximumDischargeCurrent", Tag=0x00000008, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="userMaximumChargeCurrent", Tag=0x00000009, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="randomizationDelayWindow", Tag=0x0000000A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="nextChargeStartTime", Tag=0x00000023, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="nextChargeTargetTime", Tag=0x00000024, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="nextChargeRequiredEnergy", Tag=0x00000025, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="nextChargeTargetSoC", Tag=0x00000026, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="approximateEVEfficiency", Tag=0x00000027, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="stateOfCharge", Tag=0x00000030, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="batteryCapacity", Tag=0x00000031, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="vehicleID", Tag=0x00000032, Type=typing.Union[None, Nullable, str]),
                ClusterObjectFieldDescriptor(Label="sessionID", Tag=0x00000040, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="sessionDuration", Tag=0x00000041, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="sessionEnergyCharged", Tag=0x00000042, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="sessionEnergyDischarged", Tag=0x00000043, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    state: typing.Union[Nullable, EnergyEvse.Enums.StateEnum] = NullValue
    supplyState: EnergyEvse.Enums.SupplyStateEnum = 0
    faultState: EnergyEvse.Enums.FaultStateEnum = 0
    chargingEnabledUntil: typing.Union[Nullable, uint] = NullValue
    dischargingEnabledUntil: typing.Union[None, Nullable, uint] = None
    circuitCapacity: int = 0
    minimumChargeCurrent: int = 0
    maximumChargeCurrent: int = 0
    maximumDischargeCurrent: typing.Optional[int] = None
    userMaximumChargeCurrent: typing.Optional[int] = None
    randomizationDelayWindow: typing.Optional[uint] = None
    nextChargeStartTime: typing.Union[None, Nullable, uint] = None
    nextChargeTargetTime: typing.Union[None, Nullable, uint] = None
    nextChargeRequiredEnergy: typing.Union[None, Nullable, int] = None
    nextChargeTargetSoC: typing.Union[None, Nullable, uint] = None
    approximateEVEfficiency: typing.Union[None, Nullable, uint] = None
    stateOfCharge: typing.Union[None, Nullable, uint] = None
    batteryCapacity: typing.Union[None, Nullable, int] = None
    vehicleID: typing.Union[None, Nullable, str] = None
    sessionID: typing.Union[Nullable, uint] = NullValue
    sessionDuration: typing.Union[Nullable, uint] = NullValue
    sessionEnergyCharged: typing.Union[Nullable, int] = NullValue
    sessionEnergyDischarged: typing.Union[None, Nullable, int] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class StateEnum(MatterIntEnum):
            kNotPluggedIn = 0x00
            kPluggedInNoDemand = 0x01
            kPluggedInDemand = 0x02
            kPluggedInCharging = 0x03
            kPluggedInDischarging = 0x04
            kSessionEnding = 0x05
            kFault = 0x06
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 7

        class SupplyStateEnum(MatterIntEnum):
            kDisabled = 0x00
            kChargingEnabled = 0x01
            kDischargingEnabled = 0x02
            kDisabledError = 0x03
            kDisabledDiagnostics = 0x04
            kEnabled = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

        class FaultStateEnum(MatterIntEnum):
            kNoError = 0x00
            kMeterFailure = 0x01
            kOverVoltage = 0x02
            kUnderVoltage = 0x03
            kOverCurrent = 0x04
            kContactWetFailure = 0x05
            kContactDryFailure = 0x06
            kGroundFault = 0x07
            kPowerLoss = 0x08
            kPowerQuality = 0x09
            kPilotShortCircuit = 0x0A
            kEmergencyStop = 0x0B
            kEVDisconnected = 0x0C
            kWrongPowerSupply = 0x0D
            kLiveNeutralSwap = 0x0E
            kOverTemperature = 0x0F
            kOther = 0xFF
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 256

        class EnergyTransferStoppedReasonEnum(MatterIntEnum):
            kEVStopped = 0x00
            kEVSEStopped = 0x01
            kOther = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

    class Bitmaps:
        class Feature(IntFlag):
            kChargingPreferences = 0x1
            kSoCReporting = 0x2
            kPlugAndCharge = 0x4
            kRfid = 0x8
            kV2x = 0x10

        class TargetDayOfWeekBitmap(IntFlag):
            kSunday = 0x1
            kMonday = 0x2
            kTuesday = 0x4
            kWednesday = 0x8
            kThursday = 0x10
            kFriday = 0x20
            kSaturday = 0x40

    class Structs:
        @dataclass
        class ChargingTargetStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="targetTimeMinutesPastMidnight", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="targetSoC", Tag=1, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="addedEnergy", Tag=2, Type=typing.Optional[int]),
                    ])

            targetTimeMinutesPastMidnight: uint = 0
            targetSoC: typing.Optional[uint] = None
            addedEnergy: typing.Optional[int] = None

        @dataclass
        class ChargingTargetScheduleStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dayOfWeekForSequence", Tag=0, Type=EnergyEvse.Bitmaps.TargetDayOfWeekBitmap),
                        ClusterObjectFieldDescriptor(Label="chargingTargets", Tag=1, Type=typing.List[EnergyEvse.Structs.ChargingTargetStruct]),
                    ])

            dayOfWeekForSequence: EnergyEvse.Bitmaps.TargetDayOfWeekBitmap = 0
            chargingTargets: typing.List[EnergyEvse.Structs.ChargingTargetStruct] = field(default_factory=lambda: [])

    class Commands:
        @dataclass
        class Disable(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class EnableCharging(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="chargingEnabledUntil", Tag=0, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="minimumChargeCurrent", Tag=1, Type=int),
                        ClusterObjectFieldDescriptor(Label="maximumChargeCurrent", Tag=2, Type=int),
                    ])

            chargingEnabledUntil: typing.Union[Nullable, uint] = NullValue
            minimumChargeCurrent: int = 0
            maximumChargeCurrent: int = 0

        @dataclass
        class EnableDischarging(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dischargingEnabledUntil", Tag=0, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="maximumDischargeCurrent", Tag=1, Type=int),
                    ])

            dischargingEnabledUntil: typing.Union[Nullable, uint] = NullValue
            maximumDischargeCurrent: int = 0

        @dataclass
        class StartDiagnostics(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class SetTargets(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="chargingTargetSchedules", Tag=0, Type=typing.List[EnergyEvse.Structs.ChargingTargetScheduleStruct]),
                    ])

            chargingTargetSchedules: typing.List[EnergyEvse.Structs.ChargingTargetScheduleStruct] = field(default_factory=lambda: [])

        @dataclass
        class GetTargets(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'GetTargetsResponse'

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class ClearTargets(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class GetTargetsResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000099
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="chargingTargetSchedules", Tag=0, Type=typing.List[EnergyEvse.Structs.ChargingTargetScheduleStruct]),
                    ])

            chargingTargetSchedules: typing.List[EnergyEvse.Structs.ChargingTargetScheduleStruct] = field(default_factory=lambda: [])

    class Attributes:
        State = _attr(__module__, __qualname__, "State", 0x00000099, 0x00000000, "typing.Union[Nullable, EnergyEvse.Enums.StateEnum]", NullValue)

        SupplyState = _attr(__module__, __qualname__, "SupplyState", 0x00000099, 0x00000001, "EnergyEvse.Enums.SupplyStateEnum", 0)

        FaultState = _attr(__module__, __qualname__, "FaultState", 0x00000099, 0x00000002, "EnergyEvse.Enums.FaultStateEnum", 0)

        ChargingEnabledUntil = _attr(__module__, __qualname__, "ChargingEnabledUntil", 0x00000099, 0x00000003, "typing.Union[Nullable, uint]", NullValue)

        DischargingEnabledUntil = _attr(__module__, __qualname__, "DischargingEnabledUntil", 0x00000099, 0x00000004, "typing.Union[None, Nullable, uint]", None)

        CircuitCapacity = _attr(__module__, __qualname__, "CircuitCapacity", 0x00000099, 0x00000005, "int", 0)

        MinimumChargeCurrent = _attr(__module__, __qualname__, "MinimumChargeCurrent", 0x00000099, 0x00000006, "int", 0)

        MaximumChargeCurrent = _attr(__module__, __qualname__, "MaximumChargeCurrent", 0x00000099, 0x00000007, "int", 0)

        MaximumDischargeCurrent = _attr(__module__, __qualname__, "MaximumDischargeCurrent", 0x00000099, 0x00000008, "typing.Optional[int]", None)

        UserMaximumChargeCurrent = _attr(__module__, __qualname__, "UserMaximumChargeCurrent", 0x00000099, 0x00000009, "typing.Optional[int]", None)

        RandomizationDelayWindow = _attr(__module__, __qualname__, "RandomizationDelayWindow", 0x00000099, 0x0000000A, "typing.Optional[uint]", None)

        NextChargeStartTime = _attr(__module__, __qualname__, "NextChargeStartTime", 0x00000099, 0x00000023, "typing.Union[None, Nullable, uint]", None)

        NextChargeTargetTime = _attr(__module__, __qualname__, "NextChargeTargetTime", 0x00000099, 0x00000024, "typing.Union[None, Nullable, uint]", None)

        NextChargeRequiredEnergy = _attr(__module__, __qualname__, "NextChargeRequiredEnergy", 0x00000099, 0x00000025, "typing.Union[None, Nullable, int]", None)

        NextChargeTargetSoC = _attr(__module__, __qualname__, "NextChargeTargetSoC", 0x00000099, 0x00000026, "typing.Union[None, Nullable, uint]", None)

        ApproximateEVEfficiency = _attr(__module__, __qualname__, "ApproximateEVEfficiency", 0x00000099, 0x00000027, "typing.Union[None, Nullable, uint]", None)

        StateOfCharge = _attr(__module__, __qualname__, "StateOfCharge", 0x00000099, 0x00000030, "typing.Union[None, Nullable, uint]", None)

        BatteryCapacity = _attr(__module__, __qualname__, "BatteryCapacity", 0x00000099, 0x00000031, "typing.Union[None, Nullable, int]", None)

        VehicleID = _attr(__module__, __qualname__, "VehicleID", 0x00000099, 0x00000032, "typing.Union[None, Nullable, str]", None)

        SessionID = _attr(__module__, __qualname__, "SessionID", 0x00000099, 0x00000040, "typing.Union[Nullable, uint]", NullValue)

        SessionDuration = _attr(__module__, __qualname__, "SessionDuration", 0x00000099, 0x00000041, "typing.Union[Nullable, uint]", NullValue)

        SessionEnergyCharged = _attr(__module__, __qualname__, "SessionEnergyCharged", 0x00000099, 0x00000042, "typing.Union[Nullable, int]", NullValue)

        SessionEnergyDischarged = _attr(__module__, __qualname__, "SessionEnergyDischarged", 0x00000099, 0x00000043, "typing.Union[None, Nullable, int]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000099, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000099, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000099, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000099, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000099, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class EVConnected(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000099

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="sessionID", Tag=0, Type=uint),
                    ])

            sessionID: uint = 0

        @dataclass
        class EVNotDetected(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000099

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="sessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="state", Tag=1, Type=EnergyEvse.Enums.StateEnum),
                        ClusterObjectFieldDescriptor(Label="sessionDuration", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="sessionEnergyCharged", Tag=3, Type=int),
                        ClusterObjectFieldDescriptor(Label="sessionEnergyDischarged", Tag=4, Type=typing.Optional[int]),
                    ])

            sessionID: uint = 0
            state: EnergyEvse.Enums.StateEnum = 0
            sessionDuration: uint = 0
            sessionEnergyCharged: int = 0
            sessionEnergyDischarged: typing.Optional[int] = None

        @dataclass
        class EnergyTransferStarted(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000099

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000002

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="sessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="state", Tag=1, Type=EnergyEvse.Enums.StateEnum),
                        ClusterObjectFieldDescriptor(Label="maximumCurrent", Tag=2, Type=int),
                        ClusterObjectFieldDescriptor(Label="maximumDischargeCurrent", Tag=3, Type=typing.Optional[int]),
                    ])

            sessionID: uint = 0
            state: EnergyEvse.Enums.StateEnum = 0
            maximumCurrent: int = 0
            maximumDischargeCurrent: typing.Optional[int] = None

        @dataclass
        class EnergyTransferStopped(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000099

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000003

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="sessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="state", Tag=1, Type=EnergyEvse.Enums.StateEnum),
                        ClusterObjectFieldDescriptor(Label="reason", Tag=2, Type=EnergyEvse.Enums.EnergyTransferStoppedReasonEnum),
                        ClusterObjectFieldDescriptor(Label="energyTransferred", Tag=4, Type=int),
                        ClusterObjectFieldDescriptor(Label="energyDischarged", Tag=5, Type=typing.Optional[int]),
                    ])

            sessionID: uint = 0
            state: EnergyEvse.Enums.StateEnum = 0
            reason: EnergyEvse.Enums.EnergyTransferStoppedReasonEnum = 0
            energyTransferred: int = 0
            energyDischarged: typing.Optional[int] = None

        @dataclass
        class Fault(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000099

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000004

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="sessionID", Tag=0, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="state", Tag=1, Type=EnergyEvse.Enums.StateEnum),
                        ClusterObjectFieldDescriptor(Label="faultStatePreviousState", Tag=2, Type=EnergyEvse.Enums.FaultStateEnum),
                        ClusterObjectFieldDescriptor(Label="faultStateCurrentState", Tag=4, Type=EnergyEvse.Enums.FaultStateEnum),
                    ])

            sessionID: typing.Union[Nullable, uint] = NullValue
            state: EnergyEvse.Enums.StateEnum = 0
            faultStatePreviousState: EnergyEvse.Enums.FaultStateEnum = 0
            faultStateCurrentState: EnergyEvse.Enums.FaultStateEnum = 0

        @dataclass
        class Rfid(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000099

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000005

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="uid", Tag=0, Type=bytes),
                    ])

            uid: bytes = b""
