from app.controller.general_controller import GeneralController
from ..service import billing_account_service

class BillingAccountController(GeneralController):
    _service = billing_account_service


