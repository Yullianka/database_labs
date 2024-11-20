from .general_service import GeneralService
from ..dao import energy_sale_dao

class EnergySaleService(GeneralService):
    _dao = energy_sale_dao