from components import Storage

class Controller:

    def __init__(self, storage: Storage, pv_production, house_consumption):
        self.storage = storage
        self.pv_production = pv_production
        self.house_consumption = house_consumption
        self.battery_charge_status = 0
        self.grid_power_surplus = 0
        self.grid_power_required = 0

    def manage_energy_flow(self):
        """
        Implements the energy management algorithm:
        1. Charge battery with surplus PV.
        2. Export remaining power to the grid.
        3. Discharge storage to supply the house if PV isn't sufficient.
        4. Import remaining power from the grid if needed.
        """
        surplus = self.pv_production - self.house_consumption
        total_battery_power = self.storage.inverters.max_power_watts


        if surplus > 0:
            # Charge batteries first
            self.battery_charge_status = min(surplus, total_battery_power)  # Limit charging rate
            surplus -= self.battery_charge_status

            # Send remaining power to the grid
            self.grid_power_surplus = surplus
            self.storage.power_command = "CHARGE"

        else:
            # Discharge battery to supply power to the house
            required_power = abs(surplus)
            self.battery_charge_status = -min(required_power, total_battery_power)  # Limit discharging rate
            required_power -= abs(self.battery_charge_status)

            # Import remaining power from the grid
            self.grid_power_required = required_power
            if self.battery_charge_status:
                self.storage.power_command = "DISCHARGE"

    def get_status(self):
        """
        Returns the current system status as a dictionary.
        """
        return {
            "pv_production": self.pv_production,
            "house_consumption": self.house_consumption,
            "setup_type": self.storage.setup_type,
            "battery_charge": self.battery_charge_status,
            "grid_power_surplus": self.grid_power_surplus,
            "grid_power_required": self.grid_power_required,
            "storage_command_state": self.storage.power_command
        }
