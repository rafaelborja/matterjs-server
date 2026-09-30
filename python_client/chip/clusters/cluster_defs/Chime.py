"""Chime cluster definition (auto-generated, DO NOT edit)."""

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
class Chime(Cluster):
    id: typing.ClassVar[int] = 0x00000556

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="installedChimeSounds", Tag=0x00000000, Type=typing.List[Chime.Structs.ChimeSoundStruct]),
                ClusterObjectFieldDescriptor(Label="selectedChime", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="enabled", Tag=0x00000002, Type=bool),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    installedChimeSounds: typing.List[Chime.Structs.ChimeSoundStruct] = field(default_factory=lambda: [])
    selectedChime: uint = 0
    enabled: bool = False
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Structs:
        @dataclass
        class ChimeSoundStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="chimeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="name", Tag=1, Type=str),
                    ])

            chimeID: uint = 0
            name: str = ""

    class Commands:
        @dataclass
        class PlayChimeSound(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000556
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="chimeID", Tag=0, Type=typing.Optional[uint]),
                    ])

            chimeID: typing.Optional[uint] = None

    class Attributes:
        InstalledChimeSounds = _attr(__module__, __qualname__, "InstalledChimeSounds", 0x00000556, 0x00000000, "typing.List[Chime.Structs.ChimeSoundStruct]", None, "[]")

        SelectedChime = _attr(__module__, __qualname__, "SelectedChime", 0x00000556, 0x00000001, "uint", 0)

        Enabled = _attr(__module__, __qualname__, "Enabled", 0x00000556, 0x00000002, "bool", False)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000556, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000556, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000556, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000556, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000556, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class ChimeStartedPlaying(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000556

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="chimeID", Tag=0, Type=uint),
                    ])

            chimeID: uint = 0
