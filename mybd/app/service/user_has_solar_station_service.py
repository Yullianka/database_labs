from .general_service import GeneralService
from ..dao import user_has_solar_station_dao

class UserHasSolarStationService(GeneralService):
    _dao = user_has_solar_station_dao