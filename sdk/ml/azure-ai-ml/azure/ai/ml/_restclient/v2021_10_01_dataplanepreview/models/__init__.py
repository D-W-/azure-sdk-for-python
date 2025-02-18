# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccountKeyDatastoreCredentials
    from ._models_py3 import AccountKeyDatastoreSecrets
    from ._models_py3 import AcrDetail
    from ._models_py3 import AmlToken
    from ._models_py3 import AnonymousAccessCredentialDto
    from ._models_py3 import AssetBase
    from ._models_py3 import AssetContainer
    from ._models_py3 import AssetReferenceBase
    from ._models_py3 import AzureBlobDatastore
    from ._models_py3 import AzureDataLakeGen1Datastore
    from ._models_py3 import AzureDataLakeGen2Datastore
    from ._models_py3 import AzureFileDatastore
    from ._models_py3 import BanditPolicy
    from ._models_py3 import BasicBinding
    from ._models_py3 import Binding
    from ._models_py3 import BlobReferenceForConsumptionDto
    from ._models_py3 import BlobReferenceSASRequestDto
    from ._models_py3 import BlobReferenceSASResponseDto
    from ._models_py3 import BuildContext
    from ._models_py3 import CertificateDatastoreCredentials
    from ._models_py3 import CertificateDatastoreSecrets
    from ._models_py3 import CodeContainerData
    from ._models_py3 import CodeContainerDetails
    from ._models_py3 import CodeContainerResourceArmPaginatedResult
    from ._models_py3 import CodeVersionData
    from ._models_py3 import CodeVersionDetails
    from ._models_py3 import CodeVersionResourceArmPaginatedResult
    from ._models_py3 import CommandJob
    from ._models_py3 import CommandJobLimits
    from ._models_py3 import ComponentContainerData
    from ._models_py3 import ComponentContainerDetails
    from ._models_py3 import ComponentContainerResourceArmPaginatedResult
    from ._models_py3 import ComponentJob
    from ._models_py3 import ComponentVersionData
    from ._models_py3 import ComponentVersionDetails
    from ._models_py3 import ComponentVersionResourceArmPaginatedResult
    from ._models_py3 import DataContainerData
    from ._models_py3 import DataContainerDetails
    from ._models_py3 import DataContainerResourceArmPaginatedResult
    from ._models_py3 import DataPathAssetReference
    from ._models_py3 import DataReferenceCredentialDto
    from ._models_py3 import DataVersionBaseData
    from ._models_py3 import DataVersionBaseDetails
    from ._models_py3 import DataVersionBaseResourceArmPaginatedResult
    from ._models_py3 import Datastore
    from ._models_py3 import DatastoreCredentials
    from ._models_py3 import DatastoreSecrets
    from ._models_py3 import DistributionConfiguration
    from ._models_py3 import DockerCredentialDto
    from ._models_py3 import EarlyTerminationPolicy
    from ._models_py3 import EnvironmentContainerData
    from ._models_py3 import EnvironmentContainerDetails
    from ._models_py3 import EnvironmentContainerResourceArmPaginatedResult
    from ._models_py3 import EnvironmentVersionData
    from ._models_py3 import EnvironmentVersionDetails
    from ._models_py3 import EnvironmentVersionResourceArmPaginatedResult
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import FlavorData
    from ._models_py3 import IdAssetReference
    from ._models_py3 import IdentityConfiguration
    from ._models_py3 import ImageReferenceForConsumptionDto
    from ._models_py3 import InferenceContainerProperties
    from ._models_py3 import IntellectualProperty
    from ._models_py3 import Job
    from ._models_py3 import JobBase
    from ._models_py3 import JobInput
    from ._models_py3 import JobInputDataset
    from ._models_py3 import JobInputLiteral
    from ._models_py3 import JobInputUri
    from ._models_py3 import JobLimits
    from ._models_py3 import JobOutput
    from ._models_py3 import JobOutputDataset
    from ._models_py3 import JobOutputUri
    from ._models_py3 import JobService
    from ._models_py3 import MLTableData
    from ._models_py3 import ManagedIdentity
    from ._models_py3 import ManagedIdentityCredentialDto
    from ._models_py3 import MedianStoppingPolicy
    from ._models_py3 import ModelContainerData
    from ._models_py3 import ModelContainerDetails
    from ._models_py3 import ModelContainerResourceArmPaginatedResult
    from ._models_py3 import ModelVersionData
    from ._models_py3 import ModelVersionDetails
    from ._models_py3 import ModelVersionResourceArmPaginatedResult
    from ._models_py3 import Mpi
    from ._models_py3 import NoneDatastoreCredentials
    from ._models_py3 import Objective
    from ._models_py3 import OutputPathAssetReference
    from ._models_py3 import PipelineJob
    from ._models_py3 import PyTorch
    from ._models_py3 import Resource
    from ._models_py3 import ResourceBase
    from ._models_py3 import ResourceConfiguration
    from ._models_py3 import ResourceManagementAssetReferenceData
    from ._models_py3 import ResourceManagementAssetReferenceDetails
    from ._models_py3 import Route
    from ._models_py3 import SASCredentialDto
    from ._models_py3 import SasDatastoreCredentials
    from ._models_py3 import SasDatastoreSecrets
    from ._models_py3 import ServicePrincipalDatastoreCredentials
    from ._models_py3 import ServicePrincipalDatastoreSecrets
    from ._models_py3 import SweepJob
    from ._models_py3 import SweepJobLimits
    from ._models_py3 import SystemData
    from ._models_py3 import TemporaryDataReferenceRequestDto
    from ._models_py3 import TemporaryDataReferenceResponseDto
    from ._models_py3 import TensorFlow
    from ._models_py3 import TrialComponent
    from ._models_py3 import TruncationSelectionPolicy
    from ._models_py3 import UriFileDataVersion
    from ._models_py3 import UriFolderDataVersion
    from ._models_py3 import UriReference
except (SyntaxError, ImportError):
    from ._models import AccountKeyDatastoreCredentials  # type: ignore
    from ._models import AccountKeyDatastoreSecrets  # type: ignore
    from ._models import AcrDetail  # type: ignore
    from ._models import AmlToken  # type: ignore
    from ._models import AnonymousAccessCredentialDto  # type: ignore
    from ._models import AssetBase  # type: ignore
    from ._models import AssetContainer  # type: ignore
    from ._models import AssetReferenceBase  # type: ignore
    from ._models import AzureBlobDatastore  # type: ignore
    from ._models import AzureDataLakeGen1Datastore  # type: ignore
    from ._models import AzureDataLakeGen2Datastore  # type: ignore
    from ._models import AzureFileDatastore  # type: ignore
    from ._models import BanditPolicy  # type: ignore
    from ._models import BasicBinding  # type: ignore
    from ._models import Binding  # type: ignore
    from ._models import BlobReferenceForConsumptionDto  # type: ignore
    from ._models import BlobReferenceSASRequestDto  # type: ignore
    from ._models import BlobReferenceSASResponseDto  # type: ignore
    from ._models import BuildContext  # type: ignore
    from ._models import CertificateDatastoreCredentials  # type: ignore
    from ._models import CertificateDatastoreSecrets  # type: ignore
    from ._models import CodeContainerData  # type: ignore
    from ._models import CodeContainerDetails  # type: ignore
    from ._models import CodeContainerResourceArmPaginatedResult  # type: ignore
    from ._models import CodeVersionData  # type: ignore
    from ._models import CodeVersionDetails  # type: ignore
    from ._models import CodeVersionResourceArmPaginatedResult  # type: ignore
    from ._models import CommandJob  # type: ignore
    from ._models import CommandJobLimits  # type: ignore
    from ._models import ComponentContainerData  # type: ignore
    from ._models import ComponentContainerDetails  # type: ignore
    from ._models import ComponentContainerResourceArmPaginatedResult  # type: ignore
    from ._models import ComponentJob  # type: ignore
    from ._models import ComponentVersionData  # type: ignore
    from ._models import ComponentVersionDetails  # type: ignore
    from ._models import ComponentVersionResourceArmPaginatedResult  # type: ignore
    from ._models import DataContainerData  # type: ignore
    from ._models import DataContainerDetails  # type: ignore
    from ._models import DataContainerResourceArmPaginatedResult  # type: ignore
    from ._models import DataPathAssetReference  # type: ignore
    from ._models import DataReferenceCredentialDto  # type: ignore
    from ._models import DataVersionBaseData  # type: ignore
    from ._models import DataVersionBaseDetails  # type: ignore
    from ._models import DataVersionBaseResourceArmPaginatedResult  # type: ignore
    from ._models import Datastore  # type: ignore
    from ._models import DatastoreCredentials  # type: ignore
    from ._models import DatastoreSecrets  # type: ignore
    from ._models import DistributionConfiguration  # type: ignore
    from ._models import DockerCredentialDto  # type: ignore
    from ._models import EarlyTerminationPolicy  # type: ignore
    from ._models import EnvironmentContainerData  # type: ignore
    from ._models import EnvironmentContainerDetails  # type: ignore
    from ._models import EnvironmentContainerResourceArmPaginatedResult  # type: ignore
    from ._models import EnvironmentVersionData  # type: ignore
    from ._models import EnvironmentVersionDetails  # type: ignore
    from ._models import EnvironmentVersionResourceArmPaginatedResult  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import FlavorData  # type: ignore
    from ._models import IdAssetReference  # type: ignore
    from ._models import IdentityConfiguration  # type: ignore
    from ._models import ImageReferenceForConsumptionDto  # type: ignore
    from ._models import InferenceContainerProperties  # type: ignore
    from ._models import IntellectualProperty  # type: ignore
    from ._models import Job  # type: ignore
    from ._models import JobBase  # type: ignore
    from ._models import JobInput  # type: ignore
    from ._models import JobInputDataset  # type: ignore
    from ._models import JobInputLiteral  # type: ignore
    from ._models import JobInputUri  # type: ignore
    from ._models import JobLimits  # type: ignore
    from ._models import JobOutput  # type: ignore
    from ._models import JobOutputDataset  # type: ignore
    from ._models import JobOutputUri  # type: ignore
    from ._models import JobService  # type: ignore
    from ._models import MLTableData  # type: ignore
    from ._models import ManagedIdentity  # type: ignore
    from ._models import ManagedIdentityCredentialDto  # type: ignore
    from ._models import MedianStoppingPolicy  # type: ignore
    from ._models import ModelContainerData  # type: ignore
    from ._models import ModelContainerDetails  # type: ignore
    from ._models import ModelContainerResourceArmPaginatedResult  # type: ignore
    from ._models import ModelVersionData  # type: ignore
    from ._models import ModelVersionDetails  # type: ignore
    from ._models import ModelVersionResourceArmPaginatedResult  # type: ignore
    from ._models import Mpi  # type: ignore
    from ._models import NoneDatastoreCredentials  # type: ignore
    from ._models import Objective  # type: ignore
    from ._models import OutputPathAssetReference  # type: ignore
    from ._models import PipelineJob  # type: ignore
    from ._models import PyTorch  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceBase  # type: ignore
    from ._models import ResourceConfiguration  # type: ignore
    from ._models import ResourceManagementAssetReferenceData  # type: ignore
    from ._models import ResourceManagementAssetReferenceDetails  # type: ignore
    from ._models import Route  # type: ignore
    from ._models import SASCredentialDto  # type: ignore
    from ._models import SasDatastoreCredentials  # type: ignore
    from ._models import SasDatastoreSecrets  # type: ignore
    from ._models import ServicePrincipalDatastoreCredentials  # type: ignore
    from ._models import ServicePrincipalDatastoreSecrets  # type: ignore
    from ._models import SweepJob  # type: ignore
    from ._models import SweepJobLimits  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TemporaryDataReferenceRequestDto  # type: ignore
    from ._models import TemporaryDataReferenceResponseDto  # type: ignore
    from ._models import TensorFlow  # type: ignore
    from ._models import TrialComponent  # type: ignore
    from ._models import TruncationSelectionPolicy  # type: ignore
    from ._models import UriFileDataVersion  # type: ignore
    from ._models import UriFolderDataVersion  # type: ignore
    from ._models import UriReference  # type: ignore

from ._azure_machine_learning_workspaces_enums import (
    BindingType,
    CreatedByType,
    CredentialsType,
    DataReferenceCredentialType,
    DataType,
    DatastoreType,
    DistributionType,
    EarlyTerminationPolicyType,
    EnvironmentType,
    Goal,
    IdentityConfigurationType,
    InputDataDeliveryMode,
    JobInputType,
    JobLimitsType,
    JobOutputType,
    JobStatus,
    JobType,
    ListViewType,
    OperatingSystemType,
    OutputDataDeliveryMode,
    ProtectionLevel,
    ReferenceType,
    SamplingAlgorithm,
    SecretsType,
    ServiceDataAccessAuthIdentity,
)

__all__ = [
    'AccountKeyDatastoreCredentials',
    'AccountKeyDatastoreSecrets',
    'AcrDetail',
    'AmlToken',
    'AnonymousAccessCredentialDto',
    'AssetBase',
    'AssetContainer',
    'AssetReferenceBase',
    'AzureBlobDatastore',
    'AzureDataLakeGen1Datastore',
    'AzureDataLakeGen2Datastore',
    'AzureFileDatastore',
    'BanditPolicy',
    'BasicBinding',
    'Binding',
    'BlobReferenceForConsumptionDto',
    'BlobReferenceSASRequestDto',
    'BlobReferenceSASResponseDto',
    'BuildContext',
    'CertificateDatastoreCredentials',
    'CertificateDatastoreSecrets',
    'CodeContainerData',
    'CodeContainerDetails',
    'CodeContainerResourceArmPaginatedResult',
    'CodeVersionData',
    'CodeVersionDetails',
    'CodeVersionResourceArmPaginatedResult',
    'CommandJob',
    'CommandJobLimits',
    'ComponentContainerData',
    'ComponentContainerDetails',
    'ComponentContainerResourceArmPaginatedResult',
    'ComponentJob',
    'ComponentVersionData',
    'ComponentVersionDetails',
    'ComponentVersionResourceArmPaginatedResult',
    'DataContainerData',
    'DataContainerDetails',
    'DataContainerResourceArmPaginatedResult',
    'DataPathAssetReference',
    'DataReferenceCredentialDto',
    'DataVersionBaseData',
    'DataVersionBaseDetails',
    'DataVersionBaseResourceArmPaginatedResult',
    'Datastore',
    'DatastoreCredentials',
    'DatastoreSecrets',
    'DistributionConfiguration',
    'DockerCredentialDto',
    'EarlyTerminationPolicy',
    'EnvironmentContainerData',
    'EnvironmentContainerDetails',
    'EnvironmentContainerResourceArmPaginatedResult',
    'EnvironmentVersionData',
    'EnvironmentVersionDetails',
    'EnvironmentVersionResourceArmPaginatedResult',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'FlavorData',
    'IdAssetReference',
    'IdentityConfiguration',
    'ImageReferenceForConsumptionDto',
    'InferenceContainerProperties',
    'IntellectualProperty',
    'Job',
    'JobBase',
    'JobInput',
    'JobInputDataset',
    'JobInputLiteral',
    'JobInputUri',
    'JobLimits',
    'JobOutput',
    'JobOutputDataset',
    'JobOutputUri',
    'JobService',
    'MLTableData',
    'ManagedIdentity',
    'ManagedIdentityCredentialDto',
    'MedianStoppingPolicy',
    'ModelContainerData',
    'ModelContainerDetails',
    'ModelContainerResourceArmPaginatedResult',
    'ModelVersionData',
    'ModelVersionDetails',
    'ModelVersionResourceArmPaginatedResult',
    'Mpi',
    'NoneDatastoreCredentials',
    'Objective',
    'OutputPathAssetReference',
    'PipelineJob',
    'PyTorch',
    'Resource',
    'ResourceBase',
    'ResourceConfiguration',
    'ResourceManagementAssetReferenceData',
    'ResourceManagementAssetReferenceDetails',
    'Route',
    'SASCredentialDto',
    'SasDatastoreCredentials',
    'SasDatastoreSecrets',
    'ServicePrincipalDatastoreCredentials',
    'ServicePrincipalDatastoreSecrets',
    'SweepJob',
    'SweepJobLimits',
    'SystemData',
    'TemporaryDataReferenceRequestDto',
    'TemporaryDataReferenceResponseDto',
    'TensorFlow',
    'TrialComponent',
    'TruncationSelectionPolicy',
    'UriFileDataVersion',
    'UriFolderDataVersion',
    'UriReference',
    'BindingType',
    'CreatedByType',
    'CredentialsType',
    'DataReferenceCredentialType',
    'DataType',
    'DatastoreType',
    'DistributionType',
    'EarlyTerminationPolicyType',
    'EnvironmentType',
    'Goal',
    'IdentityConfigurationType',
    'InputDataDeliveryMode',
    'JobInputType',
    'JobLimitsType',
    'JobOutputType',
    'JobStatus',
    'JobType',
    'ListViewType',
    'OperatingSystemType',
    'OutputDataDeliveryMode',
    'ProtectionLevel',
    'ReferenceType',
    'SamplingAlgorithm',
    'SecretsType',
    'ServiceDataAccessAuthIdentity',
]
