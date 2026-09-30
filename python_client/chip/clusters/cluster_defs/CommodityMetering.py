"""CommodityMetering cluster definition (auto-generated, DO NOT edit)."""

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
class CommodityMetering(Cluster):
    id: typing.ClassVar[int] = 0x00000B07

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="meteredQuantity", Tag=0x00000000, Type=typing.Union[Nullable, typing.List[CommodityMetering.Structs.MeteredQuantityStruct]]),
                ClusterObjectFieldDescriptor(Label="meteredQuantityTimestamp", Tag=0x00000001, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="tariffUnit", Tag=0x00000002, Type=typing.Union[Nullable, Globals.Enums.TariffUnitEnum]),
                ClusterObjectFieldDescriptor(Label="maximumMeteredQuantities", Tag=0x00000003, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    meteredQuantity: typing.Union[Nullable, typing.List[CommodityMetering.Structs.MeteredQuantityStruct]] = NullValue
    meteredQuantityTimestamp: typing.Union[Nullable, uint] = NullValue
    tariffUnit: typing.Union[Nullable, Globals.Enums.TariffUnitEnum] = NullValue
    maximumMeteredQuantities: typing.Union[Nullable, uint] = NullValue
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Structs:
        @dataclass
        class MeteredQuantityStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="tariffComponentIDs", Tag=0, Type=typing.List[uint]),
                        ClusterObjectFieldDescriptor(Label="quantity", Tag=1, Type=int),
                    ])

            tariffComponentIDs: typing.List[uint] = field(default_factory=lambda: [])
            quantity: int = 0

    class Attributes:
        MeteredQuantity = _attr(__module__, __qualname__, "MeteredQuantity", 0x00000B07, 0x00000000, "typing.Union[Nullable, typing.List[CommodityMetering.Structs.MeteredQuantityStruct]]", NullValue)

        MeteredQuantityTimestamp = _attr(__module__, __qualname__, "MeteredQuantityTimestamp", 0x00000B07, 0x00000001, "typing.Union[Nullable, uint]", NullValue)

        TariffUnit = _attr(__module__, __qualname__, "TariffUnit", 0x00000B07, 0x00000002, "typing.Union[Nullable, Globals.Enums.TariffUnitEnum]", NullValue)

        MaximumMeteredQuantities = _attr(__module__, __qualname__, "MaximumMeteredQuantities", 0x00000B07, 0x00000003, "typing.Union[Nullable, uint]", NullValue)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000B07, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000B07, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000B07, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000B07, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000B07, 0x0000FFFD, "uint", 0)
