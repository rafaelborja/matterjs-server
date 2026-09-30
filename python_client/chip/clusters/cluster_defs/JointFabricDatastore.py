"""JointFabricDatastore cluster definition (auto-generated, DO NOT edit)."""

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
class JointFabricDatastore(Cluster):
    id: typing.ClassVar[int] = 0x00000752

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(Label="anchorRootCa", Tag=0x00000000, Type=bytes),
                ClusterObjectFieldDescriptor(Label="anchorNodeID", Tag=0x00000001, Type=uint),
                ClusterObjectFieldDescriptor(Label="anchorVendorID", Tag=0x00000002, Type=uint),
                ClusterObjectFieldDescriptor(Label="friendlyName", Tag=0x00000003, Type=str),
                ClusterObjectFieldDescriptor(Label="groupKeySetList", Tag=0x00000004, Type=typing.List[JointFabricDatastore.Structs.DatastoreGroupKeySetStruct]),
                ClusterObjectFieldDescriptor(Label="groupList", Tag=0x00000005, Type=typing.List[JointFabricDatastore.Structs.DatastoreGroupInformationEntryStruct]),
                ClusterObjectFieldDescriptor(Label="nodeList", Tag=0x00000006, Type=typing.List[JointFabricDatastore.Structs.DatastoreNodeInformationEntryStruct]),
                ClusterObjectFieldDescriptor(Label="adminList", Tag=0x00000007, Type=typing.List[JointFabricDatastore.Structs.DatastoreAdministratorInformationEntryStruct]),
                ClusterObjectFieldDescriptor(Label="status", Tag=0x00000008, Type=JointFabricDatastore.Structs.DatastoreStatusEntryStruct),
                ClusterObjectFieldDescriptor(Label="endpointGroupIDList", Tag=0x00000009, Type=typing.List[JointFabricDatastore.Structs.DatastoreEndpointGroupIDEntryStruct]),
                ClusterObjectFieldDescriptor(Label="endpointBindingList", Tag=0x0000000A, Type=typing.List[JointFabricDatastore.Structs.DatastoreEndpointBindingEntryStruct]),
                ClusterObjectFieldDescriptor(Label="nodeKeySetList", Tag=0x0000000B, Type=typing.List[JointFabricDatastore.Structs.DatastoreNodeKeySetEntryStruct]),
                ClusterObjectFieldDescriptor(Label="nodeAclList", Tag=0x0000000C, Type=typing.List[JointFabricDatastore.Structs.DatastoreACLEntryStruct]),
                ClusterObjectFieldDescriptor(Label="nodeEndpointList", Tag=0x0000000D, Type=typing.List[JointFabricDatastore.Structs.DatastoreEndpointEntryStruct]),
                ClusterObjectFieldDescriptor(Label="generatedCommandList", Tag=0x0000FFF8, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="acceptedCommandList", Tag=0x0000FFF9, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="attributeList", Tag=0x0000FFFB, Type=typing.List[uint]),
                ClusterObjectFieldDescriptor(Label="featureMap", Tag=0x0000FFFC, Type=uint),
                ClusterObjectFieldDescriptor(Label="clusterRevision", Tag=0x0000FFFD, Type=uint),
            ])

    anchorRootCa: bytes = b""
    anchorNodeID: uint = 0
    anchorVendorID: uint = 0
    friendlyName: str = ""
    groupKeySetList: typing.List[JointFabricDatastore.Structs.DatastoreGroupKeySetStruct] = field(default_factory=lambda: [])
    groupList: typing.List[JointFabricDatastore.Structs.DatastoreGroupInformationEntryStruct] = field(default_factory=lambda: [])
    nodeList: typing.List[JointFabricDatastore.Structs.DatastoreNodeInformationEntryStruct] = field(default_factory=lambda: [])
    adminList: typing.List[JointFabricDatastore.Structs.DatastoreAdministratorInformationEntryStruct] = field(default_factory=lambda: [])
    status: JointFabricDatastore.Structs.DatastoreStatusEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreStatusEntryStruct())
    endpointGroupIDList: typing.List[JointFabricDatastore.Structs.DatastoreEndpointGroupIDEntryStruct] = field(default_factory=lambda: [])
    endpointBindingList: typing.List[JointFabricDatastore.Structs.DatastoreEndpointBindingEntryStruct] = field(default_factory=lambda: [])
    nodeKeySetList: typing.List[JointFabricDatastore.Structs.DatastoreNodeKeySetEntryStruct] = field(default_factory=lambda: [])
    nodeAclList: typing.List[JointFabricDatastore.Structs.DatastoreACLEntryStruct] = field(default_factory=lambda: [])
    nodeEndpointList: typing.List[JointFabricDatastore.Structs.DatastoreEndpointEntryStruct] = field(default_factory=lambda: [])
    generatedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    acceptedCommandList: typing.List[uint] = field(default_factory=lambda: [])
    attributeList: typing.List[uint] = field(default_factory=lambda: [])
    featureMap: uint = 0
    clusterRevision: uint = 0

    class Enums:
        class DatastoreStateEnum(MatterIntEnum):
            kPending = 0x00
            kCommitted = 0x01
            kDeletePending = 0x02
            kCommitFailed = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class DatastoreAccessControlEntryPrivilegeEnum(MatterIntEnum):
            kView = 0x01
            kOperate = 0x03
            kManage = 0x04
            kAdminister = 0x05
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 6

        class DatastoreAccessControlEntryAuthModeEnum(MatterIntEnum):
            kPase = 0x01
            kCase = 0x02
            kGroup = 0x03
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 4

        class DatastoreGroupKeySecurityPolicyEnum(MatterIntEnum):
            kTrustFirst = 0x00
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 1

        class DatastoreGroupKeyMulticastPolicyEnum(MatterIntEnum):
            kPerGroupID = 0x00
            kAllNodes = 0x01
            # All received enum values that are not listed above will be mapped
            # to kUnknownEnumValue. This is a helper enum value that should only
            # be used by code to process how it handles receiving an unknown
            # enum value. This specific value should never be transmitted.
            kUnknownEnumValue = 2

    class Structs:
        @dataclass
        class DatastoreStatusEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="state", Tag=0, Type=JointFabricDatastore.Enums.DatastoreStateEnum),
                        ClusterObjectFieldDescriptor(Label="updateTimestamp", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="failureCode", Tag=2, Type=Globals.Enums.status),
                    ])

            state: JointFabricDatastore.Enums.DatastoreStateEnum = 0
            updateTimestamp: uint = 0
            failureCode: Globals.Enums.status = 0

        @dataclass
        class DatastoreNodeKeySetEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="groupKeySetID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="statusEntry", Tag=2, Type=JointFabricDatastore.Structs.DatastoreStatusEntryStruct),
                    ])

            nodeID: uint = 0
            groupKeySetID: uint = 0
            statusEntry: JointFabricDatastore.Structs.DatastoreStatusEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreStatusEntryStruct())

        @dataclass
        class DatastoreGroupInformationEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="groupKeySetID", Tag=2, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupCat", Tag=3, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupCatVersion", Tag=4, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupPermission", Tag=5, Type=JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum),
                    ])

            groupID: uint = 0
            friendlyName: str = ""
            groupKeySetID: typing.Union[Nullable, uint] = NullValue
            groupCat: typing.Union[Nullable, uint] = NullValue
            groupCatVersion: typing.Union[Nullable, uint] = NullValue
            groupPermission: JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum = 0

        @dataclass
        class DatastoreBindingTargetStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="node", Tag=1, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="group", Tag=2, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="endpoint", Tag=3, Type=typing.Optional[uint]),
                        ClusterObjectFieldDescriptor(Label="cluster", Tag=4, Type=typing.Optional[uint]),
                    ])

            node: typing.Optional[uint] = None
            group: typing.Optional[uint] = None
            endpoint: typing.Optional[uint] = None
            cluster: typing.Optional[uint] = None

        @dataclass
        class DatastoreEndpointBindingEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="listID", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="binding", Tag=3, Type=JointFabricDatastore.Structs.DatastoreBindingTargetStruct),
                        ClusterObjectFieldDescriptor(Label="statusEntry", Tag=4, Type=JointFabricDatastore.Structs.DatastoreStatusEntryStruct),
                    ])

            nodeID: uint = 0
            endpointID: uint = 0
            listID: uint = 0
            binding: JointFabricDatastore.Structs.DatastoreBindingTargetStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreBindingTargetStruct())
            statusEntry: JointFabricDatastore.Structs.DatastoreStatusEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreStatusEntryStruct())

        @dataclass
        class DatastoreEndpointGroupIDEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="statusEntry", Tag=3, Type=JointFabricDatastore.Structs.DatastoreStatusEntryStruct),
                    ])

            nodeID: uint = 0
            endpointID: uint = 0
            groupID: uint = 0
            statusEntry: JointFabricDatastore.Structs.DatastoreStatusEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreStatusEntryStruct())

        @dataclass
        class DatastoreEndpointEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=2, Type=str),
                    ])

            endpointID: uint = 0
            nodeID: uint = 0
            friendlyName: str = ""

        @dataclass
        class DatastoreAccessControlTargetStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="cluster", Tag=0, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="endpoint", Tag=1, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="deviceType", Tag=2, Type=typing.Union[Nullable, uint]),
                    ])

            cluster: typing.Union[Nullable, uint] = NullValue
            endpoint: typing.Union[Nullable, uint] = NullValue
            deviceType: typing.Union[Nullable, uint] = NullValue

        @dataclass
        class DatastoreAccessControlEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="privilege", Tag=1, Type=JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum),
                        ClusterObjectFieldDescriptor(Label="authMode", Tag=2, Type=JointFabricDatastore.Enums.DatastoreAccessControlEntryAuthModeEnum),
                        ClusterObjectFieldDescriptor(Label="subjects", Tag=3, Type=typing.Union[Nullable, typing.List[uint]]),
                        ClusterObjectFieldDescriptor(Label="targets", Tag=4, Type=typing.Union[Nullable, typing.List[JointFabricDatastore.Structs.DatastoreAccessControlTargetStruct]]),
                    ])

            privilege: JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum = 0
            authMode: JointFabricDatastore.Enums.DatastoreAccessControlEntryAuthModeEnum = 0
            subjects: typing.Union[Nullable, typing.List[uint]] = NullValue
            targets: typing.Union[Nullable, typing.List[JointFabricDatastore.Structs.DatastoreAccessControlTargetStruct]] = NullValue

        @dataclass
        class DatastoreACLEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="listID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="aclEntry", Tag=2, Type=JointFabricDatastore.Structs.DatastoreAccessControlEntryStruct),
                        ClusterObjectFieldDescriptor(Label="statusEntry", Tag=3, Type=JointFabricDatastore.Structs.DatastoreStatusEntryStruct),
                    ])

            nodeID: uint = 0
            listID: uint = 0
            aclEntry: JointFabricDatastore.Structs.DatastoreAccessControlEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreAccessControlEntryStruct())
            statusEntry: JointFabricDatastore.Structs.DatastoreStatusEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreStatusEntryStruct())

        @dataclass
        class DatastoreNodeInformationEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="commissioningStatusEntry", Tag=2, Type=JointFabricDatastore.Structs.DatastoreStatusEntryStruct),
                    ])

            nodeID: uint = 0
            friendlyName: str = ""
            commissioningStatusEntry: JointFabricDatastore.Structs.DatastoreStatusEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreStatusEntryStruct())

        @dataclass
        class DatastoreAdministratorInformationEntryStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="vendorID", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="icac", Tag=3, Type=bytes),
                    ])

            nodeID: uint = 0
            friendlyName: str = ""
            vendorID: uint = 0
            icac: bytes = b""

        @dataclass
        class DatastoreGroupKeySetStruct(ClusterObject):
            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupKeySetID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="groupKeySecurityPolicy", Tag=1, Type=JointFabricDatastore.Enums.DatastoreGroupKeySecurityPolicyEnum),
                        ClusterObjectFieldDescriptor(Label="epochKey0", Tag=2, Type=typing.Union[Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="epochStartTime0", Tag=3, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="epochKey1", Tag=4, Type=typing.Union[Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="epochStartTime1", Tag=5, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="epochKey2", Tag=6, Type=typing.Union[Nullable, bytes]),
                        ClusterObjectFieldDescriptor(Label="epochStartTime2", Tag=7, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupKeyMulticastPolicy", Tag=8, Type=typing.Optional[JointFabricDatastore.Enums.DatastoreGroupKeyMulticastPolicyEnum]),
                    ])

            groupKeySetID: uint = 0
            groupKeySecurityPolicy: JointFabricDatastore.Enums.DatastoreGroupKeySecurityPolicyEnum = 0
            epochKey0: typing.Union[Nullable, bytes] = NullValue
            epochStartTime0: typing.Union[Nullable, uint] = NullValue
            epochKey1: typing.Union[Nullable, bytes] = NullValue
            epochStartTime1: typing.Union[Nullable, uint] = NullValue
            epochKey2: typing.Union[Nullable, bytes] = NullValue
            epochStartTime2: typing.Union[Nullable, uint] = NullValue
            groupKeyMulticastPolicy: typing.Optional[JointFabricDatastore.Enums.DatastoreGroupKeyMulticastPolicyEnum] = None

    class Commands:
        @dataclass
        class AddKeySet(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000000
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupKeySet", Tag=0, Type=JointFabricDatastore.Structs.DatastoreGroupKeySetStruct),
                    ])

            groupKeySet: JointFabricDatastore.Structs.DatastoreGroupKeySetStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreGroupKeySetStruct())

        @dataclass
        class UpdateKeySet(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000001
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupKeySet", Tag=0, Type=JointFabricDatastore.Structs.DatastoreGroupKeySetStruct),
                    ])

            groupKeySet: JointFabricDatastore.Structs.DatastoreGroupKeySetStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreGroupKeySetStruct())

        @dataclass
        class RemoveKeySet(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000002
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupKeySetID", Tag=0, Type=uint),
                    ])

            groupKeySetID: uint = 0

        @dataclass
        class AddGroup(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000003
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="groupKeySetID", Tag=2, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupCat", Tag=3, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupCatVersion", Tag=4, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupPermission", Tag=5, Type=JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum),
                    ])

            groupID: uint = 0
            friendlyName: str = ""
            groupKeySetID: typing.Union[Nullable, uint] = NullValue
            groupCat: typing.Union[Nullable, uint] = NullValue
            groupCatVersion: typing.Union[Nullable, uint] = NullValue
            groupPermission: JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum = 0

        @dataclass
        class UpdateGroup(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000004
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=typing.Union[Nullable, str]),
                        ClusterObjectFieldDescriptor(Label="groupKeySetID", Tag=2, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupCat", Tag=3, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupCatVersion", Tag=4, Type=typing.Union[Nullable, uint]),
                        ClusterObjectFieldDescriptor(Label="groupPermission", Tag=5, Type=typing.Union[Nullable, JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum]),
                    ])

            groupID: uint = 0
            friendlyName: typing.Union[Nullable, str] = NullValue
            groupKeySetID: typing.Union[Nullable, uint] = NullValue
            groupCat: typing.Union[Nullable, uint] = NullValue
            groupCatVersion: typing.Union[Nullable, uint] = NullValue
            groupPermission: typing.Union[Nullable, JointFabricDatastore.Enums.DatastoreAccessControlEntryPrivilegeEnum] = NullValue

        @dataclass
        class RemoveGroup(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000005
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=0, Type=uint),
                    ])

            groupID: uint = 0

        @dataclass
        class AddAdmin(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000006
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                        ClusterObjectFieldDescriptor(Label="vendorID", Tag=2, Type=uint),
                        ClusterObjectFieldDescriptor(Label="icac", Tag=3, Type=bytes),
                    ])

            nodeID: uint = 0
            friendlyName: str = ""
            vendorID: uint = 0
            icac: bytes = b""

        @dataclass
        class UpdateAdmin(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000007
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=typing.Optional[str]),
                        ClusterObjectFieldDescriptor(Label="icac", Tag=2, Type=typing.Optional[bytes]),
                    ])

            nodeID: uint = 0
            friendlyName: typing.Optional[str] = None
            icac: typing.Optional[bytes] = None

        @dataclass
        class RemoveAdmin(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000008
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                    ])

            nodeID: uint = 0

        @dataclass
        class AddPendingNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000009
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                    ])

            nodeID: uint = 0
            friendlyName: str = ""

        @dataclass
        class RefreshNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x0000000A
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                    ])

            nodeID: uint = 0

        @dataclass
        class UpdateNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x0000000B
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=1, Type=str),
                    ])

            nodeID: uint = 0
            friendlyName: str = ""

        @dataclass
        class RemoveNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x0000000C
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                    ])

            nodeID: uint = 0

        @dataclass
        class UpdateEndpointForNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x0000000D
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="friendlyName", Tag=2, Type=str),
                    ])

            endpointID: uint = 0
            nodeID: uint = 0
            friendlyName: str = ""

        @dataclass
        class AddGroupIDToEndpointForNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x0000000E
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=2, Type=uint),
                    ])

            nodeID: uint = 0
            endpointID: uint = 0
            groupID: uint = 0

        @dataclass
        class RemoveGroupIDFromEndpointForNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x0000000F
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="groupID", Tag=2, Type=uint),
                    ])

            nodeID: uint = 0
            endpointID: uint = 0
            groupID: uint = 0

        @dataclass
        class AddBindingToEndpointForNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000010
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="binding", Tag=2, Type=JointFabricDatastore.Structs.DatastoreBindingTargetStruct),
                    ])

            nodeID: uint = 0
            endpointID: uint = 0
            binding: JointFabricDatastore.Structs.DatastoreBindingTargetStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreBindingTargetStruct())

        @dataclass
        class RemoveBindingFromEndpointForNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000011
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="listID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="endpointID", Tag=1, Type=uint),
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=2, Type=uint),
                    ])

            listID: uint = 0
            endpointID: uint = 0
            nodeID: uint = 0

        @dataclass
        class AddACLToNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000012
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="aclEntry", Tag=1, Type=JointFabricDatastore.Structs.DatastoreAccessControlEntryStruct),
                    ])

            nodeID: uint = 0
            aclEntry: JointFabricDatastore.Structs.DatastoreAccessControlEntryStruct = field(default_factory=lambda: JointFabricDatastore.Structs.DatastoreAccessControlEntryStruct())

        @dataclass
        class RemoveACLFromNode(ClusterCommand):
            cluster_id: typing.ClassVar[int] = 0x00000752
            command_id: typing.ClassVar[int] = 0x00000013
            is_client: typing.ClassVar[bool] = True
            response_type: typing.ClassVar[typing.Optional[str]] = None

            @ChipUtility.classproperty
            def descriptor(cls) -> ClusterObjectDescriptor:
                return ClusterObjectDescriptor(
                    Fields=[
                        ClusterObjectFieldDescriptor(Label="listID", Tag=0, Type=uint),
                        ClusterObjectFieldDescriptor(Label="nodeID", Tag=1, Type=uint),
                    ])

            listID: uint = 0
            nodeID: uint = 0

    class Attributes:
        AnchorRootCA = _attr(__module__, __qualname__, "AnchorRootCA", 0x00000752, 0x00000000, "bytes", b"")

        AnchorNodeID = _attr(__module__, __qualname__, "AnchorNodeID", 0x00000752, 0x00000001, "uint", 0)

        AnchorVendorID = _attr(__module__, __qualname__, "AnchorVendorID", 0x00000752, 0x00000002, "uint", 0)

        FriendlyName = _attr(__module__, __qualname__, "FriendlyName", 0x00000752, 0x00000003, "str", "")

        GroupKeySetList = _attr(__module__, __qualname__, "GroupKeySetList", 0x00000752, 0x00000004, "typing.List[JointFabricDatastore.Structs.DatastoreGroupKeySetStruct]", None, "[]")

        GroupList = _attr(__module__, __qualname__, "GroupList", 0x00000752, 0x00000005, "typing.List[JointFabricDatastore.Structs.DatastoreGroupInformationEntryStruct]", None, "[]")

        NodeList = _attr(__module__, __qualname__, "NodeList", 0x00000752, 0x00000006, "typing.List[JointFabricDatastore.Structs.DatastoreNodeInformationEntryStruct]", None, "[]")

        AdminList = _attr(__module__, __qualname__, "AdminList", 0x00000752, 0x00000007, "typing.List[JointFabricDatastore.Structs.DatastoreAdministratorInformationEntryStruct]", None, "[]")

        Status = _attr(__module__, __qualname__, "Status", 0x00000752, 0x00000008, "JointFabricDatastore.Structs.DatastoreStatusEntryStruct", None, "JointFabricDatastore.Structs.DatastoreStatusEntryStruct()")

        EndpointGroupIDList = _attr(__module__, __qualname__, "EndpointGroupIDList", 0x00000752, 0x00000009, "typing.List[JointFabricDatastore.Structs.DatastoreEndpointGroupIDEntryStruct]", None, "[]")

        EndpointBindingList = _attr(__module__, __qualname__, "EndpointBindingList", 0x00000752, 0x0000000A, "typing.List[JointFabricDatastore.Structs.DatastoreEndpointBindingEntryStruct]", None, "[]")

        NodeKeySetList = _attr(__module__, __qualname__, "NodeKeySetList", 0x00000752, 0x0000000B, "typing.List[JointFabricDatastore.Structs.DatastoreNodeKeySetEntryStruct]", None, "[]")

        NodeACLList = _attr(__module__, __qualname__, "NodeACLList", 0x00000752, 0x0000000C, "typing.List[JointFabricDatastore.Structs.DatastoreACLEntryStruct]", None, "[]")

        NodeEndpointList = _attr(__module__, __qualname__, "NodeEndpointList", 0x00000752, 0x0000000D, "typing.List[JointFabricDatastore.Structs.DatastoreEndpointEntryStruct]", None, "[]")

        GeneratedCommandList = _attr(__module__, __qualname__, "GeneratedCommandList", 0x00000752, 0x0000FFF8, "typing.List[uint]", None, "[]")

        AcceptedCommandList = _attr(__module__, __qualname__, "AcceptedCommandList", 0x00000752, 0x0000FFF9, "typing.List[uint]", None, "[]")

        AttributeList = _attr(__module__, __qualname__, "AttributeList", 0x00000752, 0x0000FFFB, "typing.List[uint]", None, "[]")

        FeatureMap = _attr(__module__, __qualname__, "FeatureMap", 0x00000752, 0x0000FFFC, "uint", 0)

        ClusterRevision = _attr(__module__, __qualname__, "ClusterRevision", 0x00000752, 0x0000FFFD, "uint", 0)
