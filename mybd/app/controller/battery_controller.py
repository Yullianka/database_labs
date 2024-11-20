from app.controller.general_controller import GeneralController
from ..service import battery_service

class BatteryController(GeneralController):
    _service = battery_service


if __name__ == "__main__":
    # Код, який має виконатися при запуску модуля
    print("Solar Station Controller запущено")

