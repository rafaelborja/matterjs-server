"""MediaInput cluster definition (auto-generated, DO NOT edit)."""

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
class MediaInput(Cluster):
    id: typing.ClassVar[int] = 0x00000507

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="inputList", Tag=0x00000000, Type=typing.List[MediaInput.Structs.InputInfoStruct]),
                ClusterObjectFieldDescriptor(Label="currentInput", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    inputList: typing.List[MediaInput.Structs.InputInfoStruct] = field(default_factory=lambda: [])
    currentInput: uint = 0
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class InputTypeEnum(MatterIntEnum):
            kInternal = 0x00
            kAux = 0x01
            kCoax = 0x02
            kComposite = 0x03
            kHdmi = 0x04
            kInput = 0x05
            kLine = 0x06
            kOptical = 0x07
            kVideo = 0x08
            kScart = 0x09
            kUsb = 0x0A
            kOther = 0x0B
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 12

    class Bitmaps:
        class Feature(IntFlag):
            kNameUpdates = 0x1

    class Structs:
        @dataclass
        class InputInfoStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="index", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="inputType", Tag=1, Type=MediaInput.Enums.InputTypeEnum),
                        ClusterObjectFieldDescriptor(Label="name", Tag=2, Type=str),
                        ClusterObjectFieldDescriptor(Label="description", Tag=3, Type=str),
                    ])

            index: uint = 0
            inputType: MediaInput.Enums.InputTypeEnum = 0
            name: str = ""
            description: str = ""

    class Commands:
        @dataclass
        class SelectInput(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000507
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
        class ShowInputStatus(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000507
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class HideInputStatus(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000507
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                    ])


        @dataclass
        class RenameInput(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000507
            command_id: typing.ClassVar[int] = 0x00000003
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
        InputList = _attr(__module__, __qualname__, "InputList", 0x00000507, 0x00000000, "typing.List[MediaInput.Structs.InputInfoStruct]", None, "[]")

        CurrentInput = _attr(__module__, __qualname__, "CurrentInput", 0x00000507, 0x00000001, "uint", 0)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000507, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000507, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000507, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000507, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000507, 0x0000FFFD, "uint", 0)
