"""ThreadBorderRouterManagement cluster definition (auto-generated, DO NOT edit)."""

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
class ThreadBorderRouterManagement(Cluster):
    id: typing.ClassVar[int] = 0x00000452

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="borderRouterName", Tag=0x00000000, Type=str),
                ClusterObjectFieldDescriptor(Label="borderAgentID", Tag=0x00000001, Type=bytes),
                ClusterObjectFieldDescriptor(Label="threadVersion", Tag=0x00000002, Type=uint),
                ClusterObjectFieldDescriptor(Label="interfaceEnabled", Tag=0x00000003, Type=bool),
                ClusterObjectFieldDescriptor(Label="activeDatasetTimestamp", Tag=0x00000004, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="pendingDatasetTimestamp", Tag=0x00000005, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    borderRouterName: str = ""
    borderAgentID: bytes = b""
    threadVersion: uint = 0
    interfaceEnabled: bool = False
    activeDatasetTimestamp: typing.Union[Nullable, uint] = NullValue
    pendingDatasetTimestamp: typing.Union[Nullable, uint] = NullValue
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kPANChange = 0x1

    class Commands:
        @dataclass
        class GetActiveDatasetRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000452
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'DatasetResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class GetPendingDatasetRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000452
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'DatasetResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class SetActiveDatasetRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000452
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="activeDataset", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="breadcrumb", Tag=1, Type=typing.Optional[uint]),
                    ])

            activeDataset: bytes = b""
            breadcrumb: typing.Optional[uint] = None

        @dataclass
        class SetPendingDatasetRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000452
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="pendingDataset", Tag=0, Type=bytes),
                    ])

            pendingDataset: bytes = b""

        @dataclass
        class DatasetResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000452
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="dataset", Tag=0, Type=bytes),
                    ])

            dataset: bytes = b""

    class Attributes:
        BorderRouterName = _attr(__module__, __qualname__, "BorderRouterName", 0x00000452, 0x00000000, "str", "")

        BorderAgentID = _attr(__module__, __qualname__, "BorderAgentID", 0x00000452, 0x00000001, "bytes", b"")

        ThreadVersion = _attr(__module__, __qualname__, "ThreadVersion", 0x00000452, 0x00000002, "uint", 0)

        InterfaceEnabled = _attr(__module__, __qualname__, "InterfaceEnabled", 0x00000452, 0x00000003, "bool", False)

        ActiveDatasetTimestamp = _attr(__module__, __qualname__, "ActiveDatasetTimestamp", 0x00000452, 0x00000004, "typing.Union[Nullable, uint]", NullValue)

        PendingDatasetTimestamp = _attr(__module__, __qualname__, "PendingDatasetTimestamp", 0x00000452, 0x00000005, "typing.Union[Nullable, uint]", NullValue)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000452, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000452, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000452, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000452, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000452, 0x0000FFFD, "uint", 0)
