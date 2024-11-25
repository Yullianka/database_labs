from app.controller.general_controller import GeneralController
from ..service import weather_conditions_service

class WeatherConditionsController(GeneralController):
    _service = weather_conditions_service