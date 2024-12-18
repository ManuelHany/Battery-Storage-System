# Class for Photovoltaic Panel
class PhotovoltaicPanel:
    def __init__(self, power_watts=500, voltage_volts=40, current_amps=12.5):
        self.power_watts = power_watts  # Power in Watts
        self.voltage_volts = voltage_volts  # Voltage in Volts
        self.current_amps = current_amps  # Current in Amps