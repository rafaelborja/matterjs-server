"""LevelControl cluster definition (auto-generated, DO NOT edit)."""

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
class LevelControl(Cluster):
    id: typing.ClassVar[int] = 0x00000008

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="currentLevel", Tag=0x00000000, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="remainingTime", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="minLevel", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="maxLevel", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentFrequency", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="minFrequency", Tag=0x00000005, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="maxFrequency", Tag=0x00000006, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="options", Tag=0x0000000F, Type=LevelControl.Bitmaps.OptionsBitmap),
                ClusterObjectFieldDescriptor(Label="onOffTransitionTime", Tag=0x00000010, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="onLevel", Tag=0x00000011, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="onTransitionTime", Tag=0x00000012, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="offTransitionTime", Tag=0x00000013, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="defaultMoveRate", Tag=0x00000014, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="startUpCurrentLevel", Tag=0x00004000, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    currentLevel: typing.Union[Nullable, uint] = NullValue
    remainingTime: typing.Optional[uint] = None
    minLevel: typing.Optional[uint] = None
    maxLevel: typing.Optional[uint] = None
    currentFrequency: typing.Optional[uint] = None
    minFrequency: typing.Optional[uint] = None
    maxFrequency: typing.Optional[uint] = None
    options: LevelControl.Bitmaps.OptionsBitmap = 0
    onOffTransitionTime: typing.Optional[uint] = None
    onLevel: typing.Union[Nullable, uint] = NullValue
    onTransitionTime: typing.Union[None, Nullable, uint] = None
    offTransitionTime: typing.Union[None, Nullable, uint] = None
    defaultMoveRate: typing.Union[None, Nullable, uint] = None
    startUpCurrentLevel: typing.Union[None, Nullable, uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class MoveModeEnum(MatterIntEnum):
            kUp = 0x00
            kDown = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class StepModeEnum(MatterIntEnum):
            kUp = 0x00
            kDown = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Bitmaps:
        class Feature(IntFlag):
            kOnOff = 0x1
            kLighting = 0x2
            kFrequency = 0x4

        class OptionsBitmap(IntFlag):
            kExecuteIfOff = 0x1
            kCoupleColorTempToLevel = 0x2

    class Commands:
        @dataclass
        class MoveToLevel(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="level", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            level: uint = 0
            transitionTime: typing.Union[Nullable, uint] = NullValue
            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class Move(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="moveMode", Tag=0, Type=LevelControl.Enums.MoveModeEnum),
                        ClusterObjectFieldDescriptor(Label="rate", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            moveMode: LevelControl.Enums.MoveModeEnum = 0
            rate: typing.Union[Nullable, uint] = NullValue
            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class Step(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepMode", Tag=0, Type=LevelControl.Enums.StepModeEnum),
                        ClusterObjectFieldDescriptor(Label="stepSize", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            stepMode: LevelControl.Enums.StepModeEnum = 0
            stepSize: uint = 0
            transitionTime: typing.Union[Nullable, uint] = NullValue
            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class Stop(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=0, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=1, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveToLevelWithOnOff(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="level", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            level: uint = 0
            transitionTime: typing.Union[Nullable, uint] = NullValue
            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveWithOnOff(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="moveMode", Tag=0, Type=LevelControl.Enums.MoveModeEnum),
                        ClusterObjectFieldDescriptor(Label="rate", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            moveMode: LevelControl.Enums.MoveModeEnum = 0
            rate: typing.Union[Nullable, uint] = NullValue
            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StepWithOnOff(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepMode", Tag=0, Type=LevelControl.Enums.StepModeEnum),
                        ClusterObjectFieldDescriptor(Label="stepSize", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            stepMode: LevelControl.Enums.StepModeEnum = 0
            stepSize: uint = 0
            transitionTime: typing.Union[Nullable, uint] = NullValue
            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StopWithOnOff(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=0, Type=LevelControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=1, Type=LevelControl.Bitmaps.OptionsBitmap),
                    ])

            optionsMask: LevelControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: LevelControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveToClosestFrequency(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000008
            command_id: typing.ClassVar[int] = 0x00000008
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="frequency", Tag=0, Type=uint),
                    ])

            frequency: uint = 0

    class Attributes:
        CurrentLevel = _attr(__module__, __qualname__, "CurrentLevel", 0x00000008, 0x00000000, "typing.Union[Nullable, uint]", NullValue)

        RemainingTime = _attr(__module__, __qualname__, "RemainingTime", 0x00000008, 0x00000001, "typing.Optional[uint]", None)

        MinLevel = _attr(__module__, __qualname__, "MinLevel", 0x00000008, 0x00000002, "typing.Optional[uint]", None)

        MaxLevel = _attr(__module__, __qualname__, "MaxLevel", 0x00000008, 0x00000003, "typing.Optional[uint]", None)

        CurrentFrequency = _attr(__module__, __qualname__, "CurrentFrequency", 0x00000008, 0x00000004, "typing.Optional[uint]", None)

        MinFrequency = _attr(__module__, __qualname__, "MinFrequency", 0x00000008, 0x00000005, "typing.Optional[uint]", None)

        MaxFrequency = _attr(__module__, __qualname__, "MaxFrequency", 0x00000008, 0x00000006, "typing.Optional[uint]", None)

        Options = _attr(__module__, __qualname__, "Options", 0x00000008, 0x0000000F, "LevelControl.Bitmaps.OptionsBitmap", 0)

        OnOffTransitionTime = _attr(__module__, __qualname__, "OnOffTransitionTime", 0x00000008, 0x00000010, "typing.Optional[uint]", None)

        OnLevel = _attr(__module__, __qualname__, "OnLevel", 0x00000008, 0x00000011, "typing.Union[Nullable, uint]", NullValue)

        OnTransitionTime = _attr(__module__, __qualname__, "OnTransitionTime", 0x00000008, 0x00000012, "typing.Union[None, Nullable, uint]", None)

        OffTransitionTime = _attr(__module__, __qualname__, "OffTransitionTime", 0x00000008, 0x00000013, "typing.Union[None, Nullable, uint]", None)

        DefaultMoveRate = _attr(__module__, __qualname__, "DefaultMoveRate", 0x00000008, 0x00000014, "typing.Union[None, Nullable, uint]", None)

        StartUpCurrentLevel = _attr(__module__, __qualname__, "StartUpCurrentLevel", 0x00000008, 0x00004000, "typing.Union[None, Nullable, uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000008, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000008, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000008, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000008, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000008, 0x0000FFFD, "uint", 0)
