from .general_dao import GeneralDAO
from ..domain import BillingAccount


class BillingAccountDAO(GeneralDAO):
    _domain_type = BillingAccount