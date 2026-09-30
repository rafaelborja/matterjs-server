"""DraftElectricalMeasurementCluster cluster definition (auto-generated, DO NOT edit)."""

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
class DraftElectricalMeasurementCluster(Cluster):
    id: typing.ClassVar[int] = 0x00000B04

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="rmsVoltage", Tag=0x00000505, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="rmsCurrent", Tag=0x00000508, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="activePower", Tag=0x0000050B, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="acVoltageMultiplier", Tag=0x00000600, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="acVoltageDivisor", Tag=0x00000601, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="acCurrentMultiplier", Tag=0x00000602, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="acCurrentDivisor", Tag=0x00000603, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="acPowerMultiplier", Tag=0x00000604, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="acPowerDivisor", Tag=0x00000605, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    rmsVoltage: typing.Optional[uint] = None
    rmsCurrent: typing.Optional[uint] = None
    activePower: typing.Optional[uint] = None
    acVoltageMultiplier: typing.Optional[uint] = None
    acVoltageDivisor: typing.Optional[uint] = None
    acCurrentMultiplier: typing.Optional[uint] = None
    acCurrentDivisor: typing.Optional[uint] = None
    acPowerMultiplier: typing.Optional[uint] = None
    acPowerDivisor: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        RmsVoltage = _attr(__module__, __qualname__, "RmsVoltage", 0x00000B04, 0x00000505, "typing.Optional[uint]", None)

        RmsCurrent = _attr(__module__, __qualname__, "RmsCurrent", 0x00000B04, 0x00000508, "typing.Optional[uint]", None)

        ActivePower = _attr(__module__, __qualname__, "ActivePower", 0x00000B04, 0x0000050B, "typing.Optional[uint]", None)

        AcVoltageMultiplier = _attr(__module__, __qualname__, "AcVoltageMultiplier", 0x00000B04, 0x00000600, "typing.Optional[uint]", None)

        AcVoltageDivisor = _attr(__module__, __qualname__, "AcVoltageDivisor", 0x00000B04, 0x00000601, "typing.Optional[uint]", None)

        AcCurrentMultiplier = _attr(__module__, __qualname__, "AcCurrentMultiplier", 0x00000B04, 0x00000602, "typing.Optional[uint]", None)

        AcCurrentDivisor = _attr(__module__, __qualname__, "AcCurrentDivisor", 0x00000B04, 0x00000603, "typing.Optional[uint]", None)

        AcPowerMultiplier = _attr(__module__, __qualname__, "AcPowerMultiplier", 0x00000B04, 0x00000604, "typing.Optional[uint]", None)

        AcPowerDivisor = _attr(__module__, __qualname__, "AcPowerDivisor", 0x00000B04, 0x00000605, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000B04, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000B04, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000B04, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000B04, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000B04, 0x0000FFFD, "uint", 0)
