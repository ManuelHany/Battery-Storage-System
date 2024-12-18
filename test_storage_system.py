import pytest
import os
from components import *

# Ensure the directory exists for the log file
log_dir = "./logs"
os.makedirs(log_dir, exist_ok=True)

# Create and configure logging inside the context manager
log_file_path = os.path.join(log_dir, "result.log")


@pytest.fixture
def dut():
    """
    Fixture representing the DUT with mock `set` and `get` methods.
    Ensures DUT returns to its original state after the test.
    Sets up logging to write results to a log file.
    """

    # Mock DUT state
    state = {}

    def set_state(key, value):
        state[key] = value
        return True

    def get_state(key):
        return state.get(key, None)

    yield {
        "set": set_state,
        "get": get_state
    }

    # Cleanup after the test (restore state)
    state.clear()


@pytest.mark.parametrize("setup_type", ["Basic", "Standard", "Pro"])
@pytest.mark.parametrize("operation", ["CHARGE", "DISCHARGE"])
@pytest.mark.parametrize("pv_production", [4000, 5000, 6000])
def test_storage_system(dut, setup_type, operation, pv_production):
    """
    Test storage system setup and energy management for various configurations and operations.
    """
    # Initialize Storage and Controller
    storage = Storage(setup_type)
    house_consumption = 3000 if operation == "CHARGE" else 8000
    controller = Controller(storage, pv_production, house_consumption)

    # Mock initial DUT state
    dut["set"]("operation", operation)
    dut["set"]("setup_type", setup_type)

    # Run energy management
    controller.manage_energy_flow()

    # Validate system status
    status = controller.get_status()

    # Log results inside the fixture
    with open(log_file_path, 'a') as log_file:
        log_results(setup_type, operation, status,log_file)

    if operation == "CHARGE":
        assert status["battery_charge"] > 0
        assert status["grid_power_surplus"] >= 0
        assert status["grid_power_required"] == 0
    else:  # DISCHARGE
        assert status["battery_charge"] < 0
        assert status["grid_power_surplus"] == 0
        assert status["grid_power_required"] >= 0

    assert status["storage_command_state"] == operation.upper()


def log_results(setup_type, operation, status, log_file):
    log_message = (
        f"setup_type: {setup_type}, operation: {operation}\n"
        f"pv_production: {status['pv_production']}\n"
        f"pv_consumption: {status['house_consumption']}\n"
        f"battery_charge: {status['battery_charge']}\n"
        f"grid_power_surplus: {status['grid_power_surplus']}\n"
        f"grid_power_required: {status['grid_power_required']}\n"
        f"storage_command_state: {status['storage_command_state']}\n"
        f"###########################################################\n"
    )
    log_file.write(log_message)
