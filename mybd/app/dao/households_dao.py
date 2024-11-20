from .general_dao import GeneralDAO
from ..domain import Household


class HouseholdDAO(GeneralDAO):
    _domain_type = Household