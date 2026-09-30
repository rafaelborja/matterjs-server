"""EthernetNetworkDiagnostics cluster definition (auto-generated, DO NOT edit)."""

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
class EthernetNetworkDiagnostics(Cluster):
    id: typing.ClassVar[int] = 0x00000037

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="PHYRate", Tag=0x00000000, Type=typing.Union[None, Nullable, EthernetNetworkDiagnostics.Enums.PHYRateEnum]),
                ClusterObjectFieldDescriptor(Label="fullDuplex", Tag=0x00000001, Type=typing.Union[None, Nullable, bool]),
                ClusterObjectFieldDescriptor(Label="packetRxCount", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="packetTxCount", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="txErrCount", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="collisionCount", Tag=0x00000005, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="overrunCount", Tag=0x00000006, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="carrierDetect", Tag=0x00000007, Type=typing.Union[None, Nullable, bool]),
                ClusterObjectFieldDescriptor(Label="timeSinceReset", Tag=0x00000008, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    PHYRate: typing.Union[None, Nullable, EthernetNetworkDiagnostics.Enums.PHYRateEnum] = None
    fullDuplex: typing.Union[None, Nullable, bool] = None
    packetRxCount: typing.Optional[uint] = None
    packetTxCount: typing.Optional[uint] = None
    txErrCount: typing.Optional[uint] = None
    collisionCount: typing.Optional[uint] = None
    overrunCount: typing.Optional[uint] = None
    carrierDetect: typing.Union[None, Nullable, bool] = None
    timeSinceReset: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class PHYRateEnum(MatterIntEnum):
            kRate10M = 0x00
            kRate100M = 0x01
            kRate1G = 0x02
            kRate25g = 0x03
            kRate5G = 0x04
            kRate10G = 0x05
            kRate40G = 0x06
            kRate100G = 0x07
            kRate200G = 0x08
            kRate400G = 0x09
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 10

    class Bitmaps:
        class Feature(IntFlag):
            kPacketCounts = 0x1
            kErrorCounts = 0x2

    class Commands:
        @dataclass
        class ResetCounts(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000037
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


    class Attributes:
        PHYRate = _attr(__module__, __qualname__, "PHYRate", 0x00000037, 0x00000000, "typing.Union[None, Nullable, EthernetNetworkDiagnostics.Enums.PHYRateEnum]", None)

        FullDuplex = _attr(__module__, __qualname__, "FullDuplex", 0x00000037, 0x00000001, "typing.Union[None, Nullable, bool]", None)

        PacketRxCount = _attr(__module__, __qualname__, "PacketRxCount", 0x00000037, 0x00000002, "typing.Optional[uint]", None)

        PacketTxCount = _attr(__module__, __qualname__, "PacketTxCount", 0x00000037, 0x00000003, "typing.Optional[uint]", None)

        TxErrCount = _attr(__module__, __qualname__, "TxErrCount", 0x00000037, 0x00000004, "typing.Optional[uint]", None)

        CollisionCount = _attr(__module__, __qualname__, "CollisionCount", 0x00000037, 0x00000005, "typing.Optional[uint]", None)

        OverrunCount = _attr(__module__, __qualname__, "OverrunCount", 0x00000037, 0x00000006, "typing.Optional[uint]", None)

        CarrierDetect = _attr(__module__, __qualname__, "CarrierDetect", 0x00000037, 0x00000007, "typing.Union[None, Nullable, bool]", None)

        TimeSinceReset = _attr(__module__, __qualname__, "TimeSinceReset", 0x00000037, 0x00000008, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000037, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000037, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000037, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000037, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000037, 0x0000FFFD, "uint", 0)
