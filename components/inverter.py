

# battery_charge = {
#     "BM_0": 3000,
#     "BM_1": 3000
# }

class Inverter:

    def __init__(self, battery_charges, battery_voltage=48, battery_current=10,
                 power_flow_watts=-200, grid_frequency=50, grid_voltage=230):
        self.max_power_watts = self._set_max_power(battery_charges)  # Maximum charge/discharge power in Watts
        self.battery_voltage = battery_voltage  # Battery voltage in Volts
        self.battery_current = battery_current  # Battery current in Amps
        self.power_flow_watts = power_flow_watts  # Positive for charging, negative for discharging
        self.grid_frequency = grid_frequency  # Sensed grid frequency in Hertz
        self.grid_voltage = grid_voltage  # Sensed grid voltage in Volts

    @staticmethod
    def _set_max_power(battery_charges):
        max_power_watts = 0
        for max_battery_power in battery_charges.values():
            max_power_watts += max_battery_power
        return max_power_watts
