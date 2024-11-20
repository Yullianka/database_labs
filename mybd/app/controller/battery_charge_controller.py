from app.controller.general_controller import GeneralController
from ..service import battery_charge_service

class BatteryChargeController(GeneralController):
    _service = battery_charge_service


