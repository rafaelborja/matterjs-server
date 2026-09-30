"""OperationalCredentials cluster definition (auto-generated, DO NOT edit)."""

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
class OperationalCredentials(Cluster):
    id: typing.ClassVar[int] = 0x0000003E

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="NOCs", Tag=0x00000000, Type=typing.List[OperationalCredentials.Structs.NOCStruct]),
                ClusterObjectFieldDescriptor(Label="fabrics", Tag=0x00000001, Type=typing.List[OperationalCredentials.Structs.FabricDescriptorStruct]),
                ClusterObjectFieldDescriptor(Label="supportedFabrics", Tag=0x00000002, Type=uint),
                ClusterObjectFieldDescriptor(Label="commissionedFabrics", Tag=0x00000003, Type=uint),
                ClusterObjectFieldDescriptor(Label="trustedRootCertificates", Tag=0x00000004, Type=typing.List[bytes]),
                ClusterObjectFieldDescriptor(Label="currentFabricIndex", Tag=0x00000005, Type=uint),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    NOCs: typing.List[OperationalCredentials.Structs.NOCStruct] = field(default_factory=lambda: [])
    fabrics: typing.List[OperationalCredentials.Structs.FabricDescriptorStruct] = field(default_factory=lambda: [])
    supportedFabrics: uint = 0
    commissionedFabrics: uint = 0
    trustedRootCertificates: typing.List[bytes] = field(default_factory=lambda: [])
    currentFabricIndex: uint = 0
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class CertificateChainTypeEnum(MatterIntEnum):
            kDACCertificate = 0x01
            kPAICertificate = 0x02
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 3

        class NodeOperationalCertStatusEnum(MatterIntEnum):
            kOk = 0x00
            kInvalidPublicKey = 0x01
            kInvalidNodeOpId = 0x02
            kInvalidNOC = 0x03
            kMissingCsr = 0x04
            kTableFull = 0x05
            kInvalidAdminSubject = 0x06
            kFabricConflict = 0x09
            kLabelConflict = 0x0A
            kInvalidFabricIndex = 0x0B
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 12

    class Structs:
        @dataclass
        class NOCStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="noc", Tag=1, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="icac", Tag=2, Type=typing.Union[Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="vvsc", Tag=3, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            noc: bytes = b""
            icac: typing.Union[Nullable, bytes] = NullValue
            vvsc: typing.Optional[bytes] = None
            fabricIndex: uint = 0

        @dataclass
        class FabricDescriptorStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="rootPublicKey", Tag=1, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="vendorID", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="fabricID", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=4, Type=uint),
                        ClusterObjectFieldDescriptor(Label="label", Tag=5, Type=str),
                        ClusterObjectFieldDescriptor(Label="VIDVerificationStatement", Tag=6, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=254, Type=uint),
                    ])

            rootPublicKey: bytes = b""
            vendorID: uint = 0
            fabricID: uint = 0
            nodeID: uint = 0
            label: str = ""
            VIDVerificationStatement: typing.Optional[bytes] = None
            fabricIndex: uint = 0

    class Commands:
        @dataclass
        class AttestationRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'AttestationResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="attestationNonce", Tag=0, Type=bytes),
                    ])

            attestationNonce: bytes = b""

        @dataclass
        class CertificateChainRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'CertificateChainResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="certificateType", Tag=0, Type=OperationalCredentials.Enums.CertificateChainTypeEnum),
                    ])

            certificateType: OperationalCredentials.Enums.CertificateChainTypeEnum = 0

        @dataclass
        class CSRRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'CSRResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="CSRNonce", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="isForUpdateNOC", Tag=1, Type=typing.Optional[bool]),
                    ])

            CSRNonce: bytes = b""
            isForUpdateNOC: typing.Optional[bool] = None

        @dataclass
        class AddNOC(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'NOCResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="NOCValue", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="ICACValue", Tag=1, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="IPKValue", Tag=2, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="caseAdminSubject", Tag=3, Type=uint),
                        ClusterObjectFieldDescriptor(Label="adminVendorId", Tag=4, Type=uint),
                    ])

            NOCValue: bytes = b""
            ICACValue: typing.Optional[bytes] = None
            IPKValue: bytes = b""
            caseAdminSubject: uint = 0
            adminVendorId: uint = 0

        @dataclass
        class UpdateNOC(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'NOCResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="NOCValue", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="ICACValue", Tag=1, Type=typing.Optional[bytes]),
                    ])

            NOCValue: bytes = b""
            ICACValue: typing.Optional[bytes] = None

        @dataclass
        class UpdateFabricLabel(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000009
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'NOCResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="label", Tag=0, Type=str),
                    ])

            label: str = ""

        @dataclass
        class RemoveFabric(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x0000000A
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'NOCResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=0, Type=uint),
                    ])

            fabricIndex: uint = 0

        @dataclass
        class AddTrustedRootCertificate(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x0000000B
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="rootCACertificate", Tag=0, Type=bytes),
                    ])

            rootCACertificate: bytes = b""

        @dataclass
        class SetVIDVerificationStatement(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x0000000C
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="vendorID", Tag=0, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="VIDVerificationStatement", Tag=1, Type=typing.Optional[bytes]),
                        ClusterObjectFieldDescriptor(Label="vvsc", Tag=2, Type=typing.Optional[bytes]),
                    ])

            vendorID: typing.Optional[uint] = None
            VIDVerificationStatement: typing.Optional[bytes] = None
            vvsc: typing.Optional[bytes] = None

        @dataclass
        class SignVIDVerificationRequest(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x0000000D
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = 'SignVIDVerificationResponse'

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="clientChallenge", Tag=1, Type=bytes),
                    ])

            fabricIndex: uint = 0
            clientChallenge: bytes = b""

        @dataclass
        class AttestationResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="attestationElements", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="attestationSignature", Tag=1, Type=bytes),
                    ])

            attestationElements: bytes = b""
            attestationSignature: bytes = b""

        @dataclass
        class CertificateChainResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="certificate", Tag=0, Type=bytes),
                    ])

            certificate: bytes = b""

        @dataclass
        class CSRResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="NOCSRElements", Tag=0, Type=bytes),
                        ClusterObjectFieldDescriptor(Label="attestationSignature", Tag=1, Type=bytes),
                    ])

            NOCSRElements: bytes = b""
            attestationSignature: bytes = b""

        @dataclass
        class NOCResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x00000008
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="statusCode", Tag=0, Type=OperationalCredentials.Enums.NodeOperationalCertStatusEnum),
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=1, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="debugText", Tag=2, Type=typing.Optional[str]),
                    ])

            statusCode: OperationalCredentials.Enums.NodeOperationalCertStatusEnum = 0
            fabricIndex: typing.Optional[uint] = None
            debugText: typing.Optional[str] = None

        @dataclass
        class SignVIDVerificationResponse(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x0000003E
            command_id: typing.ClassVar[int] = 0x0000000E
            is_client: typing.ClassVar[bool] = False
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="fabricIndex", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="fabricBindingVersion", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="signature", Tag=2, Type=bytes),
                    ])

            fabricIndex: uint = 0
            fabricBindingVersion: uint = 0
            signature: bytes = b""

    class Attributes:
        NOCs = _attr(__module__, __qualname__, "NOCs", 0x0000003E, 0x00000000, "typing.List[OperationalCredentials.Structs.NOCStruct]", None, "[]")

        Fabrics = _attr(__module__, __qualname__, "Fabrics", 0x0000003E, 0x00000001, "typing.List[OperationalCredentials.Structs.FabricDescriptorStruct]", None, "[]")

        SupportedFabrics = _attr(__module__, __qualname__, "SupportedFabrics", 0x0000003E, 0x00000002, "uint", 0)

        CommissionedFabrics = _attr(__module__, __qualname__, "CommissionedFabrics", 0x0000003E, 0x00000003, "uint", 0)

        TrustedRootCertificates = _attr(__module__, __qualname__, "TrustedRootCertificates", 0x0000003E, 0x00000004, "typing.List[bytes]", None, "[]")

        CurrentFabricIndex = _attr(__module__, __qualname__, "CurrentFabricIndex", 0x0000003E, 0x00000005, "uint", 0)

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x0000003E, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x0000003E, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x0000003E, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x0000003E, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x0000003E, 0x0000FFFD, "uint", 0)
