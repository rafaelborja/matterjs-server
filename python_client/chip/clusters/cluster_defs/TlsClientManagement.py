"""TlsClientManagement cluster definition (auto-generated, DO NOT edit)."""

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
class TlsClientManagement(Cluster):
    id: typing.ClassVar[int] = 0x00000802

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="maxProvisioned", Tag=0x00000000, Type=uint),
                ClusterObjectFieldDescriptor(Label="provisionedEndpoints", Tag=0x00000001, Type=typing.List[TlsClientManagement.Structs.TLSEndpointStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    maxProvisioned: uint = 0
    provisionedEndpoints: typing.List[TlsClientManagement.Structs.TLSEndpointStruct] = field(default_factory=lambda: [])
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class StatusCodeEnum(MatterIntEnum):
            kEndpointAlreadyInstalled = 0x02
            kRootCertificateNotFound = 0x03
            kClientCertificateNotFound = 0x04
            kEndpointInUse = 0x05
            kInvalidTime = 0x06
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 7

    class Structs:
        @dataclass
        class TLSEndpointStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="hostname", Tag=1, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="port", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="caid", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="ccdid", Tag=4, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="referenceCount", Tag=5, Type=uint),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            endpointID: uint = 0
            hostname: bytes = b""
            port: uint = 0
            caid: uint = 0
            ccdid: typing.Union[Nullable, uint] = NullValue
            referenceCount: uint = 0
            fabricIndex: uint = 0

    class Commands:
        @dataclass
        class ProvisionEndpoint(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000802
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'ProvisionEndpointResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="hostname", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="port", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="caid", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="ccdid", Tag=3, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=4, Type=typing.Union[Nullable, uint]),
                    ])

            hostname: bytes = b""
            port: uint = 0
            caid: uint = 0
            ccdid: typing.Union[Nullable, uint] = NullValue
            endpointID: typing.Union[Nullable, uint] = NullValue

        @dataclass
        class FindEndpoint(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000802
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'FindEndpointResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=0, Type=uint),
                    ])

            endpointID: uint = 0

        @dataclass
        class RemoveEndpoint(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000802
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=0, Type=uint),
                    ])

            endpointID: uint = 0

        @dataclass
        class ProvisionEndpointResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000802
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=0, Type=uint),
                    ])

            endpointID: uint = 0

        @dataclass
        class FindEndpointResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000802
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpoint", Tag=0, Type=TlsClientManagement.Structs.TLSEndpointStruct),
                    ])

            endpoint: TlsClientManagement.Structs.TLSEndpointStruct = field(default_factory=lambda: TlsClientManagement.Structs.TLSEndpointStruct())

    class Attributes:
        MaxProvisioned = _attr(__module__, __qualname__, "MaxProvisioned", 0x00000802, 0x00000000, "uint", 0)

        ProvisionedEndpoints = _attr(__module__, __qualname__, "ProvisionedEndpoints", 0x00000802, 0x00000001, "typing.List[TlsClientManagement.Structs.TLSEndpointStruct]", None, "[]")

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000802, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000802, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000802, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000802, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000802, 0x0000FFFD, "uint", 0)
