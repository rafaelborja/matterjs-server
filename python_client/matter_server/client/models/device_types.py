"""
Device type definitions.

This file is auto-generated, DO NOT edit.
"""

from __future__ import annotations

from chip.clusters import Objects as all_clusters
from chip.clusters.ClusterObjects import Cluster


class _LazyClusterSet:
    """The set of cluster classes, resolved from their names on first read."""

    __slots__ = ("_names", "_value")

    def __init__(self, names: tuple[str, ...]) -> None:
        self._names = names
        self._value: set[type[Cluster]] | None = None

    def __get__(self, obj: object, owner: type | None = None) -> set[type[Cluster]]:
        if self._value is None:
            self._value = {getattr(all_clusters, n) for n in self._names}
        return self._value


ALL_TYPES: dict[int, type[DeviceType]] = {}


class DeviceType:
    """Base class for Matter device types."""

    device_type: int = 0
    clusters: set[type[Cluster]] = set()

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        if cls.device_type != 0:
            ALL_TYPES[cls.device_type] = cls


class Aggregator(DeviceType):
    device_type: int = 0x000E
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Actions",
            "CommissionerControl",
            "Descriptor",
            "Identify",
        )
    )


class AirPurifier(DeviceType):
    device_type: int = 0x002D
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ActivatedCarbonFilterMonitoring",
            "Descriptor",
            "FanControl",
            "Groups",
            "HepaFilterMonitoring",
            "Identify",
            "OnOff",
        )
    )


class AirQualitySensor(DeviceType):
    device_type: int = 0x002C
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "AirQuality",
            "CarbonDioxideConcentrationMeasurement",
            "CarbonMonoxideConcentrationMeasurement",
            "Descriptor",
            "FormaldehydeConcentrationMeasurement",
            "Identify",
            "NitrogenDioxideConcentrationMeasurement",
            "OzoneConcentrationMeasurement",
            "Pm10ConcentrationMeasurement",
            "Pm1ConcentrationMeasurement",
            "Pm25ConcentrationMeasurement",
            "RadonConcentrationMeasurement",
            "RelativeHumidityMeasurement",
            "TemperatureMeasurement",
            "TotalVolatileOrganicCompoundsConcentrationMeasurement",
        )
    )


class AudioDoorbell(DeviceType):
    device_type: int = 0x0141
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CameraAvStreamManagement",
            "Descriptor",
            "Identify",
            "PushAvStreamTransport",
            "Switch",
            "WebRtcTransportProvider",
            "WebRtcTransportRequestor",
        )
    )


class BasicVideoPlayer(DeviceType):
    device_type: int = 0x0028
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "AudioOutput",
            "Channel",
            "ContentControl",
            "Descriptor",
            "KeypadInput",
            "LowPower",
            "MediaInput",
            "MediaPlayback",
            "Messages",
            "OnOff",
            "TargetNavigator",
            "WakeOnLan",
        )
    )


class BatteryStorage(DeviceType):
    device_type: int = 0x0018
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class BridgedNode(DeviceType):
    device_type: int = 0x0013
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "AdministratorCommissioning",
            "BridgedDeviceBasicInformation",
            "Descriptor",
            "EcosystemInformation",
            "PowerSource",
            "PowerSourceConfiguration",
        )
    )


class CameraController(DeviceType):
    device_type: int = 0x0147
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "WebRtcTransportRequestor",
        )
    )


class Camera(DeviceType):
    device_type: int = 0x0142
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CameraAvSettingsUserLevelManagement",
            "CameraAvStreamManagement",
            "Descriptor",
            "Identify",
            "OccupancySensing",
            "PushAvStreamTransport",
            "WebRtcTransportProvider",
            "WebRtcTransportRequestor",
            "ZoneManagement",
        )
    )


class CastingVideoClient(DeviceType):
    device_type: int = 0x0029
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ContentAppObserver",
            "Descriptor",
        )
    )


class CastingVideoPlayer(DeviceType):
    device_type: int = 0x0023
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "AccountLogin",
            "ApplicationLauncher",
            "AudioOutput",
            "Channel",
            "ContentControl",
            "ContentLauncher",
            "Descriptor",
            "KeypadInput",
            "LowPower",
            "MediaInput",
            "MediaPlayback",
            "Messages",
            "OnOff",
            "TargetNavigator",
            "WakeOnLan",
        )
    )


class Chime(DeviceType):
    device_type: int = 0x0146
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Chime",
            "Descriptor",
            "Identify",
        )
    )


class ClosureController(DeviceType):
    device_type: int = 0x023E
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
        )
    )


class Closure(DeviceType):
    device_type: int = 0x0230
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ClosureControl",
            "ClosureDimension",
            "Descriptor",
            "Identify",
            "WindowCovering",
        )
    )


class ClosurePanel(DeviceType):
    device_type: int = 0x0231
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ClosureControl",
            "ClosureDimension",
            "Descriptor",
            "WindowCovering",
        )
    )


class ColorDimmerSwitch(DeviceType):
    device_type: int = 0x0105
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class ColorTemperatureLight(DeviceType):
    device_type: int = 0x010C
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ColorControl",
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class ContactSensor(DeviceType):
    device_type: int = 0x0015
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "BooleanState",
            "BooleanStateConfiguration",
            "Descriptor",
            "Identify",
        )
    )


class ContentApp(DeviceType):
    device_type: int = 0x0024
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "AccountLogin",
            "ApplicationBasic",
            "ApplicationLauncher",
            "Channel",
            "ContentLauncher",
            "Descriptor",
            "KeypadInput",
            "MediaPlayback",
            "TargetNavigator",
        )
    )


class ControlBridge(DeviceType):
    device_type: int = 0x0840
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class CookSurface(DeviceType):
    device_type: int = 0x0077
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "OnOff",
            "TemperatureControl",
            "TemperatureMeasurement",
        )
    )


class Cooktop(DeviceType):
    device_type: int = 0x0078
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "OnOff",
        )
    )


class DeviceEnergyManagement(DeviceType):
    device_type: int = 0x050D
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "DeviceEnergyManagement",
            "DeviceEnergyManagementMode",
        )
    )


class DimmableLight(DeviceType):
    device_type: int = 0x0101
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class DimmablePlugInUnit(DeviceType):
    device_type: int = 0x010B
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class DimmerSwitch(DeviceType):
    device_type: int = 0x0104
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class Dishwasher(DeviceType):
    device_type: int = 0x0075
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "DishwasherAlarm",
            "DishwasherMode",
            "Identify",
            "OnOff",
            "OperationalState",
            "TemperatureControl",
        )
    )


class DoorLockController(DeviceType):
    device_type: int = 0x000B
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
        )
    )


class DoorLock(DeviceType):
    device_type: int = 0x000A
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "DoorLock",
            "Groups",
            "Identify",
            "ScenesManagement",
        )
    )


class Doorbell(DeviceType):
    device_type: int = 0x0148
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "Switch",
        )
    )


class ElectricalEnergyTariff(DeviceType):
    device_type: int = 0x0513
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CommodityPrice",
            "CommodityTariff",
            "Descriptor",
            "ElectricalGridConditions",
        )
    )


class ElectricalMeter(DeviceType):
    device_type: int = 0x0514
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CommodityMetering",
            "Descriptor",
            "ElectricalEnergyMeasurement",
            "ElectricalPowerMeasurement",
        )
    )


class ElectricalSensor(DeviceType):
    device_type: int = 0x0510
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "ElectricalEnergyMeasurement",
            "ElectricalPowerMeasurement",
            "PowerTopology",
        )
    )


class ElectricalUtilityMeter(DeviceType):
    device_type: int = 0x0511
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "MeterIdentification",
        )
    )


class EnergyEvse(DeviceType):
    device_type: int = 0x050C
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "EnergyEvse",
            "EnergyEvseMode",
            "Identify",
            "TemperatureMeasurement",
        )
    )


class ExtendedColorLight(DeviceType):
    device_type: int = 0x010D
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ColorControl",
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class ExtractorHood(DeviceType):
    device_type: int = 0x007A
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ActivatedCarbonFilterMonitoring",
            "Descriptor",
            "FanControl",
            "HepaFilterMonitoring",
            "Identify",
        )
    )


class Fan(DeviceType):
    device_type: int = 0x002B
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "FanControl",
            "Groups",
            "Identify",
            "OnOff",
        )
    )


class FloodlightCamera(DeviceType):
    device_type: int = 0x0144
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
        )
    )


class FlowSensor(DeviceType):
    device_type: int = 0x0306
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "FlowMeasurement",
            "Identify",
        )
    )


class GenericSwitch(DeviceType):
    device_type: int = 0x000F
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "Switch",
        )
    )


class HeatPump(DeviceType):
    device_type: int = 0x0309
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class HumiditySensor(DeviceType):
    device_type: int = 0x0307
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "RelativeHumidityMeasurement",
        )
    )


class Intercom(DeviceType):
    device_type: int = 0x0140
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CameraAvSettingsUserLevelManagement",
            "CameraAvStreamManagement",
            "Descriptor",
            "Identify",
            "WebRtcTransportProvider",
            "WebRtcTransportRequestor",
        )
    )


class IrrigationSystem(DeviceType):
    device_type: int = 0x0040
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "FlowMeasurement",
            "Identify",
            "OperationalState",
        )
    )


class JointFabricAdministrator(DeviceType):
    device_type: int = 0x0130
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "JointFabricAdministrator",
            "JointFabricDatastore",
        )
    )


class LaundryDryer(DeviceType):
    device_type: int = 0x007C
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "LaundryDryerControls",
            "LaundryWasherMode",
            "OnOff",
            "OperationalState",
            "TemperatureControl",
        )
    )


class LaundryWasher(DeviceType):
    device_type: int = 0x0073
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "LaundryWasherControls",
            "LaundryWasherMode",
            "OnOff",
            "OperationalState",
            "TemperatureControl",
        )
    )


class LightSensor(DeviceType):
    device_type: int = 0x0106
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "IlluminanceMeasurement",
        )
    )


class MeterReferencePoint(DeviceType):
    device_type: int = 0x0512
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class MicrowaveOven(DeviceType):
    device_type: int = 0x0079
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "FanControl",
            "Identify",
            "MicrowaveOvenControl",
            "MicrowaveOvenMode",
            "OperationalState",
        )
    )


class ModeSelect(DeviceType):
    device_type: int = 0x0027
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "ModeSelect",
        )
    )


class MountedDimmableLoadControl(DeviceType):
    device_type: int = 0x0110
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class MountedOnOffControl(DeviceType):
    device_type: int = 0x010F
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class NetworkInfrastructureManager(DeviceType):
    device_type: int = 0x0090
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "ThreadBorderRouterManagement",
            "ThreadNetworkDiagnostics",
            "ThreadNetworkDirectory",
            "WiFiNetworkManagement",
        )
    )


class OccupancySensor(DeviceType):
    device_type: int = 0x0107
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "BooleanStateConfiguration",
            "Descriptor",
            "Identify",
            "OccupancySensing",
        )
    )


class OnOffLight(DeviceType):
    device_type: int = 0x0100
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class OnOffLightSwitch(DeviceType):
    device_type: int = 0x0103
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class OnOffPlugInUnit(DeviceType):
    device_type: int = 0x010A
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "ScenesManagement",
        )
    )


class OnOffSensor(DeviceType):
    device_type: int = 0x0850
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class OtaProvider(DeviceType):
    device_type: int = 0x0014
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "OtaSoftwareUpdateProvider",
        )
    )


class OtaRequestor(DeviceType):
    device_type: int = 0x0012
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "OtaSoftwareUpdateRequestor",
        )
    )


class Oven(DeviceType):
    device_type: int = 0x007B
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class PowerSource(DeviceType):
    device_type: int = 0x0011
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "PowerSource",
        )
    )


class PressureSensor(DeviceType):
    device_type: int = 0x0305
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "PressureMeasurement",
        )
    )


class PumpController(DeviceType):
    device_type: int = 0x0304
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class Pump(DeviceType):
    device_type: int = 0x0303
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "FlowMeasurement",
            "Groups",
            "Identify",
            "LevelControl",
            "OnOff",
            "PressureMeasurement",
            "PumpConfigurationAndControl",
            "ScenesManagement",
            "TemperatureMeasurement",
        )
    )


class RainSensor(DeviceType):
    device_type: int = 0x0044
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "BooleanState",
            "BooleanStateConfiguration",
            "Descriptor",
            "Identify",
        )
    )


class Refrigerator(DeviceType):
    device_type: int = 0x0070
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ActivatedCarbonFilterMonitoring",
            "Descriptor",
            "Identify",
            "RefrigeratorAlarm",
            "RefrigeratorAndTemperatureControlledCabinetMode",
        )
    )


class RoboticVacuumCleaner(DeviceType):
    device_type: int = 0x0074
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "RvcCleanMode",
            "RvcOperationalState",
            "RvcRunMode",
            "ServiceArea",
        )
    )


class RoomAirConditioner(DeviceType):
    device_type: int = 0x0072
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ActivatedCarbonFilterMonitoring",
            "Descriptor",
            "FanControl",
            "Groups",
            "HepaFilterMonitoring",
            "Identify",
            "OnOff",
            "RelativeHumidityMeasurement",
            "ScenesManagement",
            "TemperatureMeasurement",
            "Thermostat",
            "ThermostatUserInterfaceConfiguration",
        )
    )


class RootNode(DeviceType):
    device_type: int = 0x0016
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "AccessControl",
            "AdministratorCommissioning",
            "BasicInformation",
            "Descriptor",
            "DiagnosticLogs",
            "EthernetNetworkDiagnostics",
            "GeneralCommissioning",
            "GeneralDiagnostics",
            "GroupKeyManagement",
            "IcdManagement",
            "LocalizationConfiguration",
            "NetworkCommissioning",
            "OperationalCredentials",
            "PowerSourceConfiguration",
            "SoftwareDiagnostics",
            "ThreadNetworkDiagnostics",
            "TimeFormatLocalization",
            "TimeSynchronization",
            "TlsCertificateManagement",
            "TlsClientManagement",
            "UnitLocalization",
            "WiFiNetworkDiagnostics",
        )
    )


class SecondaryNetworkInterface(DeviceType):
    device_type: int = 0x0019
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "EthernetNetworkDiagnostics",
            "NetworkCommissioning",
            "ThreadNetworkDiagnostics",
            "WiFiNetworkDiagnostics",
        )
    )


class SmokeCoAlarm(DeviceType):
    device_type: int = 0x0076
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CarbonMonoxideConcentrationMeasurement",
            "Descriptor",
            "Groups",
            "Identify",
            "RelativeHumidityMeasurement",
            "SmokeCoAlarm",
            "TemperatureMeasurement",
        )
    )


class SnapshotCamera(DeviceType):
    device_type: int = 0x0145
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "CameraAvSettingsUserLevelManagement",
            "CameraAvStreamManagement",
            "Descriptor",
            "Identify",
            "OccupancySensing",
            "ZoneManagement",
        )
    )


class SoilSensor(DeviceType):
    device_type: int = 0x0045
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "SoilMeasurement",
            "TemperatureMeasurement",
        )
    )


class SolarPower(DeviceType):
    device_type: int = 0x0017
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class Speaker(DeviceType):
    device_type: int = 0x0022
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "LevelControl",
            "OnOff",
        )
    )


class TemperatureControlledCabinet(DeviceType):
    device_type: int = 0x0071
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "OvenCavityOperationalState",
            "OvenMode",
            "RefrigeratorAndTemperatureControlledCabinetMode",
            "TemperatureAlarm",
            "TemperatureControl",
            "TemperatureMeasurement",
        )
    )


class TemperatureSensor(DeviceType):
    device_type: int = 0x0302
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "TemperatureMeasurement",
            "ThermostatUserInterfaceConfiguration",
        )
    )


class ThermostatController(DeviceType):
    device_type: int = 0x030A
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
        )
    )


class Thermostat(DeviceType):
    device_type: int = 0x0301
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "EnergyPreference",
            "Groups",
            "Identify",
            "Thermostat",
            "ThermostatUserInterfaceConfiguration",
        )
    )


class ThreadBorderRouter(DeviceType):
    device_type: int = 0x0091
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "ThreadBorderRouterManagement",
            "ThreadNetworkDiagnostics",
            "ThreadNetworkDirectory",
        )
    )


class VideoDoorbell(DeviceType):
    device_type: int = 0x0143
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
        )
    )


class VideoRemoteControl(DeviceType):
    device_type: int = 0x002A
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
        )
    )


class WaterFreezeDetector(DeviceType):
    device_type: int = 0x0041
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "BooleanState",
            "BooleanStateConfiguration",
            "Descriptor",
            "Identify",
        )
    )


class WaterHeater(DeviceType):
    device_type: int = 0x050F
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
            "Thermostat",
            "WaterHeaterManagement",
            "WaterHeaterMode",
        )
    )


class WaterLeakDetector(DeviceType):
    device_type: int = 0x0043
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "BooleanState",
            "BooleanStateConfiguration",
            "Descriptor",
            "Identify",
        )
    )


class WaterValve(DeviceType):
    device_type: int = 0x0042
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "FlowMeasurement",
            "Identify",
            "ValveConfigurationAndControl",
        )
    )


class WindowCoveringController(DeviceType):
    device_type: int = 0x0203
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "Descriptor",
            "Identify",
        )
    )


class WindowCovering(DeviceType):
    device_type: int = 0x0202
    clusters: set[type[Cluster]] = _LazyClusterSet(  # type: ignore[assignment]
        (
            "ClosureControl",
            "ClosureDimension",
            "Descriptor",
            "Groups",
            "Identify",
            "WindowCovering",
        )
    )
