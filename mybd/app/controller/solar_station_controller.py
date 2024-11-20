from app.controller.general_controller import GeneralController
from ..service import solar_station_service

class SolarStationController(GeneralController):
    _service = solar_station_service


