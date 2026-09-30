"""WiFiNetworkManagement cluster definition (auto-generated, DO NOT edit)."""

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
class WiFiNetworkManagement(Cluster):
    id: typing.ClassVar[int] = 0x00000451

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="ssid", Tag=0x00000000, Type=typing.Union[Nullable, bytes]),
                ClusterObjectFieldDescriptor(Label="passphraseSurrogate", Tag=0x00000001, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    ssid: typing.Union[Nullable, bytes] = NullValue
    passphraseSurrogate: typing.Union[Nullable, uint] = NullValue
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Commands:
        @dataclass
        class NetworkPassphraseRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000451
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'NetworkPassphraseResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class NetworkPassphraseResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000451
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="passphrase", Tag=0, Type=bytes),
                    ])

            passphrase: bytes = b""

    class Attributes:
        Ssid = _attr(__module__, __qualname__, "Ssid", 0x00000451, 0x00000000, "typing.Union[Nullable, bytes]", NullValue)

        PassphraseSurrogate = _attr(__module__, __qualname__, "PassphraseSurrogate", 0x00000451, 0x00000001, "typing.Union[Nullable, uint]", NullValue)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000451, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000451, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000451, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000451, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000451, 0x0000FFFD, "uint", 0)
