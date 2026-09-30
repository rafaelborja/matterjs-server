"""BasicInformation cluster definition (auto-generated, DO NOT edit)."""

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
class BasicInformation(Cluster):
    id: typing.ClassVar[int] = 0x00000028

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="dataModelRevision", Tag=0x00000000, Type=uint),
                ClusterObjectFieldDescriptor(Label="vendorName", Tag=0x00000001, Type=str),
                ClusterObjectFieldDescriptor(Label="vendorID", Tag=0x00000002, Type=uint),
                ClusterObjectFieldDescriptor(Label="productName", Tag=0x00000003, Type=str),
                ClusterObjectFieldDescriptor(Label="productID", Tag=0x00000004, Type=uint),
                ClusterObjectFieldDescriptor(Label="nodeLabel", Tag=0x00000005, Type=str),
                ClusterObjectFieldDescriptor(Label="location", Tag=0x00000006, Type=str),
                ClusterObjectFieldDescriptor(Label="hardwareVersion", Tag=0x00000007, Type=uint),
                ClusterObjectFieldDescriptor(Label="hardwareVersionString", Tag=0x00000008, Type=str),
                ClusterObjectFieldDescriptor(Label="softwareVersion", Tag=0x00000009, Type=uint),
                ClusterObjectFieldDescriptor(Label="softwareVersionString", Tag=0x0000000A, Type=str),
                ClusterObjectFieldDescriptor(Label="manufacturingDate", Tag=0x0000000B, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="partNumber", Tag=0x0000000C, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="productURL", Tag=0x0000000D, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="productLabel", Tag=0x0000000E, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="serialNumber", Tag=0x0000000F, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="localConfigDisabled", Tag=0x00000010, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="reachable", Tag=0x00000011, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="uniqueID", Tag=0x00000012, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="capabilityMinima", Tag=0x00000013, Type=BasicInformation.Structs.CapabilityMinimaStruct),
                ClusterObjectFieldDescriptor(Label="productAppearance", Tag=0x00000014, Type=typing.Optional[BasicInformation.Structs.ProductAppearanceStruct]),
                ClusterObjectFieldDescriptor(Label="specificationVersion", Tag=0x00000015, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="maxPathsPerInvoke", Tag=0x00000016, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="configurationVersion", Tag=0x00000018, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    dataModelRevision: uint = 0
    vendorName: str = ""
    vendorID: uint = 0
    productName: str = ""
    productID: uint = 0
    nodeLabel: str = ""
    location: str = ""
    hardwareVersion: uint = 0
    hardwareVersionString: str = ""
    softwareVersion: uint = 0
    softwareVersionString: str = ""
    manufacturingDate: typing.Optional[str] = None
    partNumber: typing.Optional[str] = None
    productURL: typing.Optional[str] = None
    productLabel: typing.Optional[str] = None
    serialNumber: typing.Optional[str] = None
    localConfigDisabled: typing.Optional[bool] = None
    reachable: typing.Optional[bool] = None
    uniqueID: typing.Optional[str] = None
    capabilityMinima: BasicInformation.Structs.CapabilityMinimaStruct = field(default_factory=lambda: BasicInformation.Structs.CapabilityMinimaStruct())
    productAppearance: typing.Optional[BasicInformation.Structs.ProductAppearanceStruct] = None
    specificationVersion: typing.Optional[uint] = None
    maxPathsPerInvoke: typing.Optional[uint] = None
    configurationVersion: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class ProductFinishEnum(MatterIntEnum):
            kOther = 0x00
            kMatte = 0x01
            kSatin = 0x02
            kPolished = 0x03
            kRugged = 0x04
            kFabric = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

        class ColorEnum(MatterIntEnum):
            kBlack = 0x00
            kNavy = 0x01
            kGreen = 0x02
            kTeal = 0x03
            kMaroon = 0x04
            kPurple = 0x05
            kOlive = 0x06
            kGray = 0x07
            kBlue = 0x08
            kLime = 0x09
            kAqua = 0x0A
            kRed = 0x0B
            kFuchsia = 0x0C
            kYellow = 0x0D
            kWhite = 0x0E
            kNickel = 0x0F
            kChrome = 0x10
            kBrass = 0x11
            kCopper = 0x12
            kSilver = 0x13
            kGold = 0x14
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 21

    class Structs:
        @dataclass
        class ProductAppearanceStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="finish", Tag=0, Type=BasicInformation.Enums.ProductFinishEnum),
                        ClusterObjectFieldDescriptor(Label="primaryColor", Tag=1, Type=typing.Union[Nullable, BasicInformation.Enums.ColorEnum]),
                    ])

            finish: BasicInformation.Enums.ProductFinishEnum = 0
            primaryColor: typing.Union[Nullable, BasicInformation.Enums.ColorEnum] = NullValue

        @dataclass
        class CapabilityMinimaStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="caseSessionsPerFabric", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="subscriptionsPerFabric", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="simultaneousInvocationsSupported", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="simultaneousWritesSupported", Tag=3, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="readPathsSupported", Tag=4, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="subscribePathsSupported", Tag=5, Type=typing.Optional[uint]),
                    ])

            caseSessionsPerFabric: uint = 0
            subscriptionsPerFabric: uint = 0
            simultaneousInvocationsSupported: typing.Optional[uint] = None
            simultaneousWritesSupported: typing.Optional[uint] = None
            readPathsSupported: typing.Optional[uint] = None
            subscribePathsSupported: typing.Optional[uint] = None

    class Attributes:
        DataModelRevision = _attr(__module__, __qualname__, "DataModelRevision", 0x00000028, 0x00000000, "uint", 0)

        VendorName = _attr(__module__, __qualname__, "VendorName", 0x00000028, 0x00000001, "str", "")

        VendorID = _attr(__module__, __qualname__, "VendorID", 0x00000028, 0x00000002, "uint", 0)

        ProductName = _attr(__module__, __qualname__, "ProductName", 0x00000028, 0x00000003, "str", "")

        ProductID = _attr(__module__, __qualname__, "ProductID", 0x00000028, 0x00000004, "uint", 0)

        NodeLabel = _attr(__module__, __qualname__, "NodeLabel", 0x00000028, 0x00000005, "str", "")

        Location = _attr(__module__, __qualname__, "Location", 0x00000028, 0x00000006, "str", "")

        HardwareVersion = _attr(__module__, __qualname__, "HardwareVersion", 0x00000028, 0x00000007, "uint", 0)

        HardwareVersionString = _attr(__module__, __qualname__, "HardwareVersionString", 0x00000028, 0x00000008, "str", "")

        SoftwareVersion = _attr(__module__, __qualname__, "SoftwareVersion", 0x00000028, 0x00000009, "uint", 0)

        SoftwareVersionString = _attr(__module__, __qualname__, "SoftwareVersionString", 0x00000028, 0x0000000A, "str", "")

        ManufacturingDate = _attr(__module__, __qualname__, "ManufacturingDate", 0x00000028, 0x0000000B, "typing.Optional[str]", None)

        PartNumber = _attr(__module__, __qualname__, "PartNumber", 0x00000028, 0x0000000C, "typing.Optional[str]", None)

        ProductURL = _attr(__module__, __qualname__, "ProductURL", 0x00000028, 0x0000000D, "typing.Optional[str]", None)

        ProductLabel = _attr(__module__, __qualname__, "ProductLabel", 0x00000028, 0x0000000E, "typing.Optional[str]", None)

        SerialNumber = _attr(__module__, __qualname__, "SerialNumber", 0x00000028, 0x0000000F, "typing.Optional[str]", None)

        LocalConfigDisabled = _attr(__module__, __qualname__, "LocalConfigDisabled", 0x00000028, 0x00000010, "typing.Optional[bool]", None)

        Reachable = _attr(__module__, __qualname__, "Reachable", 0x00000028, 0x00000011, "typing.Optional[bool]", None)

        UniqueID = _attr(__module__, __qualname__, "UniqueID", 0x00000028, 0x00000012, "typing.Optional[str]", None)

        CapabilityMinima = _attr(__module__, __qualname__, "CapabilityMinima", 0x00000028, 0x00000013, "BasicInformation.Structs.CapabilityMinimaStruct", None, "BasicInformation.Structs.CapabilityMinimaStruct()")

        ProductAppearance = _attr(__module__, __qualname__, "ProductAppearance", 0x00000028, 0x00000014, "typing.Optional[BasicInformation.Structs.ProductAppearanceStruct]", None)

        SpecificationVersion = _attr(__module__, __qualname__, "SpecificationVersion", 0x00000028, 0x00000015, "typing.Optional[uint]", None)

        MaxPathsPerInvoke = _attr(__module__, __qualname__, "MaxPathsPerInvoke", 0x00000028, 0x00000016, "typing.Optional[uint]", None)

        ConfigurationVersion = _attr(__module__, __qualname__, "ConfigurationVersion", 0x00000028, 0x00000018, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000028, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000028, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000028, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000028, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000028, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class StartUp(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000028

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="softwareVersion", Tag=0, Type=uint),
                    ])

            softwareVersion: uint = 0

        @dataclass
        class ShutDown(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000028

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class Leave(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000028

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000002

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=0, Type=uint),
                    ])

            fabricIndex: uint = 0

        @dataclass
        class ReachableChanged(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000028

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000003

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="reachableNewValue", Tag=0, Type=bool),
                    ])

            reachableNewValue: bool = False
