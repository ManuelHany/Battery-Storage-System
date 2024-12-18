# Class for Battery Module
class BatteryModule:
    def __init__(self, temperature_celsius=25, module_voltage=48, max_power_watts=1000):
        self.temperature_celsius = temperature_celsius  # Module temperature in Celsius
        self.module_voltage = module_voltage  # Module voltage in Volts
        self.max_power_watts = max_power_watts  # Max charge/discharge power in Watts

