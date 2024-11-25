from .general_service import GeneralService
from ..dao import weather_conditions_dao

class WeatherConditionsService(GeneralService):
    _dao = weather_conditions_dao