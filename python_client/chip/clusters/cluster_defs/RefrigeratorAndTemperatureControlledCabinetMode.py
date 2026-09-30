"""RefrigeratorAndTemperatureControlledCabinetMode cluster definition (auto-generated, DO NOT edit)."""

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
class RefrigeratorAndTemperatureControlledCabinetMode(Cluster):
    id: typing.ClassVar[int] = 0x00000052

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="supportedModes", Tag=0x00000000, Type=typing.List[RefrigeratorAndTemperatureControlledCabinetMode.Structs.ModeOptionStruct]),
                ClusterObjectFieldDescriptor(Label="currentMode", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="startUpMode", Tag=0x00000002, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="onMode", Tag=0x00000003, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    supportedModes: typing.List[RefrigeratorAndTemperatureControlledCabinetMode.Structs.ModeOptionStruct] = field(default_factory=lambda: [])
    currentMode: uint = 0
    startUpMode: typing.Union[None, Nullable, uint] = None
    onMode: typing.Union[None, Nullable, uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class ModeTag(MatterIntEnum):
            kAuto = 0x00
            kQuick = 0x01
            kQuiet = 0x02
            kLowNoise = 0x03
            kLowEnergy = 0x04
            kVacation = 0x05
            kMin = 0x06
            kMax = 0x07
            kNight = 0x08
            kDay = 0x09
            kRapidCool = 0x4000
            kRapidFreeze = 0x4001
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 16386

        class ModeChangeStatus(MatterIntEnum):
            kSuccess = 0x00
            kUnsupportedMode = 0x01
            kGenericFailure = 0x02
            kInvalidInMode = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Bitmaps:
        class Feature(IntFlag):
            kOnOff = 0x1

    class Structs:
        @dataclass
        class ModeOptionStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="label", Tag=0, Type=str),
                        ClusterObjectFieldDescriptor(Label="mode", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="modeTags", Tag=2, Type=typing.List[RefrigeratorAndTemperatureControlledCabinetMode.Structs.ModeTagStruct]),
                    ])

            label: str = ""
            mode: uint = 0
            modeTags: typing.List[RefrigeratorAndTemperatureControlledCabinetMode.Structs.ModeTagStruct] = field(default_factory=lambda: [])

        @dataclass
        class ModeTagStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mfgCode", Tag=0, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="value", Tag=1, Type=RefrigeratorAndTemperatureControlledCabinetMode.Enums.ModeTag),
                    ])

            mfgCode: typing.Optional[uint] = None
            value: RefrigeratorAndTemperatureControlledCabinetMode.Enums.ModeTag = 0

    class Commands:
        @dataclass
        class ChangeToMode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000052
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'ChangeToModeResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newMode", Tag=0, Type=uint),
                    ])

            newMode: uint = 0

        @dataclass
        class ChangeToModeResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000052
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="status", Tag=0, Type=RefrigeratorAndTemperatureControlledCabinetMode.Enums.ModeChangeStatus),
                        ClusterObjectFieldDescriptor(Label="statusText", Tag=1, Type=str),
                    ])

            status: RefrigeratorAndTemperatureControlledCabinetMode.Enums.ModeChangeStatus = 0
            statusText: str = ""

    class Attributes:
        SupportedModes = _attr(__module__, __qualname__, "SupportedModes", 0x00000052, 0x00000000, "typing.List[RefrigeratorAndTemperatureControlledCabinetMode.Structs.ModeOptionStruct]", None, "[]")

        CurrentMode = _attr(__module__, __qualname__, "CurrentMode", 0x00000052, 0x00000001, "uint", 0)

        StartUpMode = _attr(__module__, __qualname__, "StartUpMode", 0x00000052, 0x00000002, "typing.Union[None, Nullable, uint]", None)

        OnMode = _attr(__module__, __qualname__, "OnMode", 0x00000052, 0x00000003, "typing.Union[None, Nullable, uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000052, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000052, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000052, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000052, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000052, 0x0000FFFD, "uint", 0)
