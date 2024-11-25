from .battery_charge_service import BatteryChargeService
from .battery_service import BatteryService
from .billing_account_service import BillingAccountService
from .energy_sale_service import EnergySaleService
from .household_service import HouseholdsService
from .panel_service import PanelService
from .solar_station_service import SolarStationService
from .tilt_angle_service import TiltAngleService
from .user_has_solar_station_service import UserHasSolarStationService
from .user_service import UserService
from .weather_conditions_service import WeatherConditionsService

battery_charge_service = BatteryChargeService()
battery_service = BatteryService()
billing_account_service = BillingAccountService()
energy_sale_service = EnergySaleService()
household_service = HouseholdsService()
panel_service = PanelService()
solar_station_service = SolarStationService()
tilt_angle_service = TiltAngleService()
user_has_solar_station_service = UserHasSolarStationService()
user_service = UserService()
weather_conditions_service = WeatherConditionsService()