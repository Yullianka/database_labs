from app.controller.general_controller import GeneralController
from ..service import user_has_solar_station_service



class UserHasSolarStationController(GeneralController):
    _service = user_has_solar_station_service
  
    print('all right')