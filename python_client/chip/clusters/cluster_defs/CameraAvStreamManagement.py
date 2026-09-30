"""CameraAvStreamManagement cluster definition (auto-generated, DO NOT edit)."""

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
class CameraAvStreamManagement(Cluster):
    id: typing.ClassVar[int] = 0x00000551

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="maxConcurrentEncoders", Tag=0x00000000, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="maxEncodedPixelRate", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="videoSensorParams", Tag=0x00000002, Type=typing.Optional[CameraAvStreamManagement.Structs.VideoSensorParamsStruct]),
                ClusterObjectFieldDescriptor(Label="nightVisionUsesInfrared", Tag=0x00000003, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="minViewportResolution", Tag=0x00000004, Type=typing.Optional[CameraAvStreamManagement.Structs.VideoResolutionStruct]),
                ClusterObjectFieldDescriptor(Label="rateDistortionTradeOffPoints", Tag=0x00000005, Type=typing.Optional[typing.List[CameraAvStreamManagement.Structs.RateDistortionTradeOffPointsStruct]]),
                ClusterObjectFieldDescriptor(Label="maxContentBufferSize", Tag=0x00000006, Type=uint),
                ClusterObjectFieldDescriptor(Label="microphoneCapabilities", Tag=0x00000007, Type=typing.Optional[CameraAvStreamManagement.Structs.AudioCapabilitiesStruct]),
                ClusterObjectFieldDescriptor(Label="speakerCapabilities", Tag=0x00000008, Type=typing.Optional[CameraAvStreamManagement.Structs.AudioCapabilitiesStruct]),
                ClusterObjectFieldDescriptor(Label="twoWayTalkSupport", Tag=0x00000009, Type=typing.Optional[CameraAvStreamManagement.Enums.TwoWayTalkSupportTypeEnum]),
                ClusterObjectFieldDescriptor(Label="snapshotCapabilities", Tag=0x0000000A, Type=typing.Optional[typing.List[CameraAvStreamManagement.Structs.SnapshotCapabilitiesStruct]]),
                ClusterObjectFieldDescriptor(Label="maxNetworkBandwidth", Tag=0x0000000B, Type=uint),
                ClusterObjectFieldDescriptor(Label="currentFrameRate", Tag=0x0000000C, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="hdrModeEnabled", Tag=0x0000000D, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="supportedStreamUsages", Tag=0x0000000E, Type=typing.List[Globals.Enums.StreamUsageEnum]),
                ClusterObjectFieldDescriptor(Label="allocatedVideoStreams", Tag=0x0000000F, Type=typing.Optional[typing.List[CameraAvStreamManagement.Structs.VideoStreamStruct]]),
                ClusterObjectFieldDescriptor(Label="allocatedAudioStreams", Tag=0x00000010, Type=typing.Optional[typing.List[CameraAvStreamManagement.Structs.AudioStreamStruct]]),
                ClusterObjectFieldDescriptor(Label="allocatedSnapshotStreams", Tag=0x00000011, Type=typing.Optional[typing.List[CameraAvStreamManagement.Structs.SnapshotStreamStruct]]),
                ClusterObjectFieldDescriptor(Label="streamUsagePriorities", Tag=0x00000012, Type=typing.List[Globals.Enums.StreamUsageEnum]),
                ClusterObjectFieldDescriptor(Label="softRecordingPrivacyModeEnabled", Tag=0x00000013, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="softLivestreamPrivacyModeEnabled", Tag=0x00000014, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="hardPrivacyModeOn", Tag=0x00000015, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="nightVision", Tag=0x00000016, Type=typing.Optional[CameraAvStreamManagement.Enums.TriStateAutoEnum]),
                ClusterObjectFieldDescriptor(Label="nightVisionIllum", Tag=0x00000017, Type=typing.Optional[CameraAvStreamManagement.Enums.TriStateAutoEnum]),
                ClusterObjectFieldDescriptor(Label="viewport", Tag=0x00000018, Type=typing.Optional[Globals.Structs.ViewportStruct]),
                ClusterObjectFieldDescriptor(Label="speakerMuted", Tag=0x00000019, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="speakerVolumeLevel", Tag=0x0000001A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="speakerMaxLevel", Tag=0x0000001B, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="speakerMinLevel", Tag=0x0000001C, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="microphoneMuted", Tag=0x0000001D, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="microphoneVolumeLevel", Tag=0x0000001E, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="microphoneMaxLevel", Tag=0x0000001F, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="microphoneMinLevel", Tag=0x00000020, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="microphoneAgcEnabled", Tag=0x00000021, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="imageRotation", Tag=0x00000022, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="imageFlipHorizontal", Tag=0x00000023, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="imageFlipVertical", Tag=0x00000024, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="localVideoRecordingEnabled", Tag=0x00000025, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="localSnapshotRecordingEnabled", Tag=0x00000026, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="statusLightEnabled", Tag=0x00000027, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="statusLightBrightness", Tag=0x00000028, Type=typing.Optional[Globals.Enums.ThreeLevelAutoEnum]),
                ClusterObjectFieldDescriptor(Label="imageRotationDiscreteAngles", Tag=0x00000029, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    maxConcurrentEncoders: typing.Optional[uint] = None
    maxEncodedPixelRate: typing.Optional[uint] = None
    videoSensorParams: typing.Optional[CameraAvStreamManagement.Structs.VideoSensorParamsStruct] = None
    nightVisionUsesInfrared: typing.Optional[bool] = None
    minViewportResolution: typing.Optional[CameraAvStreamManagement.Structs.VideoResolutionStruct] = None
    rateDistortionTradeOffPoints: typing.Optional[typing.List[CameraAvStreamManagement.Structs.RateDistortionTradeOffPointsStruct]] = None
    maxContentBufferSize: uint = 0
    microphoneCapabilities: typing.Optional[CameraAvStreamManagement.Structs.AudioCapabilitiesStruct] = None
    speakerCapabilities: typing.Optional[CameraAvStreamManagement.Structs.AudioCapabilitiesStruct] = None
    twoWayTalkSupport: typing.Optional[CameraAvStreamManagement.Enums.TwoWayTalkSupportTypeEnum] = None
    snapshotCapabilities: typing.Optional[typing.List[CameraAvStreamManagement.Structs.SnapshotCapabilitiesStruct]] = None
    maxNetworkBandwidth: uint = 0
    currentFrameRate: typing.Optional[uint] = None
    hdrModeEnabled: typing.Optional[bool] = None
    supportedStreamUsages: typing.List[Globals.Enums.StreamUsageEnum] = field(default_factory=lambda: [])
    allocatedVideoStreams: typing.Optional[typing.List[CameraAvStreamManagement.Structs.VideoStreamStruct]] = None
    allocatedAudioStreams: typing.Optional[typing.List[CameraAvStreamManagement.Structs.AudioStreamStruct]] = None
    allocatedSnapshotStreams: typing.Optional[typing.List[CameraAvStreamManagement.Structs.SnapshotStreamStruct]] = None
    streamUsagePriorities: typing.List[Globals.Enums.StreamUsageEnum] = field(default_factory=lambda: [])
    softRecordingPrivacyModeEnabled: typing.Optional[bool] = None
    softLivestreamPrivacyModeEnabled: typing.Optional[bool] = None
    hardPrivacyModeOn: typing.Optional[bool] = None
    nightVision: typing.Optional[CameraAvStreamManagement.Enums.TriStateAutoEnum] = None
    nightVisionIllum: typing.Optional[CameraAvStreamManagement.Enums.TriStateAutoEnum] = None
    viewport: typing.Optional[Globals.Structs.ViewportStruct] = None
    speakerMuted: typing.Optional[bool] = None
    speakerVolumeLevel: typing.Optional[uint] = None
    speakerMaxLevel: typing.Optional[uint] = None
    speakerMinLevel: typing.Optional[uint] = None
    microphoneMuted: typing.Optional[bool] = None
    microphoneVolumeLevel: typing.Optional[uint] = None
    microphoneMaxLevel: typing.Optional[uint] = None
    microphoneMinLevel: typing.Optional[uint] = None
    microphoneAgcEnabled: typing.Optional[bool] = None
    imageRotation: typing.Optional[uint] = None
    imageFlipHorizontal: typing.Optional[bool] = None
    imageFlipVertical: typing.Optional[bool] = None
    localVideoRecordingEnabled: typing.Optional[bool] = None
    localSnapshotRecordingEnabled: typing.Optional[bool] = None
    statusLightEnabled: typing.Optional[bool] = None
    statusLightBrightness: typing.Optional[Globals.Enums.ThreeLevelAutoEnum] = None
    imageRotationDiscreteAngles: typing.Optional[uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class VideoCodecEnum(MatterIntEnum):
            kH264 = 0x00
            kHevc = 0x01
            kVvc = 0x02
            kAv1 = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class AudioCodecEnum(MatterIntEnum):
            kOpus = 0x00
            kAacLc = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class ImageCodecEnum(MatterIntEnum):
            kJpeg = 0x00
            kHeic = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class TwoWayTalkSupportTypeEnum(MatterIntEnum):
            kNotSupported = 0x00
            kHalfDuplex = 0x01
            kFullDuplex = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class TriStateAutoEnum(MatterIntEnum):
            kOff = 0x00
            kOn = 0x01
            kAuto = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

    class Bitmaps:
        class Feature(IntFlag):
            kAudio = 0x1
            kVideo = 0x2
            kSnapshot = 0x4
            kPrivacy = 0x8
            kSpeaker = 0x10
            kImageControl = 0x20
            kWatermark = 0x40
            kOnScreenDisplay = 0x80
            kLocalStorage = 0x100
            kHighDynamicRange = 0x200
            kNightVision = 0x400

    class Structs:
        @dataclass
        class VideoSensorParamsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="sensorWidth", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="sensorHeight", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="maxFps", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="maxHdrfps", Tag=3, Type=typing.Optional[uint]),
                    ])

            sensorWidth: uint = 0
            sensorHeight: uint = 0
            maxFps: uint = 0
            maxHdrfps: typing.Optional[uint] = None

        @dataclass
        class VideoResolutionStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="width", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="height", Tag=1, Type=uint),
                    ])

            width: uint = 0
            height: uint = 0

        @dataclass
        class RateDistortionTradeOffPointsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="codec", Tag=0, Type=CameraAvStreamManagement.Enums.VideoCodecEnum),
                        ClusterObjectFieldDescriptor(Label="resolution", Tag=1, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="minBitRate", Tag=2, Type=uint),
                    ])

            codec: CameraAvStreamManagement.Enums.VideoCodecEnum = 0
            resolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            minBitRate: uint = 0

        @dataclass
        class SnapshotCapabilitiesStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="resolution", Tag=0, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="maxFrameRate", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="imageCodec", Tag=2, Type=CameraAvStreamManagement.Enums.ImageCodecEnum),
                        ClusterObjectFieldDescriptor(Label="requiresEncodedPixels", Tag=3, Type=bool),
                        ClusterObjectFieldDescriptor(Label="requiresHardwareEncoder", Tag=4, Type=typing.Optional[bool]),
                    ])

            resolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            maxFrameRate: uint = 0
            imageCodec: CameraAvStreamManagement.Enums.ImageCodecEnum = 0
            requiresEncodedPixels: bool = False
            requiresHardwareEncoder: typing.Optional[bool] = None

        @dataclass
        class AudioCapabilitiesStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="maxNumberOfChannels", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="supportedCodecs", Tag=1, Type=typing.List[CameraAvStreamManagement.Enums.AudioCodecEnum]),
                        ClusterObjectFieldDescriptor(Label="supportedSampleRates", Tag=2, Type=typing.List[uint]),
                        ClusterObjectFieldDescriptor(Label="supportedBitDepths", Tag=3, Type=typing.List[uint]),
                    ])

            maxNumberOfChannels: uint = 0
            supportedCodecs: typing.List[CameraAvStreamManagement.Enums.AudioCodecEnum] = field(default_factory=lambda: [])
            supportedSampleRates: typing.List[uint] = field(default_factory=lambda: [])
            supportedBitDepths: typing.List[uint] = field(default_factory=lambda: [])

        @dataclass
        class VideoStreamStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="videoStreamID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="streamUsage", Tag=1, Type=Globals.Enums.StreamUsageEnum),
                        ClusterObjectFieldDescriptor(Label="videoCodec", Tag=2, Type=CameraAvStreamManagement.Enums.VideoCodecEnum),
                        ClusterObjectFieldDescriptor(Label="minFrameRate", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="maxFrameRate", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="minResolution", Tag=5, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="maxResolution", Tag=6, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="minBitRate", Tag=7, Type=uint),
                        ClusterObjectFieldDescriptor(Label="maxBitRate", Tag=8, Type=uint),
                        ClusterObjectFieldDescriptor(Label="keyFrameInterval", Tag=9, Type=uint),
                        ClusterObjectFieldDescriptor(Label="watermarkEnabled", Tag=10, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="osdEnabled", Tag=11, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="referenceCount", Tag=12, Type=uint),
                    ])

            videoStreamID: uint = 0
            streamUsage: Globals.Enums.StreamUsageEnum = 0
            videoCodec: CameraAvStreamManagement.Enums.VideoCodecEnum = 0
            minFrameRate: uint = 0
            maxFrameRate: uint = 0
            minResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            maxResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            minBitRate: uint = 0
            maxBitRate: uint = 0
            keyFrameInterval: uint = 0
            watermarkEnabled: typing.Optional[bool] = None
            osdEnabled: typing.Optional[bool] = None
            referenceCount: uint = 0

        @dataclass
        class AudioStreamStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="audioStreamID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="streamUsage", Tag=1, Type=Globals.Enums.StreamUsageEnum),
                        ClusterObjectFieldDescriptor(Label="audioCodec", Tag=2, Type=CameraAvStreamManagement.Enums.AudioCodecEnum),
                        ClusterObjectFieldDescriptor(Label="channelCount", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="sampleRate", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="bitRate", Tag=5, Type=uint),
                        ClusterObjectFieldDescriptor(Label="bitDepth", Tag=6, Type=uint),
                        ClusterObjectFieldDescriptor(Label="referenceCount", Tag=7, Type=uint),
                    ])

            audioStreamID: uint = 0
            streamUsage: Globals.Enums.StreamUsageEnum = 0
            audioCodec: CameraAvStreamManagement.Enums.AudioCodecEnum = 0
            channelCount: uint = 0
            sampleRate: uint = 0
            bitRate: uint = 0
            bitDepth: uint = 0
            referenceCount: uint = 0

        @dataclass
        class SnapshotStreamStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="snapshotStreamID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="imageCodec", Tag=1, Type=CameraAvStreamManagement.Enums.ImageCodecEnum),
                        ClusterObjectFieldDescriptor(Label="frameRate", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="minResolution", Tag=3, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="maxResolution", Tag=4, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="quality", Tag=5, Type=uint),
                        ClusterObjectFieldDescriptor(Label="referenceCount", Tag=6, Type=uint),
                        ClusterObjectFieldDescriptor(Label="encodedPixels", Tag=7, Type=bool),
                        ClusterObjectFieldDescriptor(Label="hardwareEncoder", Tag=8, Type=bool),
                        ClusterObjectFieldDescriptor(Label="watermarkEnabled", Tag=9, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="osdEnabled", Tag=10, Type=typing.Optional[bool]),
                    ])

            snapshotStreamID: uint = 0
            imageCodec: CameraAvStreamManagement.Enums.ImageCodecEnum = 0
            frameRate: uint = 0
            minResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            maxResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            quality: uint = 0
            referenceCount: uint = 0
            encodedPixels: bool = False
            hardwareEncoder: bool = False
            watermarkEnabled: typing.Optional[bool] = None
            osdEnabled: typing.Optional[bool] = None

        @dataclass
        class AVMetadataStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="UTCTime", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="motionZonesActive", Tag=2, Type=typing.Optional[typing.List[uint]]),
                        ClusterObjectFieldDescriptor(Label="blackAndWhiteActive", Tag=3, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="userDefined", Tag=4, Type=typing.Optional[bytes]),
                    ])

            UTCTime: typing.Union[Nullable, uint] = NullValue
            motionZonesActive: typing.Optional[typing.List[uint]] = None
            blackAndWhiteActive: typing.Optional[bool] = None
            userDefined: typing.Optional[bytes] = None

    class Commands:
        @dataclass
        class AudioStreamAllocate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'AudioStreamAllocateResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="streamUsage", Tag=0, Type=Globals.Enums.StreamUsageEnum),
                        ClusterObjectFieldDescriptor(Label="audioCodec", Tag=1, Type=CameraAvStreamManagement.Enums.AudioCodecEnum),
                        ClusterObjectFieldDescriptor(Label="channelCount", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="sampleRate", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="bitRate", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="bitDepth", Tag=5, Type=uint),
                    ])

            streamUsage: Globals.Enums.StreamUsageEnum = 0
            audioCodec: CameraAvStreamManagement.Enums.AudioCodecEnum = 0
            channelCount: uint = 0
            sampleRate: uint = 0
            bitRate: uint = 0
            bitDepth: uint = 0

        @dataclass
        class AudioStreamDeallocate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="audioStreamID", Tag=0, Type=uint),
                    ])

            audioStreamID: uint = 0

        @dataclass
        class VideoStreamAllocate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'VideoStreamAllocateResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="streamUsage", Tag=0, Type=Globals.Enums.StreamUsageEnum),
                        ClusterObjectFieldDescriptor(Label="videoCodec", Tag=1, Type=CameraAvStreamManagement.Enums.VideoCodecEnum),
                        ClusterObjectFieldDescriptor(Label="minFrameRate", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="maxFrameRate", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="minResolution", Tag=4, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="maxResolution", Tag=5, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="minBitRate", Tag=6, Type=uint),
                        ClusterObjectFieldDescriptor(Label="maxBitRate", Tag=7, Type=uint),
                        ClusterObjectFieldDescriptor(Label="keyFrameInterval", Tag=8, Type=uint),
                        ClusterObjectFieldDescriptor(Label="watermarkEnabled", Tag=9, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="osdEnabled", Tag=10, Type=typing.Optional[bool]),
                    ])

            streamUsage: Globals.Enums.StreamUsageEnum = 0
            videoCodec: CameraAvStreamManagement.Enums.VideoCodecEnum = 0
            minFrameRate: uint = 0
            maxFrameRate: uint = 0
            minResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            maxResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            minBitRate: uint = 0
            maxBitRate: uint = 0
            keyFrameInterval: uint = 0
            watermarkEnabled: typing.Optional[bool] = None
            osdEnabled: typing.Optional[bool] = None

        @dataclass
        class VideoStreamModify(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="videoStreamID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="watermarkEnabled", Tag=1, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="osdEnabled", Tag=2, Type=typing.Optional[bool]),
                    ])

            videoStreamID: uint = 0
            watermarkEnabled: typing.Optional[bool] = None
            osdEnabled: typing.Optional[bool] = None

        @dataclass
        class VideoStreamDeallocate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="videoStreamID", Tag=0, Type=uint),
                    ])

            videoStreamID: uint = 0

        @dataclass
        class SnapshotStreamAllocate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'SnapshotStreamAllocateResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="imageCodec", Tag=0, Type=CameraAvStreamManagement.Enums.ImageCodecEnum),
                        ClusterObjectFieldDescriptor(Label="maxFrameRate", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="minResolution", Tag=2, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="maxResolution", Tag=3, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                        ClusterObjectFieldDescriptor(Label="quality", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="watermarkEnabled", Tag=5, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="osdEnabled", Tag=6, Type=typing.Optional[bool]),
                    ])

            imageCodec: CameraAvStreamManagement.Enums.ImageCodecEnum = 0
            maxFrameRate: uint = 0
            minResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            maxResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())
            quality: uint = 0
            watermarkEnabled: typing.Optional[bool] = None
            osdEnabled: typing.Optional[bool] = None

        @dataclass
        class SnapshotStreamModify(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000009
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="snapshotStreamID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="watermarkEnabled", Tag=1, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="osdEnabled", Tag=2, Type=typing.Optional[bool]),
                    ])

            snapshotStreamID: uint = 0
            watermarkEnabled: typing.Optional[bool] = None
            osdEnabled: typing.Optional[bool] = None

        @dataclass
        class SnapshotStreamDeallocate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x0000000A
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="snapshotStreamID", Tag=0, Type=uint),
                    ])

            snapshotStreamID: uint = 0

        @dataclass
        class SetStreamPriorities(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x0000000B
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="streamPriorities", Tag=0, Type=typing.List[Globals.Enums.StreamUsageEnum]),
                    ])

            streamPriorities: typing.List[Globals.Enums.StreamUsageEnum] = field(default_factory=lambda: [])

        @dataclass
        class CaptureSnapshot(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x0000000C
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'CaptureSnapshotResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="snapshotStreamID", Tag=0, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="requestedResolution", Tag=1, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                    ])

            snapshotStreamID: typing.Union[Nullable, uint] = NullValue
            requestedResolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())

        @dataclass
        class AudioStreamAllocateResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="audioStreamID", Tag=0, Type=uint),
                    ])

            audioStreamID: uint = 0

        @dataclass
        class VideoStreamAllocateResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="videoStreamID", Tag=0, Type=uint),
                    ])

            videoStreamID: uint = 0

        @dataclass
        class SnapshotStreamAllocateResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x00000008
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="snapshotStreamID", Tag=0, Type=uint),
                    ])

            snapshotStreamID: uint = 0

        @dataclass
        class CaptureSnapshotResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000551
            command_id: typing.ClassVar[int] = 0x0000000D
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="data", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="imageCodec", Tag=1, Type=CameraAvStreamManagement.Enums.ImageCodecEnum),
                        ClusterObjectFieldDescriptor(Label="resolution", Tag=2, Type=CameraAvStreamManagement.Structs.VideoResolutionStruct),
                    ])

            data: bytes = b""
            imageCodec: CameraAvStreamManagement.Enums.ImageCodecEnum = 0
            resolution: CameraAvStreamManagement.Structs.VideoResolutionStruct = field(default_factory=lambda: CameraAvStreamManagement.Structs.VideoResolutionStruct())

    class Attributes:
        MaxConcurrentEncoders = _attr(__module__, __qualname__, "MaxConcurrentEncoders", 0x00000551, 0x00000000, "typing.Optional[uint]", None)

        MaxEncodedPixelRate = _attr(__module__, __qualname__, "MaxEncodedPixelRate", 0x00000551, 0x00000001, "typing.Optional[uint]", None)

        VideoSensorParams = _attr(__module__, __qualname__, "VideoSensorParams", 0x00000551, 0x00000002, "typing.Optional[CameraAvStreamManagement.Structs.VideoSensorParamsStruct]", None)

        NightVisionUsesInfrared = _attr(__module__, __qualname__, "NightVisionUsesInfrared", 0x00000551, 0x00000003, "typing.Optional[bool]", None)

        MinViewportResolution = _attr(__module__, __qualname__, "MinViewportResolution", 0x00000551, 0x00000004, "typing.Optional[CameraAvStreamManagement.Structs.VideoResolutionStruct]", None)

        RateDistortionTradeOffPoints = _attr(__module__, __qualname__, "RateDistortionTradeOffPoints", 0x00000551, 0x00000005, "typing.Optional[typing.List[CameraAvStreamManagement.Structs.RateDistortionTradeOffPointsStruct]]", None)

        MaxContentBufferSize = _attr(__module__, __qualname__, "MaxContentBufferSize", 0x00000551, 0x00000006, "uint", 0)

        MicrophoneCapabilities = _attr(__module__, __qualname__, "MicrophoneCapabilities", 0x00000551, 0x00000007, "typing.Optional[CameraAvStreamManagement.Structs.AudioCapabilitiesStruct]", None)

        SpeakerCapabilities = _attr(__module__, __qualname__, "SpeakerCapabilities", 0x00000551, 0x00000008, "typing.Optional[CameraAvStreamManagement.Structs.AudioCapabilitiesStruct]", None)

        TwoWayTalkSupport = _attr(__module__, __qualname__, "TwoWayTalkSupport", 0x00000551, 0x00000009, "typing.Optional[CameraAvStreamManagement.Enums.TwoWayTalkSupportTypeEnum]", None)

        SnapshotCapabilities = _attr(__module__, __qualname__, "SnapshotCapabilities", 0x00000551, 0x0000000A, "typing.Optional[typing.List[CameraAvStreamManagement.Structs.SnapshotCapabilitiesStruct]]", None)

        MaxNetworkBandwidth = _attr(__module__, __qualname__, "MaxNetworkBandwidth", 0x00000551, 0x0000000B, "uint", 0)

        CurrentFrameRate = _attr(__module__, __qualname__, "CurrentFrameRate", 0x00000551, 0x0000000C, "typing.Optional[uint]", None)

        HdrModeEnabled = _attr(__module__, __qualname__, "HdrModeEnabled", 0x00000551, 0x0000000D, "typing.Optional[bool]", None)

        SupportedStreamUsages = _attr(__module__, __qualname__, "SupportedStreamUsages", 0x00000551, 0x0000000E, "typing.List[Globals.Enums.StreamUsageEnum]", None, "[]")

        AllocatedVideoStreams = _attr(__module__, __qualname__, "AllocatedVideoStreams", 0x00000551, 0x0000000F, "typing.Optional[typing.List[CameraAvStreamManagement.Structs.VideoStreamStruct]]", None)

        AllocatedAudioStreams = _attr(__module__, __qualname__, "AllocatedAudioStreams", 0x00000551, 0x00000010, "typing.Optional[typing.List[CameraAvStreamManagement.Structs.AudioStreamStruct]]", None)

        AllocatedSnapshotStreams = _attr(__module__, __qualname__, "AllocatedSnapshotStreams", 0x00000551, 0x00000011, "typing.Optional[typing.List[CameraAvStreamManagement.Structs.SnapshotStreamStruct]]", None)

        StreamUsagePriorities = _attr(__module__, __qualname__, "StreamUsagePriorities", 0x00000551, 0x00000012, "typing.List[Globals.Enums.StreamUsageEnum]", None, "[]")

        SoftRecordingPrivacyModeEnabled = _attr(__module__, __qualname__, "SoftRecordingPrivacyModeEnabled", 0x00000551, 0x00000013, "typing.Optional[bool]", None)

        SoftLivestreamPrivacyModeEnabled = _attr(__module__, __qualname__, "SoftLivestreamPrivacyModeEnabled", 0x00000551, 0x00000014, "typing.Optional[bool]", None)

        HardPrivacyModeOn = _attr(__module__, __qualname__, "HardPrivacyModeOn", 0x00000551, 0x00000015, "typing.Optional[bool]", None)

        NightVision = _attr(__module__, __qualname__, "NightVision", 0x00000551, 0x00000016, "typing.Optional[CameraAvStreamManagement.Enums.TriStateAutoEnum]", None)

        NightVisionIllum = _attr(__module__, __qualname__, "NightVisionIllum", 0x00000551, 0x00000017, "typing.Optional[CameraAvStreamManagement.Enums.TriStateAutoEnum]", None)

        Viewport = _attr(__module__, __qualname__, "Viewport", 0x00000551, 0x00000018, "typing.Optional[Globals.Structs.ViewportStruct]", None)

        SpeakerMuted = _attr(__module__, __qualname__, "SpeakerMuted", 0x00000551, 0x00000019, "typing.Optional[bool]", None)

        SpeakerVolumeLevel = _attr(__module__, __qualname__, "SpeakerVolumeLevel", 0x00000551, 0x0000001A, "typing.Optional[uint]", None)

        SpeakerMaxLevel = _attr(__module__, __qualname__, "SpeakerMaxLevel", 0x00000551, 0x0000001B, "typing.Optional[uint]", None)

        SpeakerMinLevel = _attr(__module__, __qualname__, "SpeakerMinLevel", 0x00000551, 0x0000001C, "typing.Optional[uint]", None)

        MicrophoneMuted = _attr(__module__, __qualname__, "MicrophoneMuted", 0x00000551, 0x0000001D, "typing.Optional[bool]", None)

        MicrophoneVolumeLevel = _attr(__module__, __qualname__, "MicrophoneVolumeLevel", 0x00000551, 0x0000001E, "typing.Optional[uint]", None)

        MicrophoneMaxLevel = _attr(__module__, __qualname__, "MicrophoneMaxLevel", 0x00000551, 0x0000001F, "typing.Optional[uint]", None)

        MicrophoneMinLevel = _attr(__module__, __qualname__, "MicrophoneMinLevel", 0x00000551, 0x00000020, "typing.Optional[uint]", None)

        MicrophoneAgcEnabled = _attr(__module__, __qualname__, "MicrophoneAgcEnabled", 0x00000551, 0x00000021, "typing.Optional[bool]", None)

        ImageRotation = _attr(__module__, __qualname__, "ImageRotation", 0x00000551, 0x00000022, "typing.Optional[uint]", None)

        ImageFlipHorizontal = _attr(__module__, __qualname__, "ImageFlipHorizontal", 0x00000551, 0x00000023, "typing.Optional[bool]", None)

        ImageFlipVertical = _attr(__module__, __qualname__, "ImageFlipVertical", 0x00000551, 0x00000024, "typing.Optional[bool]", None)

        LocalVideoRecordingEnabled = _attr(__module__, __qualname__, "LocalVideoRecordingEnabled", 0x00000551, 0x00000025, "typing.Optional[bool]", None)

        LocalSnapshotRecordingEnabled = _attr(__module__, __qualname__, "LocalSnapshotRecordingEnabled", 0x00000551, 0x00000026, "typing.Optional[bool]", None)

        StatusLightEnabled = _attr(__module__, __qualname__, "StatusLightEnabled", 0x00000551, 0x00000027, "typing.Optional[bool]", None)

        StatusLightBrightness = _attr(__module__, __qualname__, "StatusLightBrightness", 0x00000551, 0x00000028, "typing.Optional[Globals.Enums.ThreeLevelAutoEnum]", None)

        ImageRotationDiscreteAngles = _attr(__module__, __qualname__, "ImageRotationDiscreteAngles", 0x00000551, 0x00000029, "typing.Optional[uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000551, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000551, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000551, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000551, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000551, 0x0000FFFD, "uint", 0)
