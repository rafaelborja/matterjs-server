"""Auto-generated cluster imports (DO NOT edit).

Each cluster module is imported on first attribute access instead of at package import.
"""

import sys as _sys
import types as _types

__all__ = [
    "Globals",
    "AccessControl",
    "AccountLogin",
    "Actions",
    "ActivatedCarbonFilterMonitoring",
    "AdministratorCommissioning",
    "AirQuality",
    "AmbientContextSensing",
    "ApplicationBasic",
    "ApplicationLauncher",
    "AudioOutput",
    "BasicInformation",
    "Binding",
    "BooleanState",
    "BooleanStateConfiguration",
    "BridgedDeviceBasicInformation",
    "CameraAvSettingsUserLevelManagement",
    "CameraAvStreamManagement",
    "CarbonDioxideConcentrationMeasurement",
    "CarbonMonoxideConcentrationMeasurement",
    "Channel",
    "Chime",
    "ClosureControl",
    "ClosureDimension",
    "ColorControl",
    "CommissionerControl",
    "CommodityMetering",
    "CommodityPrice",
    "CommodityTariff",
    "ContentAppObserver",
    "ContentControl",
    "ContentLauncher",
    "Descriptor",
    "DeviceEnergyManagement",
    "DeviceEnergyManagementMode",
    "DiagnosticLogs",
    "DishwasherAlarm",
    "DishwasherMode",
    "DoorLock",
    "DraftElectricalMeasurementCluster",
    "EcosystemInformation",
    "ElectricalEnergyMeasurement",
    "ElectricalGridConditions",
    "ElectricalPowerMeasurement",
    "EnergyEvse",
    "EnergyEvseMode",
    "EnergyPreference",
    "EthernetNetworkDiagnostics",
    "EveCluster",
    "FanControl",
    "FixedLabel",
    "FlowMeasurement",
    "FormaldehydeConcentrationMeasurement",
    "GeneralCommissioning",
    "GeneralDiagnostics",
    "GroupKeyManagement",
    "Groupcast",
    "Groups",
    "HeimanCluster",
    "HepaFilterMonitoring",
    "IcdManagement",
    "Identify",
    "IlluminanceMeasurement",
    "InovelliCluster",
    "JointFabricAdministrator",
    "JointFabricDatastore",
    "KeypadInput",
    "LaundryDryerControls",
    "LaundryWasherControls",
    "LaundryWasherMode",
    "LevelControl",
    "LocalizationConfiguration",
    "LowPower",
    "MediaInput",
    "MediaPlayback",
    "Messages",
    "MeterIdentification",
    "MicrowaveOvenControl",
    "MicrowaveOvenMode",
    "ModeSelect",
    "NeoCluster",
    "NetworkCommissioning",
    "NitrogenDioxideConcentrationMeasurement",
    "OccupancySensing",
    "OnOff",
    "OperationalCredentials",
    "OperationalState",
    "OtaSoftwareUpdateProvider",
    "OtaSoftwareUpdateRequestor",
    "OvenCavityOperationalState",
    "OvenMode",
    "OzoneConcentrationMeasurement",
    "Pm10ConcentrationMeasurement",
    "Pm1ConcentrationMeasurement",
    "Pm25ConcentrationMeasurement",
    "PowerSource",
    "PowerSourceConfiguration",
    "PowerTopology",
    "PressureMeasurement",
    "PumpConfigurationAndControl",
    "PushAvStreamTransport",
    "RadonConcentrationMeasurement",
    "RefrigeratorAlarm",
    "RefrigeratorAndTemperatureControlledCabinetMode",
    "RelativeHumidityMeasurement",
    "RvcCleanMode",
    "RvcOperationalState",
    "RvcRunMode",
    "ScenesManagement",
    "ServiceArea",
    "SmokeCoAlarm",
    "SoftwareDiagnostics",
    "SoilMeasurement",
    "Switch",
    "TargetNavigator",
    "TclDehumidifierCluster",
    "TemperatureAlarm",
    "TemperatureControl",
    "TemperatureMeasurement",
    "Thermostat",
    "ThermostatUserInterfaceConfiguration",
    "ThirdRealityMeteringCluster",
    "ThreadBorderRouterManagement",
    "ThreadNetworkDiagnostics",
    "ThreadNetworkDirectory",
    "TimeFormatLocalization",
    "TimeSynchronization",
    "TlsCertificateManagement",
    "TlsClientManagement",
    "TotalVolatileOrganicCompoundsConcentrationMeasurement",
    "UnitLocalization",
    "UserLabel",
    "ValveConfigurationAndControl",
    "WagoCluster",
    "WakeOnLan",
    "WaterHeaterManagement",
    "WaterHeaterMode",
    "WaterTankLevelMonitoring",
    "WebRtcTransportDefinitions",
    "WebRtcTransportProvider",
    "WebRtcTransportRequestor",
    "WiFiNetworkDiagnostics",
    "WiFiNetworkManagement",
    "WindowCovering",
    "ZoneManagement",
]

_NAMES = frozenset(__all__)


class _ClusterDefsModule(_types.ModuleType):
    # Keep attribute X bound to class X, as the eager package did, when submodule X is imported
    # directly or returned as a pending lazy submodule (Python 3.15 lazy imports).
    def __setattr__(self, name: str, value: object) -> None:
        if isinstance(value, _types.ModuleType) and name in _NAMES and value.__name__ == self.__name__ + "." + name:
            value = getattr(value, name)
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> object:
        value = super().__getattribute__(name)
        if isinstance(value, _types.ModuleType) and name in _NAMES:
            value = getattr(value, name)
            _types.ModuleType.__setattr__(self, name, value)
        return value


_sys.modules[__name__].__class__ = _ClusterDefsModule


def __getattr__(name: str) -> object:
    if name in _NAMES:
        full = __name__ + "." + name
        module = _sys.modules.get(full)
        if module is None:
            __import__(full)
            module = _sys.modules[full]
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(globals()) | _NAMES)
