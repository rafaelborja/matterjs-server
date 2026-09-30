"""WaterTankLevelMonitoring cluster definition (auto-generated, DO NOT edit)."""

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
class WaterTankLevelMonitoring(Cluster):
    id: typing.ClassVar[int] = 0x00000079

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="condition", Tag=0x00000000, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="degradationDirection", Tag=0x00000001, Type=typing.Optional[WaterTankLevelMonitoring.Enums.DegradationDirectionEnum]),
                ClusterObjectFieldDescriptor(Label="changeIndication", Tag=0x00000002, Type=WaterTankLevelMonitoring.Enums.ChangeIndicationEnum),
                ClusterObjectFieldDescriptor(Label="inPlaceIndicator", Tag=0x00000003, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="lastChangedTime", Tag=0x00000004, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="replacementProductList", Tag=0x00000005, Type=typing.Optional[typing.List[WaterTankLevelMonitoring.Structs.ReplacementProductStruct]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    condition: typing.Optional[uint] = None
    degradationDirection: typing.Optional[WaterTankLevelMonitoring.Enums.DegradationDirectionEnum] = None
    changeIndication: WaterTankLevelMonitoring.Enums.ChangeIndicationEnum = 0
    inPlaceIndicator: typing.Optional[bool] = None
    lastChangedTime: typing.Union[None, Nullable, uint] = None
    replacementProductList: typing.Optional[typing.List[WaterTankLevelMonitoring.Structs.ReplacementProductStruct]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class DegradationDirectionEnum(MatterIntEnum):
            kUp = 0x00
            kDown = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class ChangeIndicationEnum(MatterIntEnum):
            kOk = 0x00
            kWarning = 0x01
            kCritical = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class ProductIdentifierTypeEnum(MatterIntEnum):
            kUpc = 0x00
            kGtin8 = 0x01
            kEan = 0x02
            kGtin14 = 0x03
            kOem = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

    class Bitmaps:
        class Feature(IntFlag):
            kCondition = 0x1
            kWarning = 0x2
            kReplacementProductList = 0x4

    class Structs:
        @dataclass
        class ReplacementProductStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="productIdentifierType", Tag=0, Type=WaterTankLevelMonitoring.Enums.ProductIdentifierTypeEnum),
                        ClusterObjectFieldDescriptor(Label="productIdentifierValue", Tag=1, Type=str),
                    ])

            productIdentifierType: WaterTankLevelMonitoring.Enums.ProductIdentifierTypeEnum = 0
            productIdentifierValue: str = ""

    class Commands:
        @dataclass
        class ResetCondition(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000079
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


    class Attributes:
        Condition = _attr(__module__, __qualname__, "Condition", 0x00000079, 0x00000000, "typing.Optional[uint]", None)

        DegradationDirection = _attr(__module__, __qualname__, "DegradationDirection", 0x00000079, 0x00000001, "typing.Optional[WaterTankLevelMonitoring.Enums.DegradationDirectionEnum]", None)

        ChangeIndication = _attr(__module__, __qualname__, "ChangeIndication", 0x00000079, 0x00000002, "WaterTankLevelMonitoring.Enums.ChangeIndicationEnum", 0)

        InPlaceIndicator = _attr(__module__, __qualname__, "InPlaceIndicator", 0x00000079, 0x00000003, "typing.Optional[bool]", None)

        LastChangedTime = _attr(__module__, __qualname__, "LastChangedTime", 0x00000079, 0x00000004, "typing.Union[None, Nullable, uint]", None)

        ReplacementProductList = _attr(__module__, __qualname__, "ReplacementProductList", 0x00000079, 0x00000005, "typing.Optional[typing.List[WaterTankLevelMonitoring.Structs.ReplacementProductStruct]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000079, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000079, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000079, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000079, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000079, 0x0000FFFD, "uint", 0)
