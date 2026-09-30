"""Descriptor cluster definition (auto-generated, DO NOT edit)."""

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
class Descriptor(Cluster):
    id: typing.ClassVar[int] = 0x0000001D

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="deviceTypeList", Tag=0x00000000, Type=typing.List[Descriptor.Structs.DeviceTypeStruct]),
                ClusterObjectFieldDescriptor(Label="serverList", Tag=0x00000001, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="clientList", Tag=0x00000002, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="partsList", Tag=0x00000003, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="tagList", Tag=0x00000004, Type=typing.Optional[typing.List[Globals.Structs.semtag]]),
                ClusterObjectFieldDescriptor(Label="endpointUniqueID", Tag=0x00000005, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    deviceTypeList: typing.List[Descriptor.Structs.DeviceTypeStruct] = field(default_factory=lambda: [])
    serverList: typing.List[uint] = field(default_factory=lambda: [])
    clientList: typing.List[uint] = field(default_factory=lambda: [])
    partsList: typing.List[uint] = field(default_factory=lambda: [])
    tagList: typing.Optional[typing.List[Globals.Structs.semtag]] = None
    endpointUniqueID: typing.Optional[str] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kTagList = 0x1

    class Structs:
        @dataclass
        class DeviceTypeStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="deviceType", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="revision", Tag=1, Type=uint),
                    ])

            deviceType: uint = 0
            revision: uint = 0

    class Attributes:
        DeviceTypeList = _attr(__module__, __qualname__, "DeviceTypeList", 0x0000001D, 0x00000000, "typing.List[Descriptor.Structs.DeviceTypeStruct]", None, "[]")

        ServerList = _attr(__module__, __qualname__, "ServerList", 0x0000001D, 0x00000001, "typing.List[uint]", None, "[]")

        ClientList = _attr(__module__, __qualname__, "ClientList", 0x0000001D, 0x00000002, "typing.List[uint]", None, "[]")

        PartsList = _attr(__module__, __qualname__, "PartsList", 0x0000001D, 0x00000003, "typing.List[uint]", None, "[]")

        TagList = _attr(__module__, __qualname__, "TagList", 0x0000001D, 0x00000004, "typing.Optional[typing.List[Globals.Structs.semtag]]", None)

        EndpointUniqueID = _attr(__module__, __qualname__, "EndpointUniqueID", 0x0000001D, 0x00000005, "typing.Optional[str]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000001D, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000001D, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000001D, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000001D, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000001D, 0x0000FFFD, "uint", 0)
