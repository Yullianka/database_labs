from app.controller.general_controller import GeneralController
from ..service import energy_sale_service

class EnergySaleController(GeneralController):
    _service = energy_sale_service


