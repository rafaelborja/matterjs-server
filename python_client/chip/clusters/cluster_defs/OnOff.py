"""OnOff cluster definition (auto-generated, DO NOT edit)."""

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
class OnOff(Cluster):
    id: typing.ClassVar[int] = 0x00000006

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="onOff", Tag=0x00000000, Type=bool),
                ClusterObjectFieldDescriptor(Label="globalSceneControl", Tag=0x00004000, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="onTime", Tag=0x00004001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="offWaitTime", Tag=0x00004002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="startUpOnOff", Tag=0x00004003, Type=typing.Union[None, Nullable, OnOff.Enums.StartUpOnOffEnum]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    onOff: bool = False
    globalSceneControl: typing.Optional[bool] = None
    onTime: typing.Optional[uint] = None
    offWaitTime: typing.Optional[uint] = None
    startUpOnOff: typing.Union[None, Nullable, OnOff.Enums.StartUpOnOffEnum] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class StartUpOnOffEnum(MatterIntEnum):
            kOff = 0x00
            kOn = 0x01
            kToggle = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class EffectIdentifierEnum(MatterIntEnum):
            kDelayedAllOff = 0x00
            kDyingLight = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class DelayedAllOffEffectVariantEnum(MatterIntEnum):
            kDelayedOffFastFade = 0x00
            kNoFade = 0x01
            kDelayedOffSlowFade = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class DyingLightEffectVariantEnum(MatterIntEnum):
            kDyingLightFadeOff = 0x00
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 1

    class Bitmaps:
        class Feature(IntFlag):
            kLighting = 0x1
            kDeadFrontBehavior = 0x2
            kOffOnly = 0x4

        class OnOffControlBitmap(IntFlag):
            kAcceptOnlyWhenOn = 0x1

    class Commands:
        @dataclass
        class Off(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000006
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class On(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000006
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class Toggle(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000006
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class OffWithEffect(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000006
            command_id: typing.ClassVar[int] = 0x00000040
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="effectIdentifier", Tag=0, Type=OnOff.Enums.EffectIdentifierEnum),
                        ClusterObjectFieldDescriptor(Label="effectVariant", Tag=1, Type=Globals.Enums.enum8),
                    ])

            effectIdentifier: OnOff.Enums.EffectIdentifierEnum = 0
            effectVariant: Globals.Enums.enum8 = 0

        @dataclass
        class OnWithRecallGlobalScene(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000006
            command_id: typing.ClassVar[int] = 0x00000041
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class OnWithTimedOff(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000006
            command_id: typing.ClassVar[int] = 0x00000042
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="onOffControl", Tag=0, Type=OnOff.Bitmaps.OnOffControlBitmap),
                        ClusterObjectFieldDescriptor(Label="onTime", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="offWaitTime", Tag=2, Type=uint),
                    ])

            onOffControl: OnOff.Bitmaps.OnOffControlBitmap = 0
            onTime: uint = 0
            offWaitTime: uint = 0

    class Attributes:
        OnOff = _attr(__module__, __qualname__, "OnOff", 0x00000006, 0x00000000, "bool", False)

        GlobalSceneControl = _attr(__module__, __qualname__, "GlobalSceneControl", 0x00000006, 0x00004000, "typing.Optional[bool]", None)

        OnTime = _attr(__module__, __qualname__, "OnTime", 0x00000006, 0x00004001, "typing.Optional[uint]", None)

        OffWaitTime = _attr(__module__, __qualname__, "OffWaitTime", 0x00000006, 0x00004002, "typing.Optional[uint]", None)

        StartUpOnOff = _attr(__module__, __qualname__, "StartUpOnOff", 0x00000006, 0x00004003, "typing.Union[None, Nullable, OnOff.Enums.StartUpOnOffEnum]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000006, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000006, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000006, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000006, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000006, 0x0000FFFD, "uint", 0)
