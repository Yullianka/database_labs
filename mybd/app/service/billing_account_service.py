from .general_service import GeneralService
from ..dao import billing_account_dao

class BillingAccountService(GeneralService):
    _dao = billing_account_dao