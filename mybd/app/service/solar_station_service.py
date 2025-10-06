from .general_service import GeneralService
from ..dao import solar_station_dao

class SolarStationService(GeneralService):
    _dao = solar_station_dao