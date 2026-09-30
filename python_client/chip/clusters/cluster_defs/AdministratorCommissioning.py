"""AdministratorCommissioning cluster definition (auto-generated, DO NOT edit)."""

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
class AdministratorCommissioning(Cluster):
    id: typing.ClassVar[int] = 0x0000003C

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="windowStatus", Tag=0x00000000, Type=AdministratorCommissioning.Enums.CommissioningWindowStatusEnum),
                ClusterObjectFieldDescriptor(Label="adminFabricIndex", Tag=0x00000001, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="adminVendorId", Tag=0x00000002, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    windowStatus: AdministratorCommissioning.Enums.CommissioningWindowStatusEnum = 0
    adminFabricIndex: typing.Union[Nullable, uint] = NullValue
    adminVendorId: typing.Union[Nullable, uint] = NullValue
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class CommissioningWindowStatusEnum(MatterIntEnum):
            kWindowNotOpen = 0x00
            kEnhancedWindowOpen = 0x01
            kBasicWindowOpen = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class StatusCode(MatterIntEnum):
            kBusy = 0x02
            kPAKEParameterError = 0x03
            kWindowNotOpen = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

    class Bitmaps:
        class Feature(IntFlag):
            kBasic = 0x1

    class Commands:
        @dataclass
        class OpenCommissioningWindow(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003C
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

        @dataclass
        class OpenBasicCommissioningWindow(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003C
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
                        ClusterObjectFieldDescriptor(Label="commissioningTimeout", Tag=0, Type=uint),
                    ])

            commissioningTimeout: uint = 0

        @dataclass
        class RevokeCommissioning(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003C
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
                    ])


    class Attributes:
        WindowStatus = _attr(__module__, __qualname__, "WindowStatus", 0x0000003C, 0x00000000, "AdministratorCommissioning.Enums.CommissioningWindowStatusEnum", 0)

        AdminFabricIndex = _attr(__module__, __qualname__, "AdminFabricIndex", 0x0000003C, 0x00000001, "typing.Union[Nullable, uint]", NullValue)

        AdminVendorId = _attr(__module__, __qualname__, "AdminVendorId", 0x0000003C, 0x00000002, "typing.Union[Nullable, uint]", NullValue)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000003C, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000003C, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000003C, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000003C, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000003C, 0x0000FFFD, "uint", 0)
