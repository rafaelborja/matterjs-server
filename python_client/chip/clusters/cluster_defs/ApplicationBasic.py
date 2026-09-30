"""ApplicationBasic cluster definition (auto-generated, DO NOT edit)."""

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
class ApplicationBasic(Cluster):
    id: typing.ClassVar[int] = 0x0000050D

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="vendorName", Tag=0x00000000, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="vendorID", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="applicationName", Tag=0x00000002, Type=str),
                ClusterObjectFieldDescriptor(Label="productID", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="application", Tag=0x00000004, Type=ApplicationBasic.Structs.ApplicationStruct),
                ClusterObjectFieldDescriptor(Label="status", Tag=0x00000005, Type=ApplicationBasic.Enums.ApplicationStatusEnum),
                ClusterObjectFieldDescriptor(Label="applicationVersion", Tag=0x00000006, Type=str),
                ClusterObjectFieldDescriptor(Label="allowedVendorList", Tag=0x00000007, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    vendorName: typing.Optional[str] = None
    vendorID: typing.Optional[uint] = None
    applicationName: str = ""
    productID: typing.Optional[uint] = None
    application: ApplicationBasic.Structs.ApplicationStruct = field(default_factory=lambda: ApplicationBasic.Structs.ApplicationStruct())
    status: ApplicationBasic.Enums.ApplicationStatusEnum = 0
    applicationVersion: str = ""
    allowedVendorList: typing.List[uint] = field(default_factory=lambda: [])
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class ApplicationStatusEnum(MatterIntEnum):
            kStopped = 0x00
            kActiveVisibleFocus = 0x01
            kActiveHidden = 0x02
            kActiveVisibleNotFocus = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Structs:
        @dataclass
        class ApplicationStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="catalogVendorID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="applicationID", Tag=1, Type=str),
                    ])

            catalogVendorID: uint = 0
            applicationID: str = ""

    class Attributes:
        VendorName = _attr(__module__, __qualname__, "VendorName", 0x0000050D, 0x00000000, "typing.Optional[str]", None)

        VendorID = _attr(__module__, __qualname__, "VendorID", 0x0000050D, 0x00000001, "typing.Optional[uint]", None)

        ApplicationName = _attr(__module__, __qualname__, "ApplicationName", 0x0000050D, 0x00000002, "str", "")

        ProductID = _attr(__module__, __qualname__, "ProductID", 0x0000050D, 0x00000003, "typing.Optional[uint]", None)

        Application = _attr(__module__, __qualname__, "Application", 0x0000050D, 0x00000004, "ApplicationBasic.Structs.ApplicationStruct", None, "ApplicationBasic.Structs.ApplicationStruct()")

        Status = _attr(__module__, __qualname__, "Status", 0x0000050D, 0x00000005, "ApplicationBasic.Enums.ApplicationStatusEnum", 0)

        ApplicationVersion = _attr(__module__, __qualname__, "ApplicationVersion", 0x0000050D, 0x00000006, "str", "")

        AllowedVendorList = _attr(__module__, __qualname__, "AllowedVendorList", 0x0000050D, 0x00000007, "typing.List[uint]", None, "[]")

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000050D, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000050D, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000050D, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000050D, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000050D, 0x0000FFFD, "uint", 0)
