"""EcosystemInformation cluster definition (auto-generated, DO NOT edit)."""

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
class EcosystemInformation(Cluster):
    id: typing.ClassVar[int] = 0x00000750

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="deviceDirectory", Tag=0x00000000, Type=typing.List[EcosystemInformation.Structs.EcosystemDeviceStruct]),
                ClusterObjectFieldDescriptor(Label="locationDirectory", Tag=0x00000001, Type=typing.List[EcosystemInformation.Structs.EcosystemLocationStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    deviceDirectory: typing.List[EcosystemInformation.Structs.EcosystemDeviceStruct] = field(default_factory=lambda: [])
    locationDirectory: typing.List[EcosystemInformation.Structs.EcosystemLocationStruct] = field(default_factory=lambda: [])
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

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

        @dataclass
        class EcosystemDeviceStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="deviceName", Tag=0, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="deviceNameLastEdit", Tag=1, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="bridgedEndpoint", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="originalEndpoint", Tag=3, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="deviceTypes", Tag=4, Type=typing.List[EcosystemInformation.Structs.DeviceTypeStruct]),
                        ClusterObjectFieldDescriptor(Label="uniqueLocationIDs", Tag=5, Type=typing.List[str]),
                        ClusterObjectFieldDescriptor(Label="uniqueLocationIDsLastEdit", Tag=6, Type=uint),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            deviceName: typing.Optional[str] = None
            deviceNameLastEdit: typing.Optional[uint] = None
            bridgedEndpoint: typing.Optional[uint] = None
            originalEndpoint: typing.Optional[uint] = None
            deviceTypes: typing.List[EcosystemInformation.Structs.DeviceTypeStruct] = field(default_factory=lambda: [])
            uniqueLocationIDs: typing.List[str] = field(default_factory=lambda: [])
            uniqueLocationIDsLastEdit: uint = 0
            fabricIndex: uint = 0

        @dataclass
        class EcosystemLocationStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="uniqueLocationID", Tag=0, Type=str),
                        ClusterObjectFieldDescriptor(Label="locationDescriptor", Tag=1, Type=Globals.Structs.locationdesc),
                        ClusterObjectFieldDescriptor(Label="locationDescriptorLastEdit", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            uniqueLocationID: str = ""
            locationDescriptor: Globals.Structs.locationdesc = field(default_factory=lambda: Globals.Structs.locationdesc())
            locationDescriptorLastEdit: uint = 0
            fabricIndex: uint = 0

    class Attributes:
        DeviceDirectory = _attr(__module__, __qualname__, "DeviceDirectory", 0x00000750, 0x00000000, "typing.List[EcosystemInformation.Structs.EcosystemDeviceStruct]", None, "[]")

        LocationDirectory = _attr(__module__, __qualname__, "LocationDirectory", 0x00000750, 0x00000001, "typing.List[EcosystemInformation.Structs.EcosystemLocationStruct]", None, "[]")

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000750, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000750, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000750, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000750, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000750, 0x0000FFFD, "uint", 0)
