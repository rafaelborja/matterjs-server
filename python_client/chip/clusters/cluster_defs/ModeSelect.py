"""ModeSelect cluster definition (auto-generated, DO NOT edit)."""

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
class ModeSelect(Cluster):
    id: typing.ClassVar[int] = 0x00000050

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="description", Tag=0x00000000, Type=str),
                ClusterObjectFieldDescriptor(Label="standardNamespace", Tag=0x00000001, Type=typing.Union[Nullable, Globals.Enums.namespace]),
                ClusterObjectFieldDescriptor(Label="supportedModes", Tag=0x00000002, Type=typing.List[ModeSelect.Structs.ModeOptionStruct]),
                ClusterObjectFieldDescriptor(Label="currentMode", Tag=0x00000003, Type=uint),
                ClusterObjectFieldDescriptor(Label="startUpMode", Tag=0x00000004, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="onMode", Tag=0x00000005, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    description: str = ""
    standardNamespace: typing.Union[Nullable, Globals.Enums.namespace] = NullValue
    supportedModes: typing.List[ModeSelect.Structs.ModeOptionStruct] = field(default_factory=lambda: [])
    currentMode: uint = 0
    startUpMode: typing.Union[None, Nullable, uint] = None
    onMode: typing.Union[None, Nullable, uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kOnOff = 0x1

    class Structs:
        @dataclass
        class SemanticTagStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mfgCode", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="value", Tag=1, Type=uint),
                    ])

            mfgCode: uint = 0
            value: uint = 0

        @dataclass
        class ModeOptionStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="label", Tag=0, Type=str),
                        ClusterObjectFieldDescriptor(Label="mode", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="semanticTags", Tag=2, Type=typing.List[ModeSelect.Structs.SemanticTagStruct]),
                    ])

            label: str = ""
            mode: uint = 0
            semanticTags: typing.List[ModeSelect.Structs.SemanticTagStruct] = field(default_factory=lambda: [])

    class Commands:
        @dataclass
        class ChangeToMode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000050
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newMode", Tag=0, Type=uint),
                    ])

            newMode: uint = 0

    class Attributes:
        Description = _attr(__module__, __qualname__, "Description", 0x00000050, 0x00000000, "str", "")

        StandardNamespace = _attr(__module__, __qualname__, "StandardNamespace", 0x00000050, 0x00000001, "typing.Union[Nullable, Globals.Enums.namespace]", NullValue)

        SupportedModes = _attr(__module__, __qualname__, "SupportedModes", 0x00000050, 0x00000002, "typing.List[ModeSelect.Structs.ModeOptionStruct]", None, "[]")

        CurrentMode = _attr(__module__, __qualname__, "CurrentMode", 0x00000050, 0x00000003, "uint", 0)

        StartUpMode = _attr(__module__, __qualname__, "StartUpMode", 0x00000050, 0x00000004, "typing.Union[None, Nullable, uint]", None)

        OnMode = _attr(__module__, __qualname__, "OnMode", 0x00000050, 0x00000005, "typing.Union[None, Nullable, uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000050, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000050, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000050, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000050, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000050, 0x0000FFFD, "uint", 0)
