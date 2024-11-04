from .general_dao import GeneralDAO
from ..domain import Battery


class BatteryDAO(GeneralDAO):
    _domain_type = Battery