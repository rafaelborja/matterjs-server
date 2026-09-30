"""LaundryWasherControls cluster definition (auto-generated, DO NOT edit)."""

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
class LaundryWasherControls(Cluster):
    id: typing.ClassVar[int] = 0x00000053

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="spinSpeeds", Tag=0x00000000, Type=typing.Optional[typing.List[str]]),
                ClusterObjectFieldDescriptor(Label="spinSpeedCurrent", Tag=0x00000001, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="numberOfRinses", Tag=0x00000002, Type=typing.Optional[LaundryWasherControls.Enums.NumberOfRinsesEnum]),
                ClusterObjectFieldDescriptor(Label="supportedRinses", Tag=0x00000003, Type=typing.Optional[typing.List[LaundryWasherControls.Enums.NumberOfRinsesEnum]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    spinSpeeds: typing.Optional[typing.List[str]] = None
    spinSpeedCurrent: typing.Union[None, Nullable, uint] = None
    numberOfRinses: typing.Optional[LaundryWasherControls.Enums.NumberOfRinsesEnum] = None
    supportedRinses: typing.Optional[typing.List[LaundryWasherControls.Enums.NumberOfRinsesEnum]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class NumberOfRinsesEnum(MatterIntEnum):
            kNone = 0x00
            kNormal = 0x01
            kExtra = 0x02
            kMax = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Bitmaps:
        class Feature(IntFlag):
            kSpin = 0x1
            kRinse = 0x2

    class Attributes:
        SpinSpeeds = _attr(__module__, __qualname__, "SpinSpeeds", 0x00000053, 0x00000000, "typing.Optional[typing.List[str]]", None)

        SpinSpeedCurrent = _attr(__module__, __qualname__, "SpinSpeedCurrent", 0x00000053, 0x00000001, "typing.Union[None, Nullable, uint]", None)

        NumberOfRinses = _attr(__module__, __qualname__, "NumberOfRinses", 0x00000053, 0x00000002, "typing.Optional[LaundryWasherControls.Enums.NumberOfRinsesEnum]", None)

        SupportedRinses = _attr(__module__, __qualname__, "SupportedRinses", 0x00000053, 0x00000003, "typing.Optional[typing.List[LaundryWasherControls.Enums.NumberOfRinsesEnum]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000053, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000053, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000053, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000053, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000053, 0x0000FFFD, "uint", 0)
