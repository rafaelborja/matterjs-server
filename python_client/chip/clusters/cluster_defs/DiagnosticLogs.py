"""DiagnosticLogs cluster definition (auto-generated, DO NOT edit)."""

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
class DiagnosticLogs(Cluster):
    id: typing.ClassVar[int] = 0x00000032

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

    class Enums:
        class IntentEnum(MatterIntEnum):
            kEndUserSupport = 0x00
            kNetworkDiag = 0x01
            kCrashLogs = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class StatusEnum(MatterIntEnum):
            kSuccess = 0x00
            kExhausted = 0x01
            kNoLogs = 0x02
            kBusy = 0x03
            kDenied = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

        class TransferProtocolEnum(MatterIntEnum):
            kResponsePayload = 0x00
            kBdx = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Commands:
        @dataclass
        class RetrieveLogsRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000032
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'RetrieveLogsResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="intent", Tag=0, Type=DiagnosticLogs.Enums.IntentEnum),
                        ClusterObjectFieldDescriptor(Label="requestedProtocol", Tag=1, Type=DiagnosticLogs.Enums.TransferProtocolEnum),
                        ClusterObjectFieldDescriptor(Label="transferFileDesignator", Tag=2, Type=typing.Optional[str]),
                    ])

            intent: DiagnosticLogs.Enums.IntentEnum = 0
            requestedProtocol: DiagnosticLogs.Enums.TransferProtocolEnum = 0
            transferFileDesignator: typing.Optional[str] = None

        @dataclass
        class RetrieveLogsResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000032
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="status", Tag=0, Type=DiagnosticLogs.Enums.StatusEnum),
                        ClusterObjectFieldDescriptor(Label="logContent", Tag=1, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="UTCTimeStamp", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="timeSinceBoot", Tag=3, Type=typing.Optional[uint]),
                    ])

            status: DiagnosticLogs.Enums.StatusEnum = 0
            logContent: bytes = b""
            UTCTimeStamp: typing.Optional[uint] = None
            timeSinceBoot: typing.Optional[uint] = None

    class Attributes:
        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000032, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000032, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000032, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000032, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000032, 0x0000FFFD, "uint", 0)
