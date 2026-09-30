"""ElectricalEnergyMeasurement cluster definition (auto-generated, DO NOT edit)."""

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
class ElectricalEnergyMeasurement(Cluster):
    id: typing.ClassVar[int] = 0x00000091

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="accuracy", Tag=0x00000000, Type=Globals.Structs.MeasurementAccuracyStruct),
                ClusterObjectFieldDescriptor(Label="cumulativeEnergyImported", Tag=0x00000001, Type=typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                ClusterObjectFieldDescriptor(Label="cumulativeEnergyExported", Tag=0x00000002, Type=typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                ClusterObjectFieldDescriptor(Label="periodicEnergyImported", Tag=0x00000003, Type=typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                ClusterObjectFieldDescriptor(Label="periodicEnergyExported", Tag=0x00000004, Type=typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                ClusterObjectFieldDescriptor(Label="cumulativeEnergyReset", Tag=0x00000005, Type=typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.CumulativeEnergyResetStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    accuracy: Globals.Structs.MeasurementAccuracyStruct = field(default_factory=lambda: Globals.Structs.MeasurementAccuracyStruct())
    cumulativeEnergyImported: typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
    cumulativeEnergyExported: typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
    periodicEnergyImported: typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
    periodicEnergyExported: typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
    cumulativeEnergyReset: typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.CumulativeEnergyResetStruct] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class MeasurementTypeEnum(MatterIntEnum):
            kUnspecified = 0x00
            kVoltage = 0x01
            kActiveCurrent = 0x02
            kReactiveCurrent = 0x03
            kApparentCurrent = 0x04
            kActivePower = 0x05
            kReactivePower = 0x06
            kApparentPower = 0x07
            kRMSVoltage = 0x08
            kRMSCurrent = 0x09
            kRMSPower = 0x0A
            kFrequency = 0x0B
            kPowerFactor = 0x0C
            kNeutralCurrent = 0x0D
            kElectricalEnergy = 0x0E
            kReactiveEnergy = 0x0F
            kApparentEnergy = 0x10
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 17

    class Bitmaps:
        class Feature(IntFlag):
            kImportedEnergy = 0x1
            kExportedEnergy = 0x2
            kCumulativeEnergy = 0x4
            kPeriodicEnergy = 0x8
            kApparentEnergy = 0x10
            kReactiveEnergy = 0x20

    class Structs:
        @dataclass
        class EnergyMeasurementStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="energy", Tag=0, Type=int),
                        ClusterObjectFieldDescriptor(Label="startTimestamp", Tag=1, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="endTimestamp", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="startSystime", Tag=3, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="endSystime", Tag=4, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="apparentEnergy", Tag=5, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="reactiveEnergy", Tag=6, Type=typing.Optional[int]),
                    ])

            energy: int = 0
            startTimestamp: typing.Optional[uint] = None
            endTimestamp: typing.Optional[uint] = None
            startSystime: typing.Optional[uint] = None
            endSystime: typing.Optional[uint] = None
            apparentEnergy: typing.Optional[int] = None
            reactiveEnergy: typing.Optional[int] = None

        @dataclass
        class CumulativeEnergyResetStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="importedResetTimestamp", Tag=0, Type=typing.Union[None, Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="exportedResetTimestamp", Tag=1, Type=typing.Union[None, Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="importedResetSystime", Tag=2, Type=typing.Union[None, Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="exportedResetSystime", Tag=3, Type=typing.Union[None, Nullable, uint]),
                    ])

            importedResetTimestamp: typing.Union[None, Nullable, uint] = None
            exportedResetTimestamp: typing.Union[None, Nullable, uint] = None
            importedResetSystime: typing.Union[None, Nullable, uint] = None
            exportedResetSystime: typing.Union[None, Nullable, uint] = None

    class Attributes:
        Accuracy = _attr(__module__, __qualname__, "Accuracy", 0x00000091, 0x00000000, "Globals.Structs.MeasurementAccuracyStruct", None, "Globals.Structs.MeasurementAccuracyStruct()")

        CumulativeEnergyImported = _attr(__module__, __qualname__, "CumulativeEnergyImported", 0x00000091, 0x00000001, "typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]", None)

        CumulativeEnergyExported = _attr(__module__, __qualname__, "CumulativeEnergyExported", 0x00000091, 0x00000002, "typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]", None)

        PeriodicEnergyImported = _attr(__module__, __qualname__, "PeriodicEnergyImported", 0x00000091, 0x00000003, "typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]", None)

        PeriodicEnergyExported = _attr(__module__, __qualname__, "PeriodicEnergyExported", 0x00000091, 0x00000004, "typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]", None)

        CumulativeEnergyReset = _attr(__module__, __qualname__, "CumulativeEnergyReset", 0x00000091, 0x00000005, "typing.Union[None, Nullable, ElectricalEnergyMeasurement.Structs.CumulativeEnergyResetStruct]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000091, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000091, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000091, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000091, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000091, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class CumulativeEnergyMeasured(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000091

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="energyImported", Tag=0, Type=typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                        ClusterObjectFieldDescriptor(Label="energyExported", Tag=1, Type=typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                    ])

            energyImported: typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
            energyExported: typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None

        @dataclass
        class PeriodicEnergyMeasured(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000091

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="energyImported", Tag=0, Type=typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                        ClusterObjectFieldDescriptor(Label="energyExported", Tag=1, Type=typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct]),
                    ])

            energyImported: typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
            energyExported: typing.Optional[ElectricalEnergyMeasurement.Structs.EnergyMeasurementStruct] = None
