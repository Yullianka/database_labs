from .general_service import GeneralService
from ..dao import battery_charge_dao

class BatteryChargeService(GeneralService):
    _dao = battery_charge_dao