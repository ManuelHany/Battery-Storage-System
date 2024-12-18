class House:
    def __init__(self, power_in_watts=600, house_voltage=220, house_frequency=50, current_in_amps=2.7):
        self.power_in_watts = power_in_watts  # Power entering house in Watts
        self.house_voltage = house_voltage  # Voltage of house grid
        self.house_frequency = house_frequency  # Frequency of house grid
        self.current_in_amps = current_in_amps  # Current flowing into house in Amps

