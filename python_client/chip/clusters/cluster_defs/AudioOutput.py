"""AudioOutput cluster definition (auto-generated, DO NOT edit)."""

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
class AudioOutput(Cluster):
    id: typing.ClassVar[int] = 0x0000050B

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="outputList", Tag=0x00000000, Type=typing.List[AudioOutput.Structs.OutputInfoStruct]),
                ClusterObjectFieldDescriptor(Label="currentOutput", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    outputList: typing.List[AudioOutput.Structs.OutputInfoStruct] = field(default_factory=lambda: [])
    currentOutput: uint = 0
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class OutputTypeEnum(MatterIntEnum):
            kHdmi = 0x00
            kBt = 0x01
            kOptical = 0x02
            kHeadphone = 0x03
            kInternal = 0x04
            kOther = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

    class Bitmaps:
        class Feature(IntFlag):
            kNameUpdates = 0x1

    class Structs:
        @dataclass
        class OutputInfoStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="index", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="outputType", Tag=1, Type=AudioOutput.Enums.OutputTypeEnum),
                        ClusterObjectFieldDescriptor(Label="name", Tag=2, Type=str),
                    ])

            index: uint = 0
            outputType: AudioOutput.Enums.OutputTypeEnum = 0
            name: str = ""

    class Commands:
        @dataclass
        class SelectOutput(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050B
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="index", Tag=0, Type=uint),
                    ])

            index: uint = 0

        @dataclass
        class RenameOutput(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050B
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="index", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="name", Tag=1, Type=str),
                    ])

            index: uint = 0
            name: str = ""

    class Attributes:
        OutputList = _attr(__module__, __qualname__, "OutputList", 0x0000050B, 0x00000000, "typing.List[AudioOutput.Structs.OutputInfoStruct]", None, "[]")

        CurrentOutput = _attr(__module__, __qualname__, "CurrentOutput", 0x0000050B, 0x00000001, "uint", 0)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000050B, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000050B, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000050B, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000050B, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000050B, 0x0000FFFD, "uint", 0)
