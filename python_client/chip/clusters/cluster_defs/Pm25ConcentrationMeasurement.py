"""Pm25ConcentrationMeasurement cluster definition (auto-generated, DO NOT edit)."""

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
class Pm25ConcentrationMeasurement(Cluster):
    id: typing.ClassVar[int] = 0x0000042A

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="measuredValue", Tag=0x00000000, Type=typing.Union[None, Nullable, float32]),
                ClusterObjectFieldDescriptor(Label="minMeasuredValue", Tag=0x00000001, Type=typing.Union[None, Nullable, float32]),
                ClusterObjectFieldDescriptor(Label="maxMeasuredValue", Tag=0x00000002, Type=typing.Union[None, Nullable, float32]),
                ClusterObjectFieldDescriptor(Label="peakMeasuredValue", Tag=0x00000003, Type=typing.Union[None, Nullable, float32]),
                ClusterObjectFieldDescriptor(Label="peakMeasuredValueWindow", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="averageMeasuredValue", Tag=0x00000005, Type=typing.Union[None, Nullable, float32]),
                ClusterObjectFieldDescriptor(Label="averageMeasuredValueWindow", Tag=0x00000006, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="uncertainty", Tag=0x00000007, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="measurementUnit", Tag=0x00000008, Type=typing.Optional[Pm25ConcentrationMeasurement.Enums.MeasurementUnitEnum]),
                ClusterObjectFieldDescriptor(Label="measurementMedium", Tag=0x00000009, Type=Pm25ConcentrationMeasurement.Enums.MeasurementMediumEnum),
                ClusterObjectFieldDescriptor(Label="levelValue", Tag=0x0000000A, Type=typing.Optional[Pm25ConcentrationMeasurement.Enums.LevelValueEnum]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    measuredValue: typing.Union[None, Nullable, float32] = None
    minMeasuredValue: typing.Union[None, Nullable, float32] = None
    maxMeasuredValue: typing.Union[None, Nullable, float32] = None
    peakMeasuredValue: typing.Union[None, Nullable, float32] = None
    peakMeasuredValueWindow: typing.Optional[uint] = None
    averageMeasuredValue: typing.Union[None, Nullable, float32] = None
    averageMeasuredValueWindow: typing.Optional[uint] = None
    uncertainty: typing.Optional[float32] = None
    measurementUnit: typing.Optional[Pm25ConcentrationMeasurement.Enums.MeasurementUnitEnum] = None
    measurementMedium: Pm25ConcentrationMeasurement.Enums.MeasurementMediumEnum = 0
    levelValue: typing.Optional[Pm25ConcentrationMeasurement.Enums.LevelValueEnum] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class MeasurementUnitEnum(MatterIntEnum):
            kPpm = 0x00
            kPpb = 0x01
            kPpt = 0x02
            kMgm3 = 0x03
            kUgm3 = 0x04
            kNgm3 = 0x05
            kPm3 = 0x06
            kBqm3 = 0x07
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 8

        class MeasurementMediumEnum(MatterIntEnum):
            kAir = 0x00
            kWater = 0x01
            kSoil = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class LevelValueEnum(MatterIntEnum):
            kUnknown = 0x00
            kLow = 0x01
            kMedium = 0x02
            kHigh = 0x03
            kCritical = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

    class Bitmaps:
        class Feature(IntFlag):
            kNumericMeasurement = 0x1
            kLevelIndication = 0x2
            kMediumLevel = 0x4
            kCriticalLevel = 0x8
            kPeakMeasurement = 0x10
            kAverageMeasurement = 0x20

    class Attributes:
        MeasuredValue = _attr(__module__, __qualname__, "MeasuredValue", 0x0000042A, 0x00000000, "typing.Union[None, Nullable, float32]", None)

        MinMeasuredValue = _attr(__module__, __qualname__, "MinMeasuredValue", 0x0000042A, 0x00000001, "typing.Union[None, Nullable, float32]", None)

        MaxMeasuredValue = _attr(__module__, __qualname__, "MaxMeasuredValue", 0x0000042A, 0x00000002, "typing.Union[None, Nullable, float32]", None)

        PeakMeasuredValue = _attr(__module__, __qualname__, "PeakMeasuredValue", 0x0000042A, 0x00000003, "typing.Union[None, Nullable, float32]", None)

        PeakMeasuredValueWindow = _attr(__module__, __qualname__, "PeakMeasuredValueWindow", 0x0000042A, 0x00000004, "typing.Optional[uint]", None)

        AverageMeasuredValue = _attr(__module__, __qualname__, "AverageMeasuredValue", 0x0000042A, 0x00000005, "typing.Union[None, Nullable, float32]", None)

        AverageMeasuredValueWindow = _attr(__module__, __qualname__, "AverageMeasuredValueWindow", 0x0000042A, 0x00000006, "typing.Optional[uint]", None)

        Uncertainty = _attr(__module__, __qualname__, "Uncertainty", 0x0000042A, 0x00000007, "typing.Optional[float32]", None)

        MeasurementUnit = _attr(__module__, __qualname__, "MeasurementUnit", 0x0000042A, 0x00000008, "typing.Optional[Pm25ConcentrationMeasurement.Enums.MeasurementUnitEnum]", None)

        MeasurementMedium = _attr(__module__, __qualname__, "MeasurementMedium", 0x0000042A, 0x00000009, "Pm25ConcentrationMeasurement.Enums.MeasurementMediumEnum", 0)

        LevelValue = _attr(__module__, __qualname__, "LevelValue", 0x0000042A, 0x0000000A, "typing.Optional[Pm25ConcentrationMeasurement.Enums.LevelValueEnum]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000042A, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000042A, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000042A, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000042A, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000042A, 0x0000FFFD, "uint", 0)
