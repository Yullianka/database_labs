from .general_dao import GeneralDAO
from ..domain import WeatherCondition


class WeatherConditionDAO(GeneralDAO):
    _domain_type = WeatherCondition