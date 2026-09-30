"""IcdManagement cluster definition (auto-generated, DO NOT edit)."""

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
class IcdManagement(Cluster):
    id: typing.ClassVar[int] = 0x00000046

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="idleModeDuration", Tag=0x00000000, Type=uint),
                ClusterObjectFieldDescriptor(Label="activeModeDuration", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="activeModeThreshold", Tag=0x00000002, Type=uint),
                ClusterObjectFieldDescriptor(Label="registeredClients", Tag=0x00000003, Type=typing.Optional[typing.List[IcdManagement.Structs.MonitoringRegistrationStruct]]),
                ClusterObjectFieldDescriptor(Label="ICDCounter", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="clientsSupportedPerFabric", Tag=0x00000005, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="userActiveModeTriggerHint", Tag=0x00000006, Type=typing.Optional[IcdManagement.Bitmaps.UserActiveModeTriggerBitmap]),
                ClusterObjectFieldDescriptor(Label="userActiveModeTriggerInstruction", Tag=0x00000007, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="operatingMode", Tag=0x00000008, Type=typing.Optional[IcdManagement.Enums.OperatingModeEnum]),
                ClusterObjectFieldDescriptor(Label="maximumCheckInBackoff", Tag=0x00000009, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    idleModeDuration: uint = 0
    activeModeDuration: uint = 0
    activeModeThreshold: uint = 0
    registeredClients: typing.Optional[typing.List[IcdManagement.Structs.MonitoringRegistrationStruct]] = None
    ICDCounter: typing.Optional[uint] = None
    clientsSupportedPerFabric: typing.Optional[uint] = None
    userActiveModeTriggerHint: typing.Optional[IcdManagement.Bitmaps.UserActiveModeTriggerBitmap] = None
    userActiveModeTriggerInstruction: typing.Optional[str] = None
    operatingMode: typing.Optional[IcdManagement.Enums.OperatingModeEnum] = None
    maximumCheckInBackoff: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class ClientTypeEnum(MatterIntEnum):
            kPermanent = 0x00
            kEphemeral = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class OperatingModeEnum(MatterIntEnum):
            kSit = 0x00
            kLit = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Bitmaps:
        class Feature(IntFlag):
            kCheckInProtocolSupport = 0x1
            kUserActiveModeTrigger = 0x2
            kLongIdleTimeSupport = 0x4
            kDynamicSitLitSupport = 0x8

        class UserActiveModeTriggerBitmap(IntFlag):
            kPowerCycle = 0x1
            kSettingsMenu = 0x2
            kCustomInstruction = 0x4
            kDeviceManual = 0x8
            kActuateSensor = 0x10
            kActuateSensorSeconds = 0x20
            kActuateSensorTimes = 0x40
            kActuateSensorLightsBlink = 0x80
            kResetButton = 0x100
            kResetButtonLightsBlink = 0x200
            kResetButtonSeconds = 0x400
            kResetButtonTimes = 0x800
            kSetupButton = 0x1000
            kSetupButtonSeconds = 0x2000
            kSetupButtonLightsBlink = 0x4000
            kSetupButtonTimes = 0x8000
            kAppDefinedButton = 0x10000

    class Structs:
        @dataclass
        class MonitoringRegistrationStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="checkInNodeID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="monitoredSubject", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="key", Tag=3, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="clientType", Tag=4, Type=IcdManagement.Enums.ClientTypeEnum),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            checkInNodeID: uint = 0
            monitoredSubject: uint = 0
            key: typing.Optional[uint] = None
            clientType: IcdManagement.Enums.ClientTypeEnum = 0
            fabricIndex: uint = 0

    class Commands:
        @dataclass
        class RegisterClient(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000046
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'RegisterClientResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="checkInNodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="monitoredSubject", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="key", Tag=2, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="verificationKey", Tag=3, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="clientType", Tag=4, Type=IcdManagement.Enums.ClientTypeEnum),
                    ])

            checkInNodeID: uint = 0
            monitoredSubject: uint = 0
            key: bytes = b""
            verificationKey: typing.Optional[bytes] = None
            clientType: IcdManagement.Enums.ClientTypeEnum = 0

        @dataclass
        class UnregisterClient(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000046
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="checkInNodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="verificationKey", Tag=1, Type=typing.Optional[bytes]),
                    ])

            checkInNodeID: uint = 0
            verificationKey: typing.Optional[bytes] = None

        @dataclass
        class StayActiveRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000046
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'StayActiveResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stayActiveDuration", Tag=0, Type=uint),
                    ])

            stayActiveDuration: uint = 0

        @dataclass
        class RegisterClientResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000046
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="ICDCounter", Tag=0, Type=uint),
                    ])

            ICDCounter: uint = 0

        @dataclass
        class StayActiveResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000046
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="promisedActiveDuration", Tag=0, Type=uint),
                    ])

            promisedActiveDuration: uint = 0

    class Attributes:
        IdleModeDuration = _attr(__module__, __qualname__, "IdleModeDuration", 0x00000046, 0x00000000, "uint", 0)

        ActiveModeDuration = _attr(__module__, __qualname__, "ActiveModeDuration", 0x00000046, 0x00000001, "uint", 0)

        ActiveModeThreshold = _attr(__module__, __qualname__, "ActiveModeThreshold", 0x00000046, 0x00000002, "uint", 0)

        RegisteredClients = _attr(__module__, __qualname__, "RegisteredClients", 0x00000046, 0x00000003, "typing.Optional[typing.List[IcdManagement.Structs.MonitoringRegistrationStruct]]", None)

        ICDCounter = _attr(__module__, __qualname__, "ICDCounter", 0x00000046, 0x00000004, "typing.Optional[uint]", None)

        ClientsSupportedPerFabric = _attr(__module__, __qualname__, "ClientsSupportedPerFabric", 0x00000046, 0x00000005, "typing.Optional[uint]", None)

        UserActiveModeTriggerHint = _attr(__module__, __qualname__, "UserActiveModeTriggerHint", 0x00000046, 0x00000006, "typing.Optional[IcdManagement.Bitmaps.UserActiveModeTriggerBitmap]", None)

        UserActiveModeTriggerInstruction = _attr(__module__, __qualname__, "UserActiveModeTriggerInstruction", 0x00000046, 0x00000007, "typing.Optional[str]", None)

        OperatingMode = _attr(__module__, __qualname__, "OperatingMode", 0x00000046, 0x00000008, "typing.Optional[IcdManagement.Enums.OperatingModeEnum]", None)

        MaximumCheckInBackOff = _attr(__module__, __qualname__, "MaximumCheckInBackOff", 0x00000046, 0x00000009, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000046, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000046, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000046, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000046, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000046, 0x0000FFFD, "uint", 0)
