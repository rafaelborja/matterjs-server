"""TemperatureControl cluster definition (auto-generated, DO NOT edit)."""

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
class TemperatureControl(Cluster):
    id: typing.ClassVar[int] = 0x00000056

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="temperatureSetpoint", Tag=0x00000000, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="minTemperature", Tag=0x00000001, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="maxTemperature", Tag=0x00000002, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="step", Tag=0x00000003, Type=typing.Optional[int]),
                ClusterObjectFieldDescriptor(Label="selectedTemperatureLevel", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="supportedTemperatureLevels", Tag=0x00000005, Type=typing.Optional[typing.List[str]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    temperatureSetpoint: typing.Optional[int] = None
    minTemperature: typing.Optional[int] = None
    maxTemperature: typing.Optional[int] = None
    step: typing.Optional[int] = None
    selectedTemperatureLevel: typing.Optional[uint] = None
    supportedTemperatureLevels: typing.Optional[typing.List[str]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kTemperatureNumber = 0x1
            kTemperatureLevel = 0x2
            kTemperatureStep = 0x4

    class Commands:
        @dataclass
        class SetTemperature(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000056
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="targetTemperature", Tag=0, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="targetTemperatureLevel", Tag=1, Type=typing.Optional[uint]),
                    ])

            targetTemperature: typing.Optional[int] = None
            targetTemperatureLevel: typing.Optional[uint] = None

    class Attributes:
        TemperatureSetpoint = _attr(__module__, __qualname__, "TemperatureSetpoint", 0x00000056, 0x00000000, "typing.Optional[int]", None)

        MinTemperature = _attr(__module__, __qualname__, "MinTemperature", 0x00000056, 0x00000001, "typing.Optional[int]", None)

        MaxTemperature = _attr(__module__, __qualname__, "MaxTemperature", 0x00000056, 0x00000002, "typing.Optional[int]", None)

        Step = _attr(__module__, __qualname__, "Step", 0x00000056, 0x00000003, "typing.Optional[int]", None)

        SelectedTemperatureLevel = _attr(__module__, __qualname__, "SelectedTemperatureLevel", 0x00000056, 0x00000004, "typing.Optional[uint]", None)

        SupportedTemperatureLevels = _attr(__module__, __qualname__, "SupportedTemperatureLevels", 0x00000056, 0x00000005, "typing.Optional[typing.List[str]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000056, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000056, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000056, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000056, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000056, 0x0000FFFD, "uint", 0)
