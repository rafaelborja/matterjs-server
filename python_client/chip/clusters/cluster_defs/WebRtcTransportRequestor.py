"""WebRtcTransportRequestor cluster definition (auto-generated, DO NOT edit)."""

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
from .WebRtcTransportDefinitions import WebRtcTransportDefinitions


@dataclass
class WebRtcTransportRequestor(Cluster):
    id: typing.ClassVar[int] = 0x00000554

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="currentSessions", Tag=0x00000000, Type=typing.List[WebRtcTransportDefinitions.Structs.WebRTCSessionStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    currentSessions: typing.List[WebRtcTransportDefinitions.Structs.WebRTCSessionStruct] = field(default_factory=lambda: [])
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Commands:
        @dataclass
        class Offer(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000554
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="webRtcSessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="sdp", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="iceServers", Tag=2, Type=typing.Optional[typing.List[WebRtcTransportDefinitions.Structs.ICEServerStruct]]),
                        ClusterObjectFieldDescriptor(Label="iceTransportPolicy", Tag=3, Type=typing.Optional[str]),
                    ])

            webRtcSessionID: uint = 0
            sdp: str = ""
            iceServers: typing.Optional[typing.List[WebRtcTransportDefinitions.Structs.ICEServerStruct]] = None
            iceTransportPolicy: typing.Optional[str] = None

        @dataclass
        class Answer(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000554
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="webRtcSessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="sdp", Tag=1, Type=str),
                    ])

            webRtcSessionID: uint = 0
            sdp: str = ""

        @dataclass
        class IceCandidates(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000554
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="webRtcSessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="iceCandidates", Tag=1, Type=typing.List[WebRtcTransportDefinitions.Structs.ICECandidateStruct]),
                    ])

            webRtcSessionID: uint = 0
            iceCandidates: typing.List[WebRtcTransportDefinitions.Structs.ICECandidateStruct] = field(default_factory=lambda: [])

        @dataclass
        class End(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000554
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="webRtcSessionID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="reason", Tag=1, Type=WebRtcTransportDefinitions.Enums.WebRTCEndReasonEnum),
                    ])

            webRtcSessionID: uint = 0
            reason: WebRtcTransportDefinitions.Enums.WebRTCEndReasonEnum = 0

    class Attributes:
        CurrentSessions = _attr(__module__, __qualname__, "CurrentSessions", 0x00000554, 0x00000000, "typing.List[WebRtcTransportDefinitions.Structs.WebRTCSessionStruct]", None, "[]")

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000554, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000554, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000554, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000554, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000554, 0x0000FFFD, "uint", 0)
