from random import randint
from .battery_module import BatteryModule
from .inverter import Inverter


class Storage:

    def __init__(self, setup_type: str):
        """
        Initializes the Storage based on the given setup type: Basic, Standard, or Pro.
        """
        self.setup_type = setup_type
        self.battery_modules = self._set_battery_modules()
        self.inverters = Inverter(self._get_battery_charge())
        self.power_command = "CHARGE"

    def _set_battery_modules(self):
        """ Returns the number of battery modules based on setup type. """
        battery_modules = {}
        if self.setup_type == "Basic":
            for i in range(randint(1, 2)):
                instance_name = f"BM_{i}"
                battery_modules[instance_name] = BatteryModule()
        elif self.setup_type == "Standard":
            for i in range(3):
                instance_name = f"BM_{i}"
                battery_modules[instance_name] = BatteryModule()
        elif self.setup_type == "Pro":
            for i in range(randint(4, 5)):
                instance_name = f"BM_{i}"
                battery_modules[instance_name] = BatteryModule()
        else:
            raise ValueError("Unknown setup type")
        return battery_modules

    def _get_battery_charge(self):
        """ Return the maximum  watt power of each """
        battery_charges = {}
        for battery_id, specs in self.battery_modules.items():
            battery_charges[str(battery_id)] = specs.max_power_watts
        return battery_charges
