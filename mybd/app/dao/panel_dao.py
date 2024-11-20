from .general_dao import GeneralDAO
from ..domain import Panel


class PanelDAO(GeneralDAO):
    _domain_type = Panel