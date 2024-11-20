from .general_service import GeneralService
from ..dao import households_dao

class HouseholdsService(GeneralService):
    _dao = households_dao