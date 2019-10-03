"""Constants for ebus component."""
from homeassistant.const import ENERGY_KILO_WATT_HOUR, TEMP_CELSIUS, PRESSURE_BAR

DOMAIN = "ebusd"
TIME_SECONDS = "seconds"

#  SensorTypes from ebusdpy module :
#  0='decimal', 1='time-schedule', 2='switch', 3='string', 4='value;status'

SENSOR_TYPES = {
    "700": {
        "ActualFlowTemperatureDesired": [
            "Hc1ActualFlowTempDesired",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "MaxFlowTemperatureDesired": [
            "Hc1MaxFlowTempDesired",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "MinFlowTemperatureDesired": [
            "Hc1MinFlowTempDesired",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "PumpStatus": ["Hc1PumpStatus", None, "mdi:toggle-switch", 2],
        "HCSummerTemperatureLimit": [
            "Hc1SummerTempLimit",
            TEMP_CELSIUS,
            "mdi:weather-sunny",
            0,
        ],
        "HolidayTemperature": ["HolidayTemp", TEMP_CELSIUS, "mdi:thermometer", 0],
        "HWTemperatureDesired": ["HwcTempDesired", TEMP_CELSIUS, "mdi:thermometer", 0],
        "HWTimerMonday": ["hwcTimer.Monday", None, "mdi:timer", 1],
        "HWTimerTuesday": ["hwcTimer.Tuesday", None, "mdi:timer", 1],
        "HWTimerWednesday": ["hwcTimer.Wednesday", None, "mdi:timer", 1],
        "HWTimerThursday": ["hwcTimer.Thursday", None, "mdi:timer", 1],
        "HWTimerFriday": ["hwcTimer.Friday", None, "mdi:timer", 1],
        "HWTimerSaturday": ["hwcTimer.Saturday", None, "mdi:timer", 1],
        "HWTimerSunday": ["hwcTimer.Sunday", None, "mdi:timer", 1],
        "WaterPressure": ["WaterPressure", PRESSURE_BAR, "mdi:water-pump", 0],
        "Zone1RoomZoneMapping": ["z1RoomZoneMapping", None, "mdi:label", 0],
        "Zone1NightTemperature": ["z1NightTemp", TEMP_CELSIUS, "mdi:weather-night", 0],
        "Zone1DayTemperature": ["z1DayTemp", TEMP_CELSIUS, "mdi:weather-sunny", 0],
        "Zone1HolidayTemperature": [
            "z1HolidayTemp",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "Zone1RoomTemperature": ["z1RoomTemp", TEMP_CELSIUS, "mdi:thermometer", 0],
        "Zone1ActualRoomTemperatureDesired": [
            "z1ActualRoomTempDesired",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "Zone1TimerMonday": ["z1Timer.Monday", None, "mdi:timer", 1],
        "Zone1TimerTuesday": ["z1Timer.Tuesday", None, "mdi:timer", 1],
        "Zone1TimerWednesday": ["z1Timer.Wednesday", None, "mdi:timer", 1],
        "Zone1TimerThursday": ["z1Timer.Thursday", None, "mdi:timer", 1],
        "Zone1TimerFriday": ["z1Timer.Friday", None, "mdi:timer", 1],
        "Zone1TimerSaturday": ["z1Timer.Saturday", None, "mdi:timer", 1],
        "Zone1TimerSunday": ["z1Timer.Sunday", None, "mdi:timer", 1],
        "Zone1OperativeMode": ["z1OpMode", None, "mdi:math-compass", 3],
        "ContinuosHeating": ["ContinuosHeating", TEMP_CELSIUS, "mdi:weather-snowy", 0],
        "PowerEnergyConsumptionLastMonth": [
            "PrEnergySumHcLastMonth",
            ENERGY_KILO_WATT_HOUR,
            "mdi:flash",
            0,
        ],
        "PowerEnergyConsumptionThisMonth": [
            "PrEnergySumHcThisMonth",
            ENERGY_KILO_WATT_HOUR,
            "mdi:flash",
            0,
        ],
    },
    "ehp": {
        "HWTemperature": ["HwcTemp", TEMP_CELSIUS, "mdi:thermometer", 4],
        "OutsideTemp": ["OutsideTemp", TEMP_CELSIUS, "mdi:thermometer", 4],
    },
    "bai": {
        "HotWaterTemperature": ["HwcTemp", TEMP_CELSIUS, "mdi:thermometer", 4],
        "StorageTemperature": ["StorageTemp", TEMP_CELSIUS, "mdi:thermometer", 4],
        "DesiredStorageTemperature": [
            "StorageTempDesired",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "OutdoorsTemperature": [
            "OutdoorstempSensor",
            TEMP_CELSIUS,
            "mdi:thermometer",
            4,
        ],
        "WaterPreasure": ["WaterPressure", PRESSURE_BAR, "mdi:pipe", 4],
        "AverageIgnitionTime": ["averageIgnitiontime", TIME_SECONDS, "mdi:av-timer", 0],
        "MaximumIgnitionTime": ["maxIgnitiontime", TIME_SECONDS, "mdi:av-timer", 0],
        "MinimumIgnitionTime": ["minIgnitiontime", TIME_SECONDS, "mdi:av-timer", 0],
        "ReturnTemperature": ["ReturnTemp", TEMP_CELSIUS, "mdi:thermometer", 4],
        "CentralHeatingPump": ["WP", None, "mdi:toggle-switch", 2],
        "HeatingSwitch": ["HeatingSwitch", None, "mdi:toggle-switch", 2],
        "DesiredFlowTemperature": [
            "FlowTempDesired",
            TEMP_CELSIUS,
            "mdi:thermometer",
            0,
        ],
        "FlowTemperature": ["FlowTemp", TEMP_CELSIUS, "mdi:thermometer", 4],
        "Flame": ["Flame", None, "mdi:toggle-switch", 2],
        "PowerEnergyConsumptionHeatingCircuit": [
            "PrEnergySumHc1",
            ENERGY_KILO_WATT_HOUR,
            "mdi:flash",
            0,
        ],
        "PowerEnergyConsumptionHotWaterCircuit": [
            "PrEnergySumHwc1",
            ENERGY_KILO_WATT_HOUR,
            "mdi:flash",
            0,
        ],
        "RoomThermostat": ["DCRoomthermostat", None, "mdi:toggle-switch", 2],
        "HeatingPartLoad": ["PartloadHcKW", ENERGY_KILO_WATT_HOUR, "mdi:flash", 0],
    },
}