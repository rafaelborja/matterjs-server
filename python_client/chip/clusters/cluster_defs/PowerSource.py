"""PowerSource cluster definition (auto-generated, DO NOT edit)."""

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
class PowerSource(Cluster):
    id: typing.ClassVar[int] = 0x0000002F

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="status", Tag=0x00000000, Type=PowerSource.Enums.PowerSourceStatusEnum),
                ClusterObjectFieldDescriptor(Label="order", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="description", Tag=0x00000002, Type=str),
                ClusterObjectFieldDescriptor(Label="wiredAssessedInputVoltage", Tag=0x00000003, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="wiredAssessedInputFrequency", Tag=0x00000004, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="wiredCurrentType", Tag=0x00000005, Type=typing.Optional[PowerSource.Enums.WiredCurrentTypeEnum]),
                ClusterObjectFieldDescriptor(Label="wiredAssessedCurrent", Tag=0x00000006, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="wiredNominalVoltage", Tag=0x00000007, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="wiredMaximumCurrent", Tag=0x00000008, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="wiredPresent", Tag=0x00000009, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="activeWiredFaults", Tag=0x0000000A, Type=typing.Optional[typing.List[PowerSource.Enums.WiredFaultEnum]]),
                ClusterObjectFieldDescriptor(Label="batVoltage", Tag=0x0000000B, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="batPercentRemaining", Tag=0x0000000C, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="batTimeRemaining", Tag=0x0000000D, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="batChargeLevel", Tag=0x0000000E, Type=typing.Optional[PowerSource.Enums.BatChargeLevelEnum]),
                ClusterObjectFieldDescriptor(Label="batReplacementNeeded", Tag=0x0000000F, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="batReplaceability", Tag=0x00000010, Type=typing.Optional[PowerSource.Enums.BatReplaceabilityEnum]),
                ClusterObjectFieldDescriptor(Label="batPresent", Tag=0x00000011, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="activeBatFaults", Tag=0x00000012, Type=typing.Optional[typing.List[PowerSource.Enums.BatFaultEnum]]),
                ClusterObjectFieldDescriptor(Label="batReplacementDescription", Tag=0x00000013, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="batCommonDesignation", Tag=0x00000014, Type=typing.Optional[PowerSource.Enums.BatCommonDesignationEnum]),
                ClusterObjectFieldDescriptor(Label="batANSIDesignation", Tag=0x00000015, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="batIECDesignation", Tag=0x00000016, Type=typing.Optional[str]),
                ClusterObjectFieldDescriptor(Label="batApprovedChemistry", Tag=0x00000017, Type=typing.Optional[PowerSource.Enums.BatApprovedChemistryEnum]),
                ClusterObjectFieldDescriptor(Label="batCapacity", Tag=0x00000018, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="batQuantity", Tag=0x00000019, Type=typing.Optional[uint]),
                ClusterObjectFieldDescriptor(Label="batChargeState", Tag=0x0000001A, Type=typing.Optional[PowerSource.Enums.BatChargeStateEnum]),
                ClusterObjectFieldDescriptor(Label="batTimeToFullCharge", Tag=0x0000001B, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="batFunctionalWhileCharging", Tag=0x0000001C, Type=typing.Optional[bool]),
                ClusterObjectFieldDescriptor(Label="batChargingCurrent", Tag=0x0000001D, Type=typing.Union[None, Nullable, uint]),
                ClusterObjectFieldDescriptor(Label="activeBatChargeFaults", Tag=0x0000001E, Type=typing.Optional[typing.List[PowerSource.Enums.BatChargeFaultEnum]]),
                ClusterObjectFieldDescriptor(Label="endpointList", Tag=0x0000001F, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    status: PowerSource.Enums.PowerSourceStatusEnum = 0
    order: uint = 0
    description: str = ""
    wiredAssessedInputVoltage: typing.Union[None, Nullable, uint] = None
    wiredAssessedInputFrequency: typing.Union[None, Nullable, uint] = None
    wiredCurrentType: typing.Optional[PowerSource.Enums.WiredCurrentTypeEnum] = None
    wiredAssessedCurrent: typing.Union[None, Nullable, uint] = None
    wiredNominalVoltage: typing.Optional[uint] = None
    wiredMaximumCurrent: typing.Optional[uint] = None
    wiredPresent: typing.Optional[bool] = None
    activeWiredFaults: typing.Optional[typing.List[PowerSource.Enums.WiredFaultEnum]] = None
    batVoltage: typing.Union[None, Nullable, uint] = None
    batPercentRemaining: typing.Union[None, Nullable, uint] = None
    batTimeRemaining: typing.Union[None, Nullable, uint] = None
    batChargeLevel: typing.Optional[PowerSource.Enums.BatChargeLevelEnum] = None
    batReplacementNeeded: typing.Optional[bool] = None
    batReplaceability: typing.Optional[PowerSource.Enums.BatReplaceabilityEnum] = None
    batPresent: typing.Optional[bool] = None
    activeBatFaults: typing.Optional[typing.List[PowerSource.Enums.BatFaultEnum]] = None
    batReplacementDescription: typing.Optional[str] = None
    batCommonDesignation: typing.Optional[PowerSource.Enums.BatCommonDesignationEnum] = None
    batANSIDesignation: typing.Optional[str] = None
    batIECDesignation: typing.Optional[str] = None
    batApprovedChemistry: typing.Optional[PowerSource.Enums.BatApprovedChemistryEnum] = None
    batCapacity: typing.Optional[uint] = None
    batQuantity: typing.Optional[uint] = None
    batChargeState: typing.Optional[PowerSource.Enums.BatChargeStateEnum] = None
    batTimeToFullCharge: typing.Union[None, Nullable, uint] = None
    batFunctionalWhileCharging: typing.Optional[bool] = None
    batChargingCurrent: typing.Union[None, Nullable, uint] = None
    activeBatChargeFaults: typing.Optional[typing.List[PowerSource.Enums.BatChargeFaultEnum]] = None
    endpointList: typing.List[uint] = field(default_factory=lambda: [])
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class WiredFaultEnum(MatterIntEnum):
            kUnspecified = 0x00
            kOverVoltage = 0x01
            kUnderVoltage = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class BatFaultEnum(MatterIntEnum):
            kUnspecified = 0x00
            kOverTemp = 0x01
            kUnderTemp = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class BatChargeFaultEnum(MatterIntEnum):
            kUnspecified = 0x00
            kAmbientTooHot = 0x01
            kAmbientTooCold = 0x02
            kBatteryTooHot = 0x03
            kBatteryTooCold = 0x04
            kBatteryAbsent = 0x05
            kBatteryOverVoltage = 0x06
            kBatteryUnderVoltage = 0x07
            kChargerOverVoltage = 0x08
            kChargerUnderVoltage = 0x09
            kSafetyTimeout = 0x0A
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 11

        class PowerSourceStatusEnum(MatterIntEnum):
            kUnspecified = 0x00
            kActive = 0x01
            kStandby = 0x02
            kUnavailable = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class WiredCurrentTypeEnum(MatterIntEnum):
            kAc = 0x00
            kDc = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

        class BatChargeLevelEnum(MatterIntEnum):
            kOk = 0x00
            kWarning = 0x01
            kCritical = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class BatReplaceabilityEnum(MatterIntEnum):
            kUnspecified = 0x00
            kNotReplaceable = 0x01
            kUserReplaceable = 0x02
            kFactoryReplaceable = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class BatCommonDesignationEnum(MatterIntEnum):
            kUnspecified = 0x00
            kAaa = 0x01
            kAa = 0x02
            kC = 0x03
            kD = 0x04
            k4v5 = 0x05
            k6v0 = 0x06
            k9v0 = 0x07
            k12aa = 0x08
            kAaaa = 0x09
            kA = 0x0A
            kB = 0x0B
            kF = 0x0C
            kN = 0x0D
            kNo6 = 0x0E
            kSubC = 0x0F
            kA23 = 0x10
            kA27 = 0x11
            kBa5800 = 0x12
            kDuplex = 0x13
            k4sr44 = 0x14
            k523 = 0x15
            k531 = 0x16
            k15v0 = 0x17
            k22v5 = 0x18
            k30v0 = 0x19
            k45v0 = 0x1A
            k67v5 = 0x1B
            kJ = 0x1C
            kCr123a = 0x1D
            kCr2 = 0x1E
            k2cr5 = 0x1F
            kCrP2 = 0x20
            kCrV3 = 0x21
            kSr41 = 0x22
            kSr43 = 0x23
            kSr44 = 0x24
            kSr45 = 0x25
            kSr48 = 0x26
            kSr54 = 0x27
            kSr55 = 0x28
            kSr57 = 0x29
            kSr58 = 0x2A
            kSr59 = 0x2B
            kSr60 = 0x2C
            kSr63 = 0x2D
            kSr64 = 0x2E
            kSr65 = 0x2F
            kSr66 = 0x30
            kSr67 = 0x31
            kSr68 = 0x32
            kSr69 = 0x33
            kSr516 = 0x34
            kSr731 = 0x35
            kSr712 = 0x36
            kLr932 = 0x37
            kA5 = 0x38
            kA10 = 0x39
            kA13 = 0x3A
            kA312 = 0x3B
            kA675 = 0x3C
            kAc41e = 0x3D
            k10180 = 0x3E
            k10280 = 0x3F
            k10440 = 0x40
            k14250 = 0x41
            k14430 = 0x42
            k14500 = 0x43
            k14650 = 0x44
            k15270 = 0x45
            k16340 = 0x46
            kRcr123a = 0x47
            k17500 = 0x48
            k17670 = 0x49
            k18350 = 0x4A
            k18500 = 0x4B
            k18650 = 0x4C
            k19670 = 0x4D
            k25500 = 0x4E
            k26650 = 0x4F
            k32600 = 0x50
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 81

        class BatApprovedChemistryEnum(MatterIntEnum):
            kUnspecified = 0x00
            kAlkaline = 0x01
            kLithiumCarbonFluoride = 0x02
            kLithiumChromiumOxide = 0x03
            kLithiumCopperOxide = 0x04
            kLithiumIronDisulfide = 0x05
            kLithiumManganeseDioxide = 0x06
            kLithiumThionylChloride = 0x07
            kMagnesium = 0x08
            kMercuryOxide = 0x09
            kNickelOxyhydride = 0x0A
            kSilverOxide = 0x0B
            kZincAir = 0x0C
            kZincCarbon = 0x0D
            kZincChloride = 0x0E
            kZincManganeseDioxide = 0x0F
            kLeadAcid = 0x10
            kLithiumCobaltOxide = 0x11
            kLithiumIon = 0x12
            kLithiumIonPolymer = 0x13
            kLithiumIronPhosphate = 0x14
            kLithiumSulfur = 0x15
            kLithiumTitanate = 0x16
            kNickelCadmium = 0x17
            kNickelHydrogen = 0x18
            kNickelIron = 0x19
            kNickelMetalHydride = 0x1A
            kNickelZinc = 0x1B
            kSilverZinc = 0x1C
            kSodiumIon = 0x1D
            kSodiumSulfur = 0x1E
            kZincBromide = 0x1F
            kZincCerium = 0x20
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 33

        class BatChargeStateEnum(MatterIntEnum):
            kUnknown = 0x00
            kIsCharging = 0x01
            kIsAtFullCharge = 0x02
            kIsNotCharging = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

    class Bitmaps:
        class Feature(IntFlag):
            kWired = 0x1
            kBattery = 0x2
            kRechargeable = 0x4
            kReplaceable = 0x8

    class Attributes:
        Status = _attr(__module__, __qualname__, "Status", 0x0000002F, 0x00000000, "PowerSource.Enums.PowerSourceStatusEnum", 0)

        Order = _attr(__module__, __qualname__, "Order", 0x0000002F, 0x00000001, "uint", 0)

        Description = _attr(__module__, __qualname__, "Description", 0x0000002F, 0x00000002, "str", "")

        WiredAssessedInputVoltage = _attr(__module__, __qualname__, "WiredAssessedInputVoltage", 0x0000002F, 0x00000003, "typing.Union[None, Nullable, uint]", None)

        WiredAssessedInputFrequency = _attr(__module__, __qualname__, "WiredAssessedInputFrequency", 0x0000002F, 0x00000004, "typing.Union[None, Nullable, uint]", None)

        WiredCurrentType = _attr(__module__, __qualname__, "WiredCurrentType", 0x0000002F, 0x00000005, "typing.Optional[PowerSource.Enums.WiredCurrentTypeEnum]", None)

        WiredAssessedCurrent = _attr(__module__, __qualname__, "WiredAssessedCurrent", 0x0000002F, 0x00000006, "typing.Union[None, Nullable, uint]", None)

        WiredNominalVoltage = _attr(__module__, __qualname__, "WiredNominalVoltage", 0x0000002F, 0x00000007, "typing.Optional[uint]", None)

        WiredMaximumCurrent = _attr(__module__, __qualname__, "WiredMaximumCurrent", 0x0000002F, 0x00000008, "typing.Optional[uint]", None)

        WiredPresent = _attr(__module__, __qualname__, "WiredPresent", 0x0000002F, 0x00000009, "typing.Optional[bool]", None)

        ActiveWiredFaults = _attr(__module__, __qualname__, "ActiveWiredFaults", 0x0000002F, 0x0000000A, "typing.Optional[typing.List[PowerSource.Enums.WiredFaultEnum]]", None)

        BatVoltage = _attr(__module__, __qualname__, "BatVoltage", 0x0000002F, 0x0000000B, "typing.Union[None, Nullable, uint]", None)

        BatPercentRemaining = _attr(__module__, __qualname__, "BatPercentRemaining", 0x0000002F, 0x0000000C, "typing.Union[None, Nullable, uint]", None)

        BatTimeRemaining = _attr(__module__, __qualname__, "BatTimeRemaining", 0x0000002F, 0x0000000D, "typing.Union[None, Nullable, uint]", None)

        BatChargeLevel = _attr(__module__, __qualname__, "BatChargeLevel", 0x0000002F, 0x0000000E, "typing.Optional[PowerSource.Enums.BatChargeLevelEnum]", None)

        BatReplacementNeeded = _attr(__module__, __qualname__, "BatReplacementNeeded", 0x0000002F, 0x0000000F, "typing.Optional[bool]", None)

        BatReplaceability = _attr(__module__, __qualname__, "BatReplaceability", 0x0000002F, 0x00000010, "typing.Optional[PowerSource.Enums.BatReplaceabilityEnum]", None)

        BatPresent = _attr(__module__, __qualname__, "BatPresent", 0x0000002F, 0x00000011, "typing.Optional[bool]", None)

        ActiveBatFaults = _attr(__module__, __qualname__, "ActiveBatFaults", 0x0000002F, 0x00000012, "typing.Optional[typing.List[PowerSource.Enums.BatFaultEnum]]", None)

        BatReplacementDescription = _attr(__module__, __qualname__, "BatReplacementDescription", 0x0000002F, 0x00000013, "typing.Optional[str]", None)

        BatCommonDesignation = _attr(__module__, __qualname__, "BatCommonDesignation", 0x0000002F, 0x00000014, "typing.Optional[PowerSource.Enums.BatCommonDesignationEnum]", None)

        BatANSIDesignation = _attr(__module__, __qualname__, "BatANSIDesignation", 0x0000002F, 0x00000015, "typing.Optional[str]", None)

        BatIECDesignation = _attr(__module__, __qualname__, "BatIECDesignation", 0x0000002F, 0x00000016, "typing.Optional[str]", None)

        BatApprovedChemistry = _attr(__module__, __qualname__, "BatApprovedChemistry", 0x0000002F, 0x00000017, "typing.Optional[PowerSource.Enums.BatApprovedChemistryEnum]", None)

        BatCapacity = _attr(__module__, __qualname__, "BatCapacity", 0x0000002F, 0x00000018, "typing.Optional[uint]", None)

        BatQuantity = _attr(__module__, __qualname__, "BatQuantity", 0x0000002F, 0x00000019, "typing.Optional[uint]", None)

        BatChargeState = _attr(__module__, __qualname__, "BatChargeState", 0x0000002F, 0x0000001A, "typing.Optional[PowerSource.Enums.BatChargeStateEnum]", None)

        BatTimeToFullCharge = _attr(__module__, __qualname__, "BatTimeToFullCharge", 0x0000002F, 0x0000001B, "typing.Union[None, Nullable, uint]", None)

        BatFunctionalWhileCharging = _attr(__module__, __qualname__, "BatFunctionalWhileCharging", 0x0000002F, 0x0000001C, "typing.Optional[bool]", None)

        BatChargingCurrent = _attr(__module__, __qualname__, "BatChargingCurrent", 0x0000002F, 0x0000001D, "typing.Union[None, Nullable, uint]", None)

        ActiveBatChargeFaults = _attr(__module__, __qualname__, "ActiveBatChargeFaults", 0x0000002F, 0x0000001E, "typing.Optional[typing.List[PowerSource.Enums.BatChargeFaultEnum]]", None)

        EndpointList = _attr(__module__, __qualname__, "EndpointList", 0x0000002F, 0x0000001F, "typing.List[uint]", None, "[]")

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000002F, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000002F, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000002F, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000002F, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000002F, 0x0000FFFD, "uint", 0)

    class Events:
        @dataclass
        class WiredFaultChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000002F

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000000

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="current", Tag=0, Type=typing.List[PowerSource.Enums.WiredFaultEnum]),
                        ClusterObjectFieldDescriptor(Label="previous", Tag=1, Type=typing.List[PowerSource.Enums.WiredFaultEnum]),
                    ])

            current: typing.List[PowerSource.Enums.WiredFaultEnum] = field(default_factory=lambda: [])
            previous: typing.List[PowerSource.Enums.WiredFaultEnum] = field(default_factory=lambda: [])

        @dataclass
        class BatFaultChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000002F

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000001

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="current", Tag=0, Type=typing.List[PowerSource.Enums.BatFaultEnum]),
                        ClusterObjectFieldDescriptor(Label="previous", Tag=1, Type=typing.List[PowerSource.Enums.BatFaultEnum]),
                    ])

            current: typing.List[PowerSource.Enums.BatFaultEnum] = field(default_factory=lambda: [])
            previous: typing.List[PowerSource.Enums.BatFaultEnum] = field(default_factory=lambda: [])

        @dataclass
        class BatChargeFaultChange(ClusterEvent):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x0000002F

            @ChipUtility.classproperty
            def event_id(cls) -> int:
                return 0x00000002

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="current", Tag=0, Type=typing.List[PowerSource.Enums.BatChargeFaultEnum]),
                        ClusterObjectFieldDescriptor(Label="previous", Tag=1, Type=typing.List[PowerSource.Enums.BatChargeFaultEnum]),
                    ])

            current: typing.List[PowerSource.Enums.BatChargeFaultEnum] = field(default_factory=lambda: [])
            previous: typing.List[PowerSource.Enums.BatChargeFaultEnum] = field(default_factory=lambda: [])
