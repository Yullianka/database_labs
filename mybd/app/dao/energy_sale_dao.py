from .general_dao import GeneralDAO
from ..domain import EnergySale


class EnergySaleDAO(GeneralDAO):
    _domain_type = EnergySale