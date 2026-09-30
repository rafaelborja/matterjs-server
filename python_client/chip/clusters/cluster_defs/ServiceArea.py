"""ServiceArea cluster definition (auto-generated, DO NOT edit)."""

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
class ServiceArea(Cluster):
    id: typing.ClassVar[int] = 0x00000150

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="supportedAreas", Tag=0x00000000, Type=typing.List[ServiceArea.Structs.AreaStruct]),
                ClusterObjectFieldDescriptor(Label="supportedMaps", Tag=0x00000001, Type=typing.Optional[typing.List[ServiceArea.Structs.MapStruct]]),
                ClusterObjectFieldDescriptor(Label="selectedAreas", Tag=0x00000002, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="currentArea", Tag=0x00000003, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="estimatedEndTime", Tag=0x00000004, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="progress", Tag=0x00000005, Type=typing.Optional[typing.List[ServiceArea.Structs.ProgressStruct]]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    supportedAreas: typing.List[ServiceArea.Structs.AreaStruct] = field(default_factory=lambda: [])
    supportedMaps: typing.Optional[typing.List[ServiceArea.Structs.MapStruct]] = None
    selectedAreas: typing.List[uint] = field(default_factory=lambda: [])
    currentArea: typing.Union[None, Nullable, uint] = None
    estimatedEndTime: typing.Union[None, Nullable, uint] = None
    progress: typing.Optional[typing.List[ServiceArea.Structs.ProgressStruct]] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class OperationalStatusEnum(MatterIntEnum):
            kPending = 0x00
            kOperating = 0x01
            kSkipped = 0x02
            kCompleted = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class SelectAreasStatus(MatterIntEnum):
            kSuccess = 0x00
            kUnsupportedArea = 0x01
            kInvalidInMode = 0x02
            kInvalidSet = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class SkipAreaStatus(MatterIntEnum):
            kSuccess = 0x00
            kInvalidAreaList = 0x01
            kInvalidInMode = 0x02
            kInvalidSkippedArea = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Bitmaps:
        class Feature(IntFlag):
            kSelectWhileRunning = 0x1
            kProgressReporting = 0x2
            kMaps = 0x4

    class Structs:
        @dataclass
        class LandmarkInfoStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="landmarkTag", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="relativePositionTag", Tag=1, Type=typing.Union[Nullable, uint]),
                    ])

            landmarkTag: uint = 0
            relativePositionTag: typing.Union[Nullable, uint] = NullValue

        @dataclass
        class AreaInfoStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="locationInfo", Tag=0, Type=typing.Union[Nullable, Globals.Structs.locationdesc]),
                        ClusterObjectFieldDescriptor(Label="landmarkInfo", Tag=1, Type=typing.Union[Nullable, ServiceArea.Structs.LandmarkInfoStruct]),
                    ])

            locationInfo: typing.Union[Nullable, Globals.Structs.locationdesc] = NullValue
            landmarkInfo: typing.Union[Nullable, ServiceArea.Structs.LandmarkInfoStruct] = NullValue

        @dataclass
        class MapStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="mapID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="name", Tag=1, Type=str),
                    ])

            mapID: uint = 0
            name: str = ""

        @dataclass
        class AreaStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="areaID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="mapID", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="areaInfo", Tag=2, Type=ServiceArea.Structs.AreaInfoStruct),
                    ])

            areaID: uint = 0
            mapID: typing.Union[Nullable, uint] = NullValue
            areaInfo: ServiceArea.Structs.AreaInfoStruct = field(default_factory=lambda: ServiceArea.Structs.AreaInfoStruct())

        @dataclass
        class ProgressStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="areaID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="status", Tag=1, Type=ServiceArea.Enums.OperationalStatusEnum),
                        ClusterObjectFieldDescriptor(Label="totalOperationalTime", Tag=2, Type=typing.Union[None, Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="estimatedTime", Tag=3, Type=typing.Union[None, Nullable, uint]),
                    ])

            areaID: uint = 0
            status: ServiceArea.Enums.OperationalStatusEnum = 0
            totalOperationalTime: typing.Union[None, Nullable, uint] = None
            estimatedTime: typing.Union[None, Nullable, uint] = None

    class Commands:
        @dataclass
        class SelectAreas(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000150
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'SelectAreasResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="newAreas", Tag=0, Type=typing.List[uint]),
                    ])

            newAreas: typing.List[uint] = field(default_factory=lambda: [])

        @dataclass
        class SkipArea(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000150
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'SkipAreaResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="skippedArea", Tag=0, Type=uint),
                    ])

            skippedArea: uint = 0

        @dataclass
        class SelectAreasResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000150
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="status", Tag=0, Type=ServiceArea.Enums.SelectAreasStatus),
                        ClusterObjectFieldDescriptor(Label="statusText", Tag=1, Type=str),
                    ])

            status: ServiceArea.Enums.SelectAreasStatus = 0
            statusText: str = ""

        @dataclass
        class SkipAreaResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000150
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="status", Tag=0, Type=ServiceArea.Enums.SkipAreaStatus),
                        ClusterObjectFieldDescriptor(Label="statusText", Tag=1, Type=str),
                    ])

            status: ServiceArea.Enums.SkipAreaStatus = 0
            statusText: str = ""

    class Attributes:
        SupportedAreas = _attr(__module__, __qualname__, "SupportedAreas", 0x00000150, 0x00000000, "typing.List[ServiceArea.Structs.AreaStruct]", None, "[]")

        SupportedMaps = _attr(__module__, __qualname__, "SupportedMaps", 0x00000150, 0x00000001, "typing.Optional[typing.List[ServiceArea.Structs.MapStruct]]", None)

        SelectedAreas = _attr(__module__, __qualname__, "SelectedAreas", 0x00000150, 0x00000002, "typing.List[uint]", None, "[]")

        CurrentArea = _attr(__module__, __qualname__, "CurrentArea", 0x00000150, 0x00000003, "typing.Union[None, Nullable, uint]", None)

        EstimatedEndTime = _attr(__module__, __qualname__, "EstimatedEndTime", 0x00000150, 0x00000004, "typing.Union[None, Nullable, uint]", None)

        Progress = _attr(__module__, __qualname__, "Progress", 0x00000150, 0x00000005, "typing.Optional[typing.List[ServiceArea.Structs.ProgressStruct]]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000150, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000150, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000150, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000150, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000150, 0x0000FFFD, "uint", 0)
