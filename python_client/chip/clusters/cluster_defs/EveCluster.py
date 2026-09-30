"""EveCluster cluster definition (auto-generated, DO NOT edit)."""

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
class EveCluster(Cluster):
    id: typing.ClassVar[int] = 0x130AFC01

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="getConfig", Tag=0x130A0000, Type=typing.Optional[bytes]),
                ClusterObjectFieldDescriptor(Label="setConfig", Tag=0x130A0001, Type=typing.Optional[bytes]),
                ClusterObjectFieldDescriptor(Label="loggingMetadata", Tag=0x130A0002, Type=typing.Optional[bytes]),
                ClusterObjectFieldDescriptor(Label="loggingData", Tag=0x130A0003, Type=typing.Optional[bytes]),
                ClusterObjectFieldDescriptor(Label="timesOpened", Tag=0x130A0006, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="lastEventTime", Tag=0x130A0007, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="voltage", Tag=0x130A0008, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="current", Tag=0x130A0009, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="watt", Tag=0x130A000A, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="wattAccumulated", Tag=0x130A000B, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="statusFault", Tag=0x130A000C, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="motionSensitivity", Tag=0x130A000D, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="wattAccumulatedControlPoint", Tag=0x130A000E, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="obstructionDetected", Tag=0x130A0010, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="childLock", Tag=0x130A0011, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="rloc16", Tag=0x130A0012, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="altitude", Tag=0x130A0013, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="pressure", Tag=0x130A0014, Type=typing.Optional[float32]),
                ClusterObjectFieldDescriptor(Label="weatherTrend", Tag=0x130A0015, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="windowOpenMode", Tag=0x130A0017, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="valvePosition", Tag=0x130A0018, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    getConfig: typing.Optional[bytes] = None
    setConfig: typing.Optional[bytes] = None
    loggingMetadata: typing.Optional[bytes] = None
    loggingData: typing.Optional[bytes] = None
    timesOpened: typing.Optional[uint] = None
    lastEventTime: typing.Optional[uint] = None
    voltage: typing.Optional[float32] = None
    current: typing.Optional[float32] = None
    watt: typing.Optional[float32] = None
    wattAccumulated: typing.Optional[float32] = None
    statusFault: typing.Optional[uint] = None
    motionSensitivity: typing.Optional[uint] = None
    wattAccumulatedControlPoint: typing.Optional[uint] = None
    obstructionDetected: typing.Optional[bool] = None
    childLock: typing.Optional[bool] = None
    rloc16: typing.Optional[uint] = None
    altitude: typing.Optional[float32] = None
    pressure: typing.Optional[float32] = None
    weatherTrend: typing.Optional[uint] = None
    windowOpenMode: typing.Optional[bool] = None
    valvePosition: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Attributes:
        GetConfig = _attr(__module__, __qualname__, "GetConfig", 0x130AFC01, 0x130A0000, "typing.Optional[bytes]", None)

        SetConfig = _attr(__module__, __qualname__, "SetConfig", 0x130AFC01, 0x130A0001, "typing.Optional[bytes]", None)

        LoggingMetadata = _attr(__module__, __qualname__, "LoggingMetadata", 0x130AFC01, 0x130A0002, "typing.Optional[bytes]", None)

        LoggingData = _attr(__module__, __qualname__, "LoggingData", 0x130AFC01, 0x130A0003, "typing.Optional[bytes]", None)

        TimesOpened = _attr(__module__, __qualname__, "TimesOpened", 0x130AFC01, 0x130A0006, "typing.Optional[uint]", None)

        LastEventTime = _attr(__module__, __qualname__, "LastEventTime", 0x130AFC01, 0x130A0007, "typing.Optional[uint]", None)

        Voltage = _attr(__module__, __qualname__, "Voltage", 0x130AFC01, 0x130A0008, "typing.Optional[float32]", None)

        Current = _attr(__module__, __qualname__, "Current", 0x130AFC01, 0x130A0009, "typing.Optional[float32]", None)

        Watt = _attr(__module__, __qualname__, "Watt", 0x130AFC01, 0x130A000A, "typing.Optional[float32]", None)

        WattAccumulated = _attr(__module__, __qualname__, "WattAccumulated", 0x130AFC01, 0x130A000B, "typing.Optional[float32]", None)

        StatusFault = _attr(__module__, __qualname__, "StatusFault", 0x130AFC01, 0x130A000C, "typing.Optional[uint]", None)

        MotionSensitivity = _attr(__module__, __qualname__, "MotionSensitivity", 0x130AFC01, 0x130A000D, "typing.Optional[uint]", None)

        WattAccumulatedControlPoint = _attr(__module__, __qualname__, "WattAccumulatedControlPoint", 0x130AFC01, 0x130A000E, "typing.Optional[uint]", None)

        ObstructionDetected = _attr(__module__, __qualname__, "ObstructionDetected", 0x130AFC01, 0x130A0010, "typing.Optional[bool]", None)

        ChildLock = _attr(__module__, __qualname__, "ChildLock", 0x130AFC01, 0x130A0011, "typing.Optional[bool]", None)

        Rloc16 = _attr(__module__, __qualname__, "Rloc16", 0x130AFC01, 0x130A0012, "typing.Optional[uint]", None)

        Altitude = _attr(__module__, __qualname__, "Altitude", 0x130AFC01, 0x130A0013, "typing.Optional[float32]", None)

        Pressure = _attr(__module__, __qualname__, "Pressure", 0x130AFC01, 0x130A0014, "typing.Optional[float32]", None)

        WeatherTrend = _attr(__module__, __qualname__, "WeatherTrend", 0x130AFC01, 0x130A0015, "typing.Optional[uint]", None)

        WindowOpenMode = _attr(__module__, __qualname__, "WindowOpenMode", 0x130AFC01, 0x130A0017, "typing.Optional[bool]", None)

        ValvePosition = _attr(__module__, __qualname__, "ValvePosition", 0x130AFC01, 0x130A0018, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x130AFC01, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x130AFC01, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x130AFC01, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x130AFC01, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x130AFC01, 0x0000FFFD, "uint", 0)
