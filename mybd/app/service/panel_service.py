from .general_service import GeneralService
from ..dao import panel_dao

class PanelService(GeneralService):
    _dao = panel_dao