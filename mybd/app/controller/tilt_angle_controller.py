from app.controller.general_controller import GeneralController
from ..service import tilt_angle_service

class TiltAngleController(GeneralController):
    _service = tilt_angle_service


