from .general_service import GeneralService
from ..dao import tilt_ange_dao

class TiltAngleService(GeneralService):
    _dao = tilt_ange_dao