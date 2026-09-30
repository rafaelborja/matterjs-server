"""ColorControl cluster definition (auto-generated, DO NOT edit)."""

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
class ColorControl(Cluster):
    id: typing.ClassVar[int] = 0x00000300

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="currentHue", Tag=0x00000000, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentSaturation", Tag=0x00000001, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="remainingTime", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentX", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="currentY", Tag=0x00000004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="driftCompensation", Tag=0x00000005, Type=typing.Optional[ColorControl.Enums.DriftCompensationEnum]),
                ClusterObjectFieldDescriptor(Label="compensationText", Tag=0x00000006, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="colorTemperatureMireds", Tag=0x00000007, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorMode", Tag=0x00000008, Type=ColorControl.Enums.ColorModeEnum),
                ClusterObjectFieldDescriptor(Label="options", Tag=0x0000000F, Type=ColorControl.Bitmaps.OptionsBitmap),
                ClusterObjectFieldDescriptor(Label="numberOfPrimaries", Tag=0x00000010, Type=typing.Union[Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="primary1X", Tag=0x00000011, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary1Y", Tag=0x00000012, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary1Intensity", Tag=0x00000013, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="primary2X", Tag=0x00000015, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary2Y", Tag=0x00000016, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary2Intensity", Tag=0x00000017, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="primary3X", Tag=0x00000019, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary3Y", Tag=0x0000001A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary3Intensity", Tag=0x0000001B, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="primary4X", Tag=0x00000020, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary4Y", Tag=0x00000021, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary4Intensity", Tag=0x00000022, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="primary5X", Tag=0x00000024, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary5Y", Tag=0x00000025, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary5Intensity", Tag=0x00000026, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="primary6X", Tag=0x00000028, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary6Y", Tag=0x00000029, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="primary6Intensity", Tag=0x0000002A, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="whitePointX", Tag=0x00000030, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="whitePointY", Tag=0x00000031, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointRX", Tag=0x00000032, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointRY", Tag=0x00000033, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointRIntensity", Tag=0x00000034, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="colorPointGX", Tag=0x00000036, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointGY", Tag=0x00000037, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointGIntensity", Tag=0x00000038, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="colorPointBX", Tag=0x0000003A, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointBY", Tag=0x0000003B, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorPointBIntensity", Tag=0x0000003C, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="enhancedCurrentHue", Tag=0x00004000, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="enhancedColorMode", Tag=0x00004001, Type=ColorControl.Enums.EnhancedColorModeEnum),
                ClusterObjectFieldDescriptor(Label="colorLoopActive", Tag=0x00004002, Type=typing.Optional[Globals.Enums.enum8]),
                ClusterObjectFieldDescriptor(Label="colorLoopDirection", Tag=0x00004003, Type=typing.Optional[ColorControl.Enums.ColorLoopDirectionEnum]),
                ClusterObjectFieldDescriptor(Label="colorLoopTime", Tag=0x00004004, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorLoopStartEnhancedHue", Tag=0x00004005, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorLoopStoredEnhancedHue", Tag=0x00004006, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorCapabilities", Tag=0x0000400A, Type=ColorControl.Bitmaps.ColorCapabilitiesBitmap),
                ClusterObjectFieldDescriptor(Label="colorTempPhysicalMinMireds", Tag=0x0000400B, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="colorTempPhysicalMaxMireds", Tag=0x0000400C, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="coupleColorTempToLevelMinMireds", Tag=0x0000400D, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="startUpColorTemperatureMireds", Tag=0x00004010, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    currentHue: typing.Optional[uint] = None
    currentSaturation: typing.Optional[uint] = None
    remainingTime: typing.Optional[uint] = None
    currentX: typing.Optional[uint] = None
    currentY: typing.Optional[uint] = None
    driftCompensation: typing.Optional[ColorControl.Enums.DriftCompensationEnum] = None
    compensationText: typing.Optional[str] = None
    colorTemperatureMireds: typing.Optional[uint] = None
    colorMode: ColorControl.Enums.ColorModeEnum = 0
    options: ColorControl.Bitmaps.OptionsBitmap = 0
    numberOfPrimaries: typing.Union[Nullable, uint] = NullValue
    primary1X: typing.Optional[uint] = None
    primary1Y: typing.Optional[uint] = None
    primary1Intensity: typing.Union[None, Nullable, uint] = None
    primary2X: typing.Optional[uint] = None
    primary2Y: typing.Optional[uint] = None
    primary2Intensity: typing.Union[None, Nullable, uint] = None
    primary3X: typing.Optional[uint] = None
    primary3Y: typing.Optional[uint] = None
    primary3Intensity: typing.Union[None, Nullable, uint] = None
    primary4X: typing.Optional[uint] = None
    primary4Y: typing.Optional[uint] = None
    primary4Intensity: typing.Union[None, Nullable, uint] = None
    primary5X: typing.Optional[uint] = None
    primary5Y: typing.Optional[uint] = None
    primary5Intensity: typing.Union[None, Nullable, uint] = None
    primary6X: typing.Optional[uint] = None
    primary6Y: typing.Optional[uint] = None
    primary6Intensity: typing.Union[None, Nullable, uint] = None
    whitePointX: typing.Optional[uint] = None
    whitePointY: typing.Optional[uint] = None
    colorPointRX: typing.Optional[uint] = None
    colorPointRY: typing.Optional[uint] = None
    colorPointRIntensity: typing.Union[None, Nullable, uint] = None
    colorPointGX: typing.Optional[uint] = None
    colorPointGY: typing.Optional[uint] = None
    colorPointGIntensity: typing.Union[None, Nullable, uint] = None
    colorPointBX: typing.Optional[uint] = None
    colorPointBY: typing.Optional[uint] = None
    colorPointBIntensity: typing.Union[None, Nullable, uint] = None
    enhancedCurrentHue: typing.Optional[uint] = None
    enhancedColorMode: ColorControl.Enums.EnhancedColorModeEnum = 0
    colorLoopActive: typing.Optional[Globals.Enums.enum8] = None
    colorLoopDirection: typing.Optional[ColorControl.Enums.ColorLoopDirectionEnum] = None
    colorLoopTime: typing.Optional[uint] = None
    colorLoopStartEnhancedHue: typing.Optional[uint] = None
    colorLoopStoredEnhancedHue: typing.Optional[uint] = None
    colorCapabilities: ColorControl.Bitmaps.ColorCapabilitiesBitmap = 0
    colorTempPhysicalMinMireds: typing.Optional[uint] = None
    colorTempPhysicalMaxMireds: typing.Optional[uint] = None
    coupleColorTempToLevelMinMireds: typing.Optional[uint] = None
    startUpColorTemperatureMireds: typing.Union[None, Nullable, uint] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class DriftCompensationEnum(MatterIntEnum):
            kNone = 0x00
            kOtherOrUnknown = 0x01
            kTemperatureMonitoring = 0x02
            kOpticalLuminanceMonitoringAndFeedback = 0x03
            kOpticalColorMonitoringAndFeedback = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

        class ColorModeEnum(MatterIntEnum):
            kCurrentHueAndCurrentSaturation = 0x00
            kCurrentXAndCurrentY = 0x01
            kColorTemperatureMireds = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class EnhancedColorModeEnum(MatterIntEnum):
            kCurrentHueAndCurrentSaturation = 0x00
            kCurrentXAndCurrentY = 0x01
            kColorTemperatureMireds = 0x02
            kEnhancedCurrentHueAndCurrentSaturation = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class DirectionEnum(MatterIntEnum):
            kShortest = 0x00
            kLongest = 0x01
            kUp = 0x02
            kDown = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class MoveModeEnum(MatterIntEnum):
            kStop = 0x00
            kUp = 0x01
            kDown = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class StepModeEnum(MatterIntEnum):
            kUp = 0x01
            kDown = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class ColorLoopActionEnum(MatterIntEnum):
            kDeactivate = 0x00
            kActivateFromColorLoopStartEnhancedHue = 0x01
            kActivateFromEnhancedCurrentHue = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class ColorLoopDirectionEnum(MatterIntEnum):
            kDecrement = 0x00
            kIncrement = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Bitmaps:
        class Feature(IntFlag):
            kHueAndSaturation = 0x1
            kEnhancedHue = 0x2
            kColorLoop = 0x4
            kXy = 0x8
            kColorTemperature = 0x10

        class OptionsBitmap(IntFlag):
            kExecuteIfOff = 0x1

        class UpdateFlagsBitmap(IntFlag):
            kUpdateAction = 0x1
            kUpdateDirection = 0x2
            kUpdateTime = 0x4
            kUpdateStartHue = 0x8

        class ColorCapabilitiesBitmap(IntFlag):
            kHueSaturation = 0x1
            kEnhancedHue = 0x2
            kColorLoop = 0x4
            kXy = 0x8
            kColorTemperature = 0x10

    class Commands:
        @dataclass
        class MoveToHue(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="hue", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="direction", Tag=1, Type=ColorControl.Enums.DirectionEnum),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            hue: uint = 0
            direction: ColorControl.Enums.DirectionEnum = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveHue(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="moveMode", Tag=0, Type=ColorControl.Enums.MoveModeEnum),
                        ClusterObjectFieldDescriptor(Label="rate", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            moveMode: ColorControl.Enums.MoveModeEnum = 0
            rate: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StepHue(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepMode", Tag=0, Type=ColorControl.Enums.StepModeEnum),
                        ClusterObjectFieldDescriptor(Label="stepSize", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            stepMode: ColorControl.Enums.StepModeEnum = 0
            stepSize: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveToSaturation(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="saturation", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            saturation: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveSaturation(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="moveMode", Tag=0, Type=ColorControl.Enums.MoveModeEnum),
                        ClusterObjectFieldDescriptor(Label="rate", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            moveMode: ColorControl.Enums.MoveModeEnum = 0
            rate: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StepSaturation(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepMode", Tag=0, Type=ColorControl.Enums.StepModeEnum),
                        ClusterObjectFieldDescriptor(Label="stepSize", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            stepMode: ColorControl.Enums.StepModeEnum = 0
            stepSize: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveToHueAndSaturation(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="hue", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="saturation", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            hue: uint = 0
            saturation: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveToColor(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="colorX", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="colorY", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            colorX: uint = 0
            colorY: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveColor(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000008
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="rateX", Tag=0, Type=int),
                        ClusterObjectFieldDescriptor(Label="rateY", Tag=1, Type=int),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            rateX: int = 0
            rateY: int = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StepColor(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000009
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepX", Tag=0, Type=int),
                        ClusterObjectFieldDescriptor(Label="stepY", Tag=1, Type=int),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            stepX: int = 0
            stepY: int = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveToColorTemperature(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x0000000A
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="colorTemperatureMireds", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            colorTemperatureMireds: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class EnhancedMoveToHue(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000040
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="enhancedHue", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="direction", Tag=1, Type=ColorControl.Enums.DirectionEnum),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            enhancedHue: uint = 0
            direction: ColorControl.Enums.DirectionEnum = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class EnhancedMoveHue(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000041
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="moveMode", Tag=0, Type=ColorControl.Enums.MoveModeEnum),
                        ClusterObjectFieldDescriptor(Label="rate", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=2, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            moveMode: ColorControl.Enums.MoveModeEnum = 0
            rate: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class EnhancedStepHue(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000042
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepMode", Tag=0, Type=ColorControl.Enums.StepModeEnum),
                        ClusterObjectFieldDescriptor(Label="stepSize", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            stepMode: ColorControl.Enums.StepModeEnum = 0
            stepSize: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class EnhancedMoveToHueAndSaturation(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000043
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="enhancedHue", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="saturation", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=3, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            enhancedHue: uint = 0
            saturation: uint = 0
            transitionTime: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class ColorLoopSet(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000044
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="updateFlags", Tag=0, Type=ColorControl.Bitmaps.UpdateFlagsBitmap),
                        ClusterObjectFieldDescriptor(Label="action", Tag=1, Type=ColorControl.Enums.ColorLoopActionEnum),
                        ClusterObjectFieldDescriptor(Label="direction", Tag=2, Type=ColorControl.Enums.ColorLoopDirectionEnum),
                        ClusterObjectFieldDescriptor(Label="time", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="startHue", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=5, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=6, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            updateFlags: ColorControl.Bitmaps.UpdateFlagsBitmap = 0
            action: ColorControl.Enums.ColorLoopActionEnum = 0
            direction: ColorControl.Enums.ColorLoopDirectionEnum = 0
            time: uint = 0
            startHue: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StopMoveStep(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x00000047
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=0, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=1, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class MoveColorTemperature(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x0000004B
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="moveMode", Tag=0, Type=ColorControl.Enums.MoveModeEnum),
                        ClusterObjectFieldDescriptor(Label="rate", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="colorTemperatureMinimumMireds", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="colorTemperatureMaximumMireds", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=4, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=5, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            moveMode: ColorControl.Enums.MoveModeEnum = 0
            rate: uint = 0
            colorTemperatureMinimumMireds: uint = 0
            colorTemperatureMaximumMireds: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

        @dataclass
        class StepColorTemperature(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000300
            command_id: typing.ClassVar[int] = 0x0000004C
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="stepMode", Tag=0, Type=ColorControl.Enums.StepModeEnum),
                        ClusterObjectFieldDescriptor(Label="stepSize", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="transitionTime", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="colorTemperatureMinimumMireds", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="colorTemperatureMaximumMireds", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="optionsMask", Tag=5, Type=ColorControl.Bitmaps.OptionsBitmap),
                        ClusterObjectFieldDescriptor(Label="optionsOverride", Tag=6, Type=ColorControl.Bitmaps.OptionsBitmap),
                    ])

            stepMode: ColorControl.Enums.StepModeEnum = 0
            stepSize: uint = 0
            transitionTime: uint = 0
            colorTemperatureMinimumMireds: uint = 0
            colorTemperatureMaximumMireds: uint = 0
            optionsMask: ColorControl.Bitmaps.OptionsBitmap = 0
            optionsOverride: ColorControl.Bitmaps.OptionsBitmap = 0

    class Attributes:
        CurrentHue = _attr(__module__, __qualname__, "CurrentHue", 0x00000300, 0x00000000, "typing.Optional[uint]", None)

        CurrentSaturation = _attr(__module__, __qualname__, "CurrentSaturation", 0x00000300, 0x00000001, "typing.Optional[uint]", None)

        RemainingTime = _attr(__module__, __qualname__, "RemainingTime", 0x00000300, 0x00000002, "typing.Optional[uint]", None)

        CurrentX = _attr(__module__, __qualname__, "CurrentX", 0x00000300, 0x00000003, "typing.Optional[uint]", None)

        CurrentY = _attr(__module__, __qualname__, "CurrentY", 0x00000300, 0x00000004, "typing.Optional[uint]", None)

        DriftCompensation = _attr(__module__, __qualname__, "DriftCompensation", 0x00000300, 0x00000005, "typing.Optional[ColorControl.Enums.DriftCompensationEnum]", None)

        CompensationText = _attr(__module__, __qualname__, "CompensationText", 0x00000300, 0x00000006, "typing.Optional[str]", None)

        ColorTemperatureMireds = _attr(__module__, __qualname__, "ColorTemperatureMireds", 0x00000300, 0x00000007, "typing.Optional[uint]", None)

        ColorMode = _attr(__module__, __qualname__, "ColorMode", 0x00000300, 0x00000008, "ColorControl.Enums.ColorModeEnum", 0)

        Options = _attr(__module__, __qualname__, "Options", 0x00000300, 0x0000000F, "ColorControl.Bitmaps.OptionsBitmap", 0)

        NumberOfPrimaries = _attr(__module__, __qualname__, "NumberOfPrimaries", 0x00000300, 0x00000010, "typing.Union[Nullable, uint]", NullValue)

        Primary1X = _attr(__module__, __qualname__, "Primary1X", 0x00000300, 0x00000011, "typing.Optional[uint]", None)

        Primary1Y = _attr(__module__, __qualname__, "Primary1Y", 0x00000300, 0x00000012, "typing.Optional[uint]", None)

        Primary1Intensity = _attr(__module__, __qualname__, "Primary1Intensity", 0x00000300, 0x00000013, "typing.Union[None, Nullable, uint]", None)

        Primary2X = _attr(__module__, __qualname__, "Primary2X", 0x00000300, 0x00000015, "typing.Optional[uint]", None)

        Primary2Y = _attr(__module__, __qualname__, "Primary2Y", 0x00000300, 0x00000016, "typing.Optional[uint]", None)

        Primary2Intensity = _attr(__module__, __qualname__, "Primary2Intensity", 0x00000300, 0x00000017, "typing.Union[None, Nullable, uint]", None)

        Primary3X = _attr(__module__, __qualname__, "Primary3X", 0x00000300, 0x00000019, "typing.Optional[uint]", None)

        Primary3Y = _attr(__module__, __qualname__, "Primary3Y", 0x00000300, 0x0000001A, "typing.Optional[uint]", None)

        Primary3Intensity = _attr(__module__, __qualname__, "Primary3Intensity", 0x00000300, 0x0000001B, "typing.Union[None, Nullable, uint]", None)

        Primary4X = _attr(__module__, __qualname__, "Primary4X", 0x00000300, 0x00000020, "typing.Optional[uint]", None)

        Primary4Y = _attr(__module__, __qualname__, "Primary4Y", 0x00000300, 0x00000021, "typing.Optional[uint]", None)

        Primary4Intensity = _attr(__module__, __qualname__, "Primary4Intensity", 0x00000300, 0x00000022, "typing.Union[None, Nullable, uint]", None)

        Primary5X = _attr(__module__, __qualname__, "Primary5X", 0x00000300, 0x00000024, "typing.Optional[uint]", None)

        Primary5Y = _attr(__module__, __qualname__, "Primary5Y", 0x00000300, 0x00000025, "typing.Optional[uint]", None)

        Primary5Intensity = _attr(__module__, __qualname__, "Primary5Intensity", 0x00000300, 0x00000026, "typing.Union[None, Nullable, uint]", None)

        Primary6X = _attr(__module__, __qualname__, "Primary6X", 0x00000300, 0x00000028, "typing.Optional[uint]", None)

        Primary6Y = _attr(__module__, __qualname__, "Primary6Y", 0x00000300, 0x00000029, "typing.Optional[uint]", None)

        Primary6Intensity = _attr(__module__, __qualname__, "Primary6Intensity", 0x00000300, 0x0000002A, "typing.Union[None, Nullable, uint]", None)

        WhitePointX = _attr(__module__, __qualname__, "WhitePointX", 0x00000300, 0x00000030, "typing.Optional[uint]", None)

        WhitePointY = _attr(__module__, __qualname__, "WhitePointY", 0x00000300, 0x00000031, "typing.Optional[uint]", None)

        ColorPointRX = _attr(__module__, __qualname__, "ColorPointRX", 0x00000300, 0x00000032, "typing.Optional[uint]", None)

        ColorPointRY = _attr(__module__, __qualname__, "ColorPointRY", 0x00000300, 0x00000033, "typing.Optional[uint]", None)

        ColorPointRIntensity = _attr(__module__, __qualname__, "ColorPointRIntensity", 0x00000300, 0x00000034, "typing.Union[None, Nullable, uint]", None)

        ColorPointGX = _attr(__module__, __qualname__, "ColorPointGX", 0x00000300, 0x00000036, "typing.Optional[uint]", None)

        ColorPointGY = _attr(__module__, __qualname__, "ColorPointGY", 0x00000300, 0x00000037, "typing.Optional[uint]", None)

        ColorPointGIntensity = _attr(__module__, __qualname__, "ColorPointGIntensity", 0x00000300, 0x00000038, "typing.Union[None, Nullable, uint]", None)

        ColorPointBX = _attr(__module__, __qualname__, "ColorPointBX", 0x00000300, 0x0000003A, "typing.Optional[uint]", None)

        ColorPointBY = _attr(__module__, __qualname__, "ColorPointBY", 0x00000300, 0x0000003B, "typing.Optional[uint]", None)

        ColorPointBIntensity = _attr(__module__, __qualname__, "ColorPointBIntensity", 0x00000300, 0x0000003C, "typing.Union[None, Nullable, uint]", None)

        EnhancedCurrentHue = _attr(__module__, __qualname__, "EnhancedCurrentHue", 0x00000300, 0x00004000, "typing.Optional[uint]", None)

        EnhancedColorMode = _attr(__module__, __qualname__, "EnhancedColorMode", 0x00000300, 0x00004001, "ColorControl.Enums.EnhancedColorModeEnum", 0)

        ColorLoopActive = _attr(__module__, __qualname__, "ColorLoopActive", 0x00000300, 0x00004002, "typing.Optional[Globals.Enums.enum8]", None)

        ColorLoopDirection = _attr(__module__, __qualname__, "ColorLoopDirection", 0x00000300, 0x00004003, "typing.Optional[ColorControl.Enums.ColorLoopDirectionEnum]", None)

        ColorLoopTime = _attr(__module__, __qualname__, "ColorLoopTime", 0x00000300, 0x00004004, "typing.Optional[uint]", None)

        ColorLoopStartEnhancedHue = _attr(__module__, __qualname__, "ColorLoopStartEnhancedHue", 0x00000300, 0x00004005, "typing.Optional[uint]", None)

        ColorLoopStoredEnhancedHue = _attr(__module__, __qualname__, "ColorLoopStoredEnhancedHue", 0x00000300, 0x00004006, "typing.Optional[uint]", None)

        ColorCapabilities = _attr(__module__, __qualname__, "ColorCapabilities", 0x00000300, 0x0000400A, "ColorControl.Bitmaps.ColorCapabilitiesBitmap", 0)

        ColorTempPhysicalMinMireds = _attr(__module__, __qualname__, "ColorTempPhysicalMinMireds", 0x00000300, 0x0000400B, "typing.Optional[uint]", None)

        ColorTempPhysicalMaxMireds = _attr(__module__, __qualname__, "ColorTempPhysicalMaxMireds", 0x00000300, 0x0000400C, "typing.Optional[uint]", None)

        CoupleColorTempToLevelMinMireds = _attr(__module__, __qualname__, "CoupleColorTempToLevelMinMireds", 0x00000300, 0x0000400D, "typing.Optional[uint]", None)

        StartUpColorTemperatureMireds = _attr(__module__, __qualname__, "StartUpColorTemperatureMireds", 0x00000300, 0x00004010, "typing.Union[None, Nullable, uint]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000300, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000300, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000300, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000300, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000300, 0x0000FFFD, "uint", 0)
