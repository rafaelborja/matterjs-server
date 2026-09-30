"""AccountLogin cluster definition (auto-generated, DO NOT edit)."""

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
class AccountLogin(Cluster):
    id: typing.ClassVar[int] = 0x0000050E

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Commands:
        @dataclass
        class GetSetupPIN(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050E
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'GetSetupPINResponse'

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="tempAccountIdentifier", Tag=0, Type=str),
                    ])

            tempAccountIdentifier: str = ""

        @dataclass
        class Login(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050E
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="tempAccountIdentifier", Tag=0, Type=str),
                        ClusterObjectFieldDescriptor(Label="setupPIN", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="node", Tag=2, Type=typing.Optional[uint]),
                    ])

            tempAccountIdentifier: str = ""
            setupPIN: str = ""
            node: typing.Optional[uint] = None

        @dataclass
        class Logout(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050E
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
                        ClusterObjectFieldDescriptor(Label="node", Tag=0, Type=typing.Optional[uint]),
                    ])

            node: typing.Optional[uint] = None

        @dataclass
        class GetSetupPINResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050E
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="setupPIN", Tag=0, Type=str),
                    ])

            setupPIN: str = ""

    class Attributes:
        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000050E, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000050E, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000050E, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000050E, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000050E, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class LoggedOut(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000050E

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="node", Tag=0, Type=typing.Optional[uint]),
                    ])

            node: typing.Optional[uint] = None
