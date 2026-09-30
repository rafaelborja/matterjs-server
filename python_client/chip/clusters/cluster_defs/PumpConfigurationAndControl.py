"""PumpConfigurationAndControl cluster definition (auto-generated, DO NOT edit)."""

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
class PumpConfigurationAndControl(Cluster):
    id: typing.ClassVar[int] = 0x00000200

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="maxPressure", Tag=0x00000000, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="maxSpeed", Tag=0x00000001, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="maxFlow", Tag=0x00000002, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="minConstPressure", Tag=0x00000003, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="maxConstPressure", Tag=0x00000004, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="minCompPressure", Tag=0x00000005, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="maxCompPressure", Tag=0x00000006, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="minConstSpeed", Tag=0x00000007, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="maxConstSpeed", Tag=0x00000008, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="minConstFlow", Tag=0x00000009, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="maxConstFlow", Tag=0x0000000A, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="minConstTemp", Tag=0x0000000B, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="maxConstTemp", Tag=0x0000000C, Type=typing.Union[None, Nullable, int]),
                ClusterObjectFieldDescriptor(Label="pumpStatus", Tag=0x00000010, Type=typing.Optional[PumpConfigurationAndControl.Bitmaps.PumpStatusBitmap]),
                ClusterObjectFieldDescriptor(Label="effectiveOperationMode", Tag=0x00000011, Type=PumpConfigurationAndControl.Enums.OperationModeEnum),
                ClusterObjectFieldDescriptor(Label="effectiveControlMode", Tag=0x00000012, Type=PumpConfigurationAndControl.Enums.ControlModeEnum),
                ClusterObjectFieldDescriptor(Label="capacity", Tag=0x00000013, Type=typing.Union[Nullable, int]),
                ClusterObjectFieldDescriptor(Label="speed", Tag=0x00000014, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="lifetimeRunningHours", Tag=0x00000015, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="power", Tag=0x00000016, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="lifetimeEnergyConsumed", Tag=0x00000017, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="operationMode", Tag=0x00000020, Type=PumpConfigurationAndControl.Enums.OperationModeEnum),
                ClusterObjectFieldDescriptor(Label="controlMode", Tag=0x00000021, Type=typing.Optional[PumpConfigurationAndControl.Enums.ControlModeEnum]),
                ClusterObjectFieldDescriptor(Label="alarmMask", Tag=0x00000022, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    maxPressure: typing.Union[Nullable, int] = NullValue
    maxSpeed: typing.Union[Nullable, uint] = NullValue
    maxFlow: typing.Union[Nullable, uint] = NullValue
    minConstPressure: typing.Union[None, Nullable, int] = None
    maxConstPressure: typing.Union[None, Nullable, int] = None
    minCompPressure: typing.Union[None, Nullable, int] = None
    maxCompPressure: typing.Union[None, Nullable, int] = None
    minConstSpeed: typing.Union[None, Nullable, uint] = None
    maxConstSpeed: typing.Union[None, Nullable, uint] = None
    minConstFlow: typing.Union[None, Nullable, uint] = None
    maxConstFlow: typing.Union[None, Nullable, uint] = None
    minConstTemp: typing.Union[None, Nullable, int] = None
    maxConstTemp: typing.Union[None, Nullable, int] = None
    pumpStatus: typing.Optional[PumpConfigurationAndControl.Bitmaps.PumpStatusBitmap] = None
    effectiveOperationMode: PumpConfigurationAndControl.Enums.OperationModeEnum = 0
    effectiveControlMode: PumpConfigurationAndControl.Enums.ControlModeEnum = 0
    capacity: typing.Union[Nullable, int] = NullValue
    speed: typing.Union[None, Nullable, uint] = None
    lifetimeRunningHours: typing.Union[None, Nullable, uint] = None
    power: typing.Union[None, Nullable, uint] = None
    lifetimeEnergyConsumed: typing.Union[None, Nullable, uint] = None
    operationMode: PumpConfigurationAndControl.Enums.OperationModeEnum = 0
    controlMode: typing.Optional[PumpConfigurationAndControl.Enums.ControlModeEnum] = None
    alarmMask: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class OperationModeEnum(MatterIntEnum):
            kNormal = 0x00
            kMinimum = 0x01
            kMaximum = 0x02
            kLocal = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class ControlModeEnum(MatterIntEnum):
            kConstantSpeed = 0x00
            kConstantPressure = 0x01
            kProportionalPressure = 0x02
            kConstantFlow = 0x03
            kConstantTemperature = 0x05
            kAutomatic = 0x07
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 8

    class Bitmaps:
        class Feature(IntFlag):
            kConstantPressure = 0x1
            kCompensatedPressure = 0x2
            kConstantFlow = 0x4
            kConstantSpeed = 0x8
            kConstantTemperature = 0x10
            kAutomatic = 0x20
            kLocalOperation = 0x40

        class PumpStatusBitmap(IntFlag):
            kDeviceFault = 0x1
            kSupplyFault = 0x2
            kSpeedLow = 0x4
            kSpeedHigh = 0x8
            kLocalOverride = 0x10
            kRunning = 0x20
            kRemotePressure = 0x40
            kRemoteFlow = 0x80
            kRemoteTemperature = 0x100

    class Attributes:
        MaxPressure = _attr(__module__, __qualname__, "MaxPressure", 0x00000200, 0x00000000, "typing.Union[Nullable, int]", NullValue)

        MaxSpeed = _attr(__module__, __qualname__, "MaxSpeed", 0x00000200, 0x00000001, "typing.Union[Nullable, uint]", NullValue)

        MaxFlow = _attr(__module__, __qualname__, "MaxFlow", 0x00000200, 0x00000002, "typing.Union[Nullable, uint]", NullValue)

        MinConstPressure = _attr(__module__, __qualname__, "MinConstPressure", 0x00000200, 0x00000003, "typing.Union[None, Nullable, int]", None)

        MaxConstPressure = _attr(__module__, __qualname__, "MaxConstPressure", 0x00000200, 0x00000004, "typing.Union[None, Nullable, int]", None)

        MinCompPressure = _attr(__module__, __qualname__, "MinCompPressure", 0x00000200, 0x00000005, "typing.Union[None, Nullable, int]", None)

        MaxCompPressure = _attr(__module__, __qualname__, "MaxCompPressure", 0x00000200, 0x00000006, "typing.Union[None, Nullable, int]", None)

        MinConstSpeed = _attr(__module__, __qualname__, "MinConstSpeed", 0x00000200, 0x00000007, "typing.Union[None, Nullable, uint]", None)

        MaxConstSpeed = _attr(__module__, __qualname__, "MaxConstSpeed", 0x00000200, 0x00000008, "typing.Union[None, Nullable, uint]", None)

        MinConstFlow = _attr(__module__, __qualname__, "MinConstFlow", 0x00000200, 0x00000009, "typing.Union[None, Nullable, uint]", None)

        MaxConstFlow = _attr(__module__, __qualname__, "MaxConstFlow", 0x00000200, 0x0000000A, "typing.Union[None, Nullable, uint]", None)

        MinConstTemp = _attr(__module__, __qualname__, "MinConstTemp", 0x00000200, 0x0000000B, "typing.Union[None, Nullable, int]", None)

        MaxConstTemp = _attr(__module__, __qualname__, "MaxConstTemp", 0x00000200, 0x0000000C, "typing.Union[None, Nullable, int]", None)

        PumpStatus = _attr(__module__, __qualname__, "PumpStatus", 0x00000200, 0x00000010, "typing.Optional[PumpConfigurationAndControl.Bitmaps.PumpStatusBitmap]", None)

        EffectiveOperationMode = _attr(__module__, __qualname__, "EffectiveOperationMode", 0x00000200, 0x00000011, "PumpConfigurationAndControl.Enums.OperationModeEnum", 0)

        EffectiveControlMode = _attr(__module__, __qualname__, "EffectiveControlMode", 0x00000200, 0x00000012, "PumpConfigurationAndControl.Enums.ControlModeEnum", 0)

        Capacity = _attr(__module__, __qualname__, "Capacity", 0x00000200, 0x00000013, "typing.Union[Nullable, int]", NullValue)

        Speed = _attr(__module__, __qualname__, "Speed", 0x00000200, 0x00000014, "typing.Union[None, Nullable, uint]", None)

        LifetimeRunningHours = _attr(__module__, __qualname__, "LifetimeRunningHours", 0x00000200, 0x00000015, "typing.Union[None, Nullable, uint]", None)

        Power = _attr(__module__, __qualname__, "Power", 0x00000200, 0x00000016, "typing.Union[None, Nullable, uint]", None)

        LifetimeEnergyConsumed = _attr(__module__, __qualname__, "LifetimeEnergyConsumed", 0x00000200, 0x00000017, "typing.Union[None, Nullable, uint]", None)

        OperationMode = _attr(__module__, __qualname__, "OperationMode", 0x00000200, 0x00000020, "PumpConfigurationAndControl.Enums.OperationModeEnum", 0)

        ControlMode = _attr(__module__, __qualname__, "ControlMode", 0x00000200, 0x00000021, "typing.Optional[PumpConfigurationAndControl.Enums.ControlModeEnum]", None)

        AlarmMask = _attr(__module__, __qualname__, "AlarmMask", 0x00000200, 0x00000022, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000200, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000200, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000200, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000200, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000200, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class SupplyVoltageLow(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class SupplyVoltageHigh(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class PowerMissingPhase(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000002

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class SystemPressureLow(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000003

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class SystemPressureHigh(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000004

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class DryRunning(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000005

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class MotorTemperatureHigh(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000006

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class PumpMotorFatalFailure(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000007

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class ElectronicTemperatureHigh(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000008

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class PumpBlocked(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000009

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class SensorFailure(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x0000000A

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class ElectronicNonFatalFailure(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x0000000B

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class ElectronicFatalFailure(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x0000000C

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class GeneralFault(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x0000000D

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class Leakage(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x0000000E

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class AirDetection(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x0000000F

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class TurbineOperation(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000200

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000010

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])

