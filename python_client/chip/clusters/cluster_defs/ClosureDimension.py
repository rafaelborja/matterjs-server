"""ClosureDimension cluster definition (auto-generated, DO NOT edit)."""

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
class ClosureDimension(Cluster):
    id: typing.ClassVar[int] = 0x00000105

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="currentState", Tag=0x00000000, Type=typing.Union[Nullable, ClosureDimension.Structs.DimensionStateStruct]),
                ClusterObjectFieldDescriptor(Label="targetState", Tag=0x00000001, Type=typing.Union[Nullable, ClosureDimension.Structs.DimensionStateStruct]),
                ClusterObjectFieldDescriptor(Label="resolution", Tag=0x00000002, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="stepValue", Tag=0x00000003, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="unit", Tag=0x00000004, Type=typing.Optional[ClosureDimension.Enums.ClosureUnitEnum]),
                ClusterObjectFieldDescriptor(Label="unitRange", Tag=0x00000005, Type=typing.Union[None, Nullable, ClosureDimension.Structs.UnitRangeStruct]),
                ClusterObjectFieldDescriptor(Label="limitRange", Tag=0x00000006, Type=typing.Optional[ClosureDimension.Structs.RangePercent100thsStruct]),
                ClusterObjectFieldDescriptor(Label="translationDirection", Tag=0x00000007, Type=typing.Optional[ClosureDimension.Enums.TranslationDirectionEnum]),
                ClusterObjectFieldDescriptor(Label="rotationAxis", Tag=0x00000008, Type=typing.Optional[ClosureDimension.Enums.RotationAxisEnum]),
                ClusterObjectFieldDescriptor(Label="overflow", Tag=0x00000009, Type=typing.Optional[ClosureDimension.Enums.OverflowEnum]),
                ClusterObjectFieldDescriptor(Label="modulationType", Tag=0x0000000A, Type=typing.Optional[ClosureDimension.Enums.ModulationTypeEnum]),
                ClusterObjectFieldDescriptor(Label="latchControlModes", Tag=0x0000000B, Type=typing.Optional[ClosureDimension.Bitmaps.LatchControlModesBitmap]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    currentState: typing.Union[Nullable, ClosureDimension.Structs.DimensionStateStruct] = NullValue
    targetState: typing.Union[Nullable, ClosureDimension.Structs.DimensionStateStruct] = NullValue
    resolution: typing.Optional[uint] = None
    stepValue: typing.Optional[uint] = None
    unit: typing.Optional[ClosureDimension.Enums.ClosureUnitEnum] = None
    unitRange: typing.Union[None, Nullable, ClosureDimension.Structs.UnitRangeStruct] = None
    limitRange: typing.Optional[ClosureDimension.Structs.RangePercent100thsStruct] = None
    translationDirection: typing.Optional[ClosureDimension.Enums.TranslationDirectionEnum] = None
    rotationAxis: typing.Optional[ClosureDimension.Enums.RotationAxisEnum] = None
    overflow: typing.Optional[ClosureDimension.Enums.OverflowEnum] = None
    modulationType: typing.Optional[ClosureDimension.Enums.ModulationTypeEnum] = None
    latchControlModes: typing.Optional[ClosureDimension.Bitmaps.LatchControlModesBitmap] = None
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class TranslationDirectionEnum(MatterIntEnum):
            kDownward = 0x00
            kUpward = 0x01
            kVerticalMask = 0x02
            kVerticalSymmetry = 0x03
            kLeftward = 0x04
            kRightward = 0x05
            kHorizontalMask = 0x06
            kHorizontalSymmetry = 0x07
            kForward = 0x08
            kBackward = 0x09
            kDepthMask = 0x0A
            kDepthSymmetry = 0x0B
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 12

        class RotationAxisEnum(MatterIntEnum):
            kLeft = 0x00
            kCenteredVertical = 0x01
            kLeftAndRight = 0x02
            kRight = 0x03
            kTop = 0x04
            kCenteredHorizontal = 0x05
            kTopAndBottom = 0x06
            kBottom = 0x07
            kLeftBarrier = 0x08
            kLeftAndRightBarriers = 0x09
            kRightBarrier = 0x0A
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 11

        class OverflowEnum(MatterIntEnum):
            kNoOverflow = 0x00
            kInside = 0x01
            kOutside = 0x02
            kTopInside = 0x03
            kTopOutside = 0x04
            kBottomInside = 0x05
            kBottomOutside = 0x06
            kLeftInside = 0x07
            kLeftOutside = 0x08
            kRightInside = 0x09
            kRightOutside = 0x0A
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 11

        class ModulationTypeEnum(MatterIntEnum):
            kSlatsOrientation = 0x00
            kSlatsOpenwork = 0x01
            kStripesAlignment = 0x02
            kOpacity = 0x03
            kVentilation = 0x04
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 5

        class ClosureUnitEnum(MatterIntEnum):
            kMillimeter = 0x00
            kDegree = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class StepDirectionEnum(MatterIntEnum):
            kDecrease = 0x00
            kIncrease = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Bitmaps:
        class Feature(IntFlag):
            kPositioning = 0x1
            kMotionLatching = 0x2
            kUnit = 0x4
            kLimitation = 0x8
            kSpeed = 0x10
            kTranslation = 0x20
            kRotation = 0x40
            kModulation = 0x80

        class LatchControlModesBitmap(IntFlag):
            kRemoteLatching = 0x1
            kRemoteUnlatching = 0x2

    class Structs:
        @dataclass
        class RangePercent100thsStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="min", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="max", Tag=1, Type=uint),
                    ])

            min: uint = 0
            max: uint = 0

        @dataclass
        class UnitRangeStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="min", Tag=0, Type=int),
                        ClusterObjectFieldDescriptor(Label="max", Tag=1, Type=int),
                    ])

            min: int = 0
            max: int = 0

        @dataclass
        class DimensionStateStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="position", Tag=0, Type=typing.Union[None, Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="latch", Tag=1, Type=typing.Union[None, Nullable, bool]),
                        ClusterObjectFieldDescriptor(Label="speed", Tag=2, Type=typing.Optional[Globals.Enums.ThreeLevelAutoEnum]),
                    ])

            position: typing.Union[None, Nullable, uint] = None
            latch: typing.Union[None, Nullable, bool] = None
            speed: typing.Optional[Globals.Enums.ThreeLevelAutoEnum] = None

    class Commands:
        @dataclass
        class SetTarget(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000105
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="position", Tag=0, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="latch", Tag=1, Type=typing.Optional[bool]),
                        ClusterObjectFieldDescriptor(Label="speed", Tag=2, Type=typing.Optional[Globals.Enums.ThreeLevelAutoEnum]),
                    ])

            position: typing.Optional[uint] = None
            latch: typing.Optional[bool] = None
            speed: typing.Optional[Globals.Enums.ThreeLevelAutoEnum] = None

        @dataclass
        class Step(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000105
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def must_use_timed_invoke(cls) -> bool:
                return True

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="direction", Tag=0, Type=ClosureDimension.Enums.StepDirectionEnum),
                        ClusterObjectFieldDescriptor(Label="numberOfSteps", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="speed", Tag=2, Type=typing.Optional[Globals.Enums.ThreeLevelAutoEnum]),
                    ])

            direction: ClosureDimension.Enums.StepDirectionEnum = 0
            numberOfSteps: uint = 0
            speed: typing.Optional[Globals.Enums.ThreeLevelAutoEnum] = None

    class Attributes:
        CurrentState = _attr(__module__, __qualname__, "CurrentState", 0x00000105, 0x00000000, "typing.Union[Nullable, ClosureDimension.Structs.DimensionStateStruct]", NullValue)

        TargetState = _attr(__module__, __qualname__, "TargetState", 0x00000105, 0x00000001, "typing.Union[Nullable, ClosureDimension.Structs.DimensionStateStruct]", NullValue)

        Resolution = _attr(__module__, __qualname__, "Resolution", 0x00000105, 0x00000002, "typing.Optional[uint]", None)

        StepValue = _attr(__module__, __qualname__, "StepValue", 0x00000105, 0x00000003, "typing.Optional[uint]", None)

        Unit = _attr(__module__, __qualname__, "Unit", 0x00000105, 0x00000004, "typing.Optional[ClosureDimension.Enums.ClosureUnitEnum]", None)

        UnitRange = _attr(__module__, __qualname__, "UnitRange", 0x00000105, 0x00000005, "typing.Union[None, Nullable, ClosureDimension.Structs.UnitRangeStruct]", None)

        LimitRange = _attr(__module__, __qualname__, "LimitRange", 0x00000105, 0x00000006, "typing.Optional[ClosureDimension.Structs.RangePercent100thsStruct]", None)

        TranslationDirection = _attr(__module__, __qualname__, "TranslationDirection", 0x00000105, 0x00000007, "typing.Optional[ClosureDimension.Enums.TranslationDirectionEnum]", None)

        RotationAxis = _attr(__module__, __qualname__, "RotationAxis", 0x00000105, 0x00000008, "typing.Optional[ClosureDimension.Enums.RotationAxisEnum]", None)

        Overflow = _attr(__module__, __qualname__, "Overflow", 0x00000105, 0x00000009, "typing.Optional[ClosureDimension.Enums.OverflowEnum]", None)

        ModulationType = _attr(__module__, __qualname__, "ModulationType", 0x00000105, 0x0000000A, "typing.Optional[ClosureDimension.Enums.ModulationTypeEnum]", None)

        LatchControlModes = _attr(__module__, __qualname__, "LatchControlModes", 0x00000105, 0x0000000B, "typing.Optional[ClosureDimension.Bitmaps.LatchControlModesBitmap]", None)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000105, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000105, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000105, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000105, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000105, 0x0000FFFD, "uint", 0)
