"""CommissionerControl cluster definition (auto-generated, DO NOT edit)."""

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
class CommissionerControl(Cluster):
    id: typing.ClassVar[int] = 0x00000751

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="supportedDeviceCategories", Tag=0x00000000, Type=CommissionerControl.Bitmaps.SupportedDeviceCategoryBitmap),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    supportedDeviceCategories: CommissionerControl.Bitmaps.SupportedDeviceCategoryBitmap = 0
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class SupportedDeviceCategoryBitmap(IntFlag):
            kFabricSynchronization = 0x1

    class Commands:
        @dataclass
        class RequestCommissioningApproval(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000751
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="requestID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="vendorID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="productID", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="label", Tag=3, Type=typing.Optional[str]),
                    ])

            requestID: uint = 0
            vendorID: uint = 0
            productID: uint = 0
            label: typing.Optional[str] = None

        @dataclass
        class CommissionNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000751
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'ReverseOpenCommissioningWindow'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="requestID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="responseTimeoutSeconds", Tag=1, Type=uint),
                    ])

            requestID: uint = 0
            responseTimeoutSeconds: uint = 0

        @dataclass
        class ReverseOpenCommissioningWindow(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000751
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="commissioningTimeout", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="PAKEPasscodeVerifier", Tag=1, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="discriminator", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="iterations", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="salt", Tag=4, Type=bytes),
                    ])

            commissioningTimeout: uint = 0
            PAKEPasscodeVerifier: bytes = b""
            discriminator: uint = 0
            iterations: uint = 0
            salt: bytes = b""

    class Attributes:
        SupportedDeviceCategories = _attr(__module__, __qualname__, "SupportedDeviceCategories", 0x00000751, 0x00000000, "CommissionerControl.Bitmaps.SupportedDeviceCategoryBitmap", 0)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000751, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000751, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000751, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000751, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000751, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class CommissioningRequestResult(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000751

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="requestID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="clientNodeID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="statusCode", Tag=2, Type=Globals.Enums.status),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            requestID: uint = 0
            clientNodeID: uint = 0
            statusCode: Globals.Enums.status = 0
            fabricIndex: uint = 0
