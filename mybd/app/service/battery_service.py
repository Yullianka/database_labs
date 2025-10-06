from .general_service import GeneralService
from ..dao import battery_dao

class BatteryService(GeneralService):
    _dao = battery_dao