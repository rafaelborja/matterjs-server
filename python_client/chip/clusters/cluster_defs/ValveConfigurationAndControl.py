"""ValveConfigurationAndControl cluster definition (auto-generated, DO NOT edit)."""

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
class ValveConfigurationAndControl(Cluster):
    id: typing.ClassVar[int] = 0x00000081

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="openDuration", Tag=0x00000000, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="defaultOpenDuration", Tag=0x00000001, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="autoCloseTime", Tag=0x00000002, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="remainingDuration", Tag=0x00000003, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="currentState", Tag=0x00000004, Type=typing.Union[Nullable, ValveConfigurationAndControl.Enums.ValveStateEnum]),
                ClusterObjectFieldDescriptor(Label="targetState", Tag=0x00000005, Type=typing.Union[Nullable, ValveConfigurationAndControl.Enums.ValveStateEnum]),
                ClusterObjectFieldDescriptor(Label="currentLevel", Tag=0x00000006, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="targetLevel", Tag=0x00000007, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="defaultOpenLevel", Tag=0x00000008, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="valveFault", Tag=0x00000009, Type=typing.Optional[ValveConfigurationAndControl.Bitmaps.ValveFaultBitmap]),
                ClusterObjectFieldDescriptor(Label="levelStep", Tag=0x0000000A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    openDuration: typing.Union[Nullable, uint] = NullValue
    defaultOpenDuration: typing.Union[Nullable, uint] = NullValue
    autoCloseTime: typing.Union[None, Nullable, uint] = None
    remainingDuration: typing.Union[Nullable, uint] = NullValue
    currentState: typing.Union[Nullable, ValveConfigurationAndControl.Enums.ValveStateEnum] = NullValue
    targetState: typing.Union[Nullable, ValveConfigurationAndControl.Enums.ValveStateEnum] = NullValue
    currentLevel: typing.Union[None, Nullable, uint] = None
    targetLevel: typing.Union[None, Nullable, uint] = None
    defaultOpenLevel: typing.Optional[uint] = None
    valveFault: typing.Optional[ValveConfigurationAndControl.Bitmaps.ValveFaultBitmap] = None
    levelStep: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class ValveStateEnum(MatterIntEnum):
            kClosed = 0x00
            kOpen = 0x01
            kTransitioning = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class StatusCodeEnum(MatterIntEnum):
            kFailureDueToFault = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

    class Bitmaps:
        class Feature(IntFlag):
            kTimeSync = 0x1
            kLevel = 0x2

        class ValveFaultBitmap(IntFlag):
            kGeneralFault = 0x1
            kBlocked = 0x2
            kLeaking = 0x4
            kNotConnected = 0x8
            kShortCircuit = 0x10
            kCurrentExceeded = 0x20

    class Commands:
        @dataclass
        class Open(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000081
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="openDuration", Tag=0, Type=typing.Union[None, Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="targetLevel", Tag=1, Type=typing.Optional[uint]),
                    ])

            openDuration: typing.Union[None, Nullable, uint] = None
            targetLevel: typing.Optional[uint] = None

        @dataclass
        class Close(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000081
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


    class Attributes:
        OpenDuration = _attr(__module__, __qualname__, "OpenDuration", 0x00000081, 0x00000000, "typing.Union[Nullable, uint]", NullValue)

        DefaultOpenDuration = _attr(__module__, __qualname__, "DefaultOpenDuration", 0x00000081, 0x00000001, "typing.Union[Nullable, uint]", NullValue)

        AutoCloseTime = _attr(__module__, __qualname__, "AutoCloseTime", 0x00000081, 0x00000002, "typing.Union[None, Nullable, uint]", None)

        RemainingDuration = _attr(__module__, __qualname__, "RemainingDuration", 0x00000081, 0x00000003, "typing.Union[Nullable, uint]", NullValue)

        CurrentState = _attr(__module__, __qualname__, "CurrentState", 0x00000081, 0x00000004, "typing.Union[Nullable, ValveConfigurationAndControl.Enums.ValveStateEnum]", NullValue)

        TargetState = _attr(__module__, __qualname__, "TargetState", 0x00000081, 0x00000005, "typing.Union[Nullable, ValveConfigurationAndControl.Enums.ValveStateEnum]", NullValue)

        CurrentLevel = _attr(__module__, __qualname__, "CurrentLevel", 0x00000081, 0x00000006, "typing.Union[None, Nullable, uint]", None)

        TargetLevel = _attr(__module__, __qualname__, "TargetLevel", 0x00000081, 0x00000007, "typing.Union[None, Nullable, uint]", None)

        DefaultOpenLevel = _attr(__module__, __qualname__, "DefaultOpenLevel", 0x00000081, 0x00000008, "typing.Optional[uint]", None)

        ValveFault = _attr(__module__, __qualname__, "ValveFault", 0x00000081, 0x00000009, "typing.Optional[ValveConfigurationAndControl.Bitmaps.ValveFaultBitmap]", None)

        LevelStep = _attr(__module__, __qualname__, "LevelStep", 0x00000081, 0x0000000A, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000081, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000081, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000081, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000081, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000081, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class ValveStateChanged(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000081

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="valveState", Tag=0, Type=ValveConfigurationAndControl.Enums.ValveStateEnum),
                        ClusterObjectFieldDescriptor(Label="valveLevel", Tag=1, Type=typing.Optional[uint]),
                    ])

            valveState: ValveConfigurationAndControl.Enums.ValveStateEnum = 0
            valveLevel: typing.Optional[uint] = None

        @dataclass
        class ValveFault(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000081

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="valveFault", Tag=0, Type=ValveConfigurationAndControl.Bitmaps.ValveFaultBitmap),
                    ])

            valveFault: ValveConfigurationAndControl.Bitmaps.ValveFaultBitmap = 0
