from app.controller.general_controller import GeneralController
from ..service import household_service

class HouseholdController(GeneralController):
    _service = household_service


