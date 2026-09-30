"""ApplicationLauncher cluster definition (auto-generated, DO NOT edit)."""

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
class ApplicationLauncher(Cluster):
    id: typing.ClassVar[int] = 0x0000050C

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="catalogList", Tag=0x00000000, Type=typing.Optional[typing.List[uint]]),
                ClusterObjectFieldDescriptor(Label="currentApp", Tag=0x00000001, Type=typing.Union[None, Nullable, ApplicationLauncher.Structs.ApplicationEPStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    catalogList: typing.Optional[typing.List[uint]] = None
    currentApp: typing.Union[None, Nullable, ApplicationLauncher.Structs.ApplicationEPStruct] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class StatusEnum(MatterIntEnum):
            kSuccess = 0x00
            kAppNotAvailable = 0x01
            kSystemBusy = 0x02
            kPendingUserApproval = 0x03
            kDownloading = 0x04
            kInstalling = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

    class Bitmaps:
        class Feature(IntFlag):
            kApplicationPlatform = 0x1

    class Structs:
        @dataclass
        class ApplicationStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="catalogVendorID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="applicationID", Tag=1, Type=str),
                    ])

            catalogVendorID: uint = 0
            applicationID: str = ""

        @dataclass
        class ApplicationEPStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="application", Tag=0, Type=ApplicationLauncher.Structs.ApplicationStruct),
                        ClusterObjectFieldDescriptor(Label="endpoint", Tag=1, Type=typing.Optional[uint]),
                    ])

            application: ApplicationLauncher.Structs.ApplicationStruct = field(default_factory=lambda: ApplicationLauncher.Structs.ApplicationStruct())
            endpoint: typing.Optional[uint] = None

    class Commands:
        @dataclass
        class LaunchApp(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050C
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'LauncherResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="application", Tag=0, Type=typing.Optional[ApplicationLauncher.Structs.ApplicationStruct]),
                        ClusterObjectFieldDescriptor(Label="data", Tag=1, Type=typing.Optional[bytes]),
                    ])

            application: typing.Optional[ApplicationLauncher.Structs.ApplicationStruct] = None
            data: typing.Optional[bytes] = None

        @dataclass
        class StopApp(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050C
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'LauncherResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="application", Tag=0, Type=typing.Optional[ApplicationLauncher.Structs.ApplicationStruct]),
                    ])

            application: typing.Optional[ApplicationLauncher.Structs.ApplicationStruct] = None

        @dataclass
        class HideApp(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050C
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'LauncherResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="application", Tag=0, Type=typing.Optional[ApplicationLauncher.Structs.ApplicationStruct]),
                    ])

            application: typing.Optional[ApplicationLauncher.Structs.ApplicationStruct] = None

        @dataclass
        class LauncherResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000050C
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="status", Tag=0, Type=ApplicationLauncher.Enums.StatusEnum),
                        ClusterObjectFieldDescriptor(Label="data", Tag=1, Type=typing.Optional[bytes]),
                    ])

            status: ApplicationLauncher.Enums.StatusEnum = 0
            data: typing.Optional[bytes] = None

    class Attributes:
        CatalogList = _attr(__module__, __qualname__, "CatalogList", 0x0000050C, 0x00000000, "typing.Optional[typing.List[uint]]", None)

        CurrentApp = _attr(__module__, __qualname__, "CurrentApp", 0x0000050C, 0x00000001, "typing.Union[None, Nullable, ApplicationLauncher.Structs.ApplicationEPStruct]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000050C, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000050C, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000050C, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000050C, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000050C, 0x0000FFFD, "uint", 0)
