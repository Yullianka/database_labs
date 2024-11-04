from .general_dao import GeneralDAO
from ..domain import SolarStation


class SolarStationDAO(GeneralDAO):
    _domain_type = SolarStation