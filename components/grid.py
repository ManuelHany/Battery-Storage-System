class Grid:
    def __init__(self, power_sold_bought=200, grid_voltage=230, grid_frequency=50):
        self.power_sold_bought = power_sold_bought  # Power sold/bought in Watts
        self.grid_voltage = grid_voltage  # Voltage in Volts
        self.grid_frequency = grid_frequency  # Frequency in Hertz
