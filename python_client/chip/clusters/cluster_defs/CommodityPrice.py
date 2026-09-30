"""CommodityPrice cluster definition (auto-generated, DO NOT edit)."""

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
class CommodityPrice(Cluster):
    id: typing.ClassVar[int] = 0x00000095

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="tariffUnit", Tag=0x00000000, Type=Globals.Enums.TariffUnitEnum),
                ClusterObjectFieldDescriptor(Label="currency", Tag=0x00000001, Type=typing.Union[Nullable, Globals.Structs.currency]),
                ClusterObjectFieldDescriptor(Label="currentPrice", Tag=0x00000002, Type=typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct]),
                ClusterObjectFieldDescriptor(Label="priceForecast", Tag=0x00000003, Type=typing.Optional[typing.List[CommodityPrice.Structs.CommodityPriceStruct]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    tariffUnit: Globals.Enums.TariffUnitEnum = 0
    currency: typing.Union[Nullable, Globals.Structs.currency] = NullValue
    currentPrice: typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct] = NullValue
    priceForecast: typing.Optional[typing.List[CommodityPrice.Structs.CommodityPriceStruct]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Bitmaps:
        class Feature(IntFlag):
            kForecasting = 0x1

        class CommodityPriceDetailBitmap(IntFlag):
            kDescription = 0x1
            kComponents = 0x2

    class Structs:
        @dataclass
        class CommodityPriceComponentStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="price", Tag=0, Type=int),
                        ClusterObjectFieldDescriptor(Label="source", Tag=1, Type=Globals.Enums.TariffPriceTypeEnum),
                        ClusterObjectFieldDescriptor(Label="description", Tag=2, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="tariffComponentID", Tag=3, Type=typing.Optional[uint]),
                    ])

            price: int = 0
            source: Globals.Enums.TariffPriceTypeEnum = 0
            description: typing.Optional[str] = None
            tariffComponentID: typing.Optional[uint] = None

        @dataclass
        class CommodityPriceStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="periodStart", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="periodEnd", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="price", Tag=2, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="priceLevel", Tag=3, Type=typing.Optional[int]),
                        ClusterObjectFieldDescriptor(Label="description", Tag=4, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="components", Tag=5, Type=typing.Optional[typing.List[CommodityPrice.Structs.CommodityPriceComponentStruct]]),
                    ])

            periodStart: uint = 0
            periodEnd: typing.Union[Nullable, uint] = NullValue
            price: typing.Optional[int] = None
            priceLevel: typing.Optional[int] = None
            description: typing.Optional[str] = None
            components: typing.Optional[typing.List[CommodityPrice.Structs.CommodityPriceComponentStruct]] = None

    class Commands:
        @dataclass
        class GetDetailedPriceRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000095
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'GetDetailedPriceResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="details", Tag=0, Type=CommodityPrice.Bitmaps.CommodityPriceDetailBitmap),
                    ])

            details: CommodityPrice.Bitmaps.CommodityPriceDetailBitmap = 0

        @dataclass
        class GetDetailedForecastRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000095
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'GetDetailedForecastResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="details", Tag=0, Type=CommodityPrice.Bitmaps.CommodityPriceDetailBitmap),
                    ])

            details: CommodityPrice.Bitmaps.CommodityPriceDetailBitmap = 0

        @dataclass
        class GetDetailedPriceResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000095
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="currentPrice", Tag=0, Type=typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct]),
                    ])

            currentPrice: typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct] = NullValue

        @dataclass
        class GetDetailedForecastResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000095
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="priceForecast", Tag=0, Type=typing.List[CommodityPrice.Structs.CommodityPriceStruct]),
                    ])

            priceForecast: typing.List[CommodityPrice.Structs.CommodityPriceStruct] = field(default_factory=lambda: [])

    class Attributes:
        TariffUnit = _attr(__module__, __qualname__, "TariffUnit", 0x00000095, 0x00000000, "Globals.Enums.TariffUnitEnum", 0)

        Currency = _attr(__module__, __qualname__, "Currency", 0x00000095, 0x00000001, "typing.Union[Nullable, Globals.Structs.currency]", NullValue)

        CurrentPrice = _attr(__module__, __qualname__, "CurrentPrice", 0x00000095, 0x00000002, "typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct]", NullValue)

        PriceForecast = _attr(__module__, __qualname__, "PriceForecast", 0x00000095, 0x00000003, "typing.Optional[typing.List[CommodityPrice.Structs.CommodityPriceStruct]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000095, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000095, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000095, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000095, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000095, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class PriceChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x00000095

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="currentPrice", Tag=0, Type=typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct]),
                    ])

            currentPrice: typing.Union[Nullable, CommodityPrice.Structs.CommodityPriceStruct] = NullValue
