from .general_dao import GeneralDAO
from ..domain.battery_charge import BatteryCharge


class BatteryChargeDAO(GeneralDAO):
    _domain_type = BatteryCharge