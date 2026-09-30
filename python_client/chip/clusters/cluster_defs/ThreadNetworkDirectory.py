"""ThreadNetworkDirectory cluster definition (auto-generated, DO NOT edit)."""

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
class ThreadNetworkDirectory(Cluster):
    id: typing.ClassVar[int] = 0x00000453

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="preferredExtendedPanID", Tag=0x00000000, Type=typing.Union[Nullable, bytes]),
                ClusterObjectFieldDescriptor(Label="threadNetworks", Tag=0x00000001, Type=typing.List[ThreadNetworkDirectory.Structs.ThreadNetworkStruct]),
                ClusterObjectFieldDescriptor(Label="threadNetworkTableSize", Tag=0x00000002, Type=uint),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    preferredExtendedPanID: typing.Union[Nullable, bytes] = NullValue
    threadNetworks: typing.List[ThreadNetworkDirectory.Structs.ThreadNetworkStruct] = field(default_factory=lambda: [])
    threadNetworkTableSize: uint = 0
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Structs:
        @dataclass
        class ThreadNetworkStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="extendedPanId", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="networkName", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="channel", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="activeTimestamp", Tag=3, Type=uint),
                    ])

            extendedPanId: bytes = b""
            networkName: str = ""
            channel: uint = 0
            activeTimestamp: uint = 0

    class Commands:
        @dataclass
        class AddNetwork(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000453
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="operationalDataset", Tag=0, Type=bytes),
                    ])

            operationalDataset: bytes = b""

        @dataclass
        class RemoveNetwork(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000453
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="extendedPanId", Tag=0, Type=bytes),
                    ])

            extendedPanId: bytes = b""

        @dataclass
        class GetOperationalDataset(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000453
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'OperationalDatasetResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="extendedPanId", Tag=0, Type=bytes),
                    ])

            extendedPanId: bytes = b""

        @dataclass
        class OperationalDatasetResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000453
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="operationalDataset", Tag=0, Type=bytes),
                    ])

            operationalDataset: bytes = b""

    class Attributes:
        PreferredExtendedPanID = _attr(__module__, __qualname__, "PreferredExtendedPanID", 0x00000453, 0x00000000, "typing.Union[Nullable, bytes]", NullValue)

        ThreadNetworks = _attr(__module__, __qualname__, "ThreadNetworks", 0x00000453, 0x00000001, "typing.List[ThreadNetworkDirectory.Structs.ThreadNetworkStruct]", None, "[]")

        ThreadNetworkTableSize = _attr(__module__, __qualname__, "ThreadNetworkTableSize", 0x00000453, 0x00000002, "uint", 0)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000453, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000453, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000453, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000453, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000453, 0x0000FFFD, "uint", 0)
