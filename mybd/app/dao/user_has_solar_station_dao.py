from .general_dao import GeneralDAO
from ..domain import UserHasSolarStation


class UserHasSolarStationDAO(GeneralDAO):
    _domain_type = UserHasSolarStation