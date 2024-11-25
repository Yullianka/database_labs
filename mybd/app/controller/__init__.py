from .solar_station_controller import SolarStationController
from .panel_controller import PanelController
from .battery_controller import BatteryController
from .battery_charge_controller import BatteryChargeController
from .household_controller import HouseholdController
from .user_controller import UserController
from .energy_sale_controller import EnergySaleController
from .tilt_angle_controller import TiltAngleController
from .billing_account_controller import BillingAccountController
from .user_has_solar_station_controller import UserHasSolarStationController
from .weather_conditions_controller import WeatherConditionsController

solar_station_controller = SolarStationController()
panel_controller = PanelController()
battery_controller = BatteryController()
battery_charge_controller = BatteryChargeController()
household_controller = HouseholdController()
user_controller = UserController()
energy_sale_controller = EnergySaleController()
tilt_angle_controller = TiltAngleController()
billing_account_controller = BillingAccountController()
user_has_solar_station_controller = UserHasSolarStationController()
weather_conditions_controller = WeatherConditionsController()
