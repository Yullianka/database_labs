from .solar_station_dao import SolarStationDAO
from .panel_dao import PanelDAO
from .battery_dao import BatteryDAO
from .households_dao import HouseholdDAO
from .user_dao import UserDAO
from .energy_sale_dao import EnergySaleDAO
from .tilt_ange_dao import TiltAngleDAO
from .battery_charge_dao import BatteryChargeDAO
from .billing_account_dao import BillingAccountDAO
from .user_has_solar_station_dao import UserHasSolarStationDAO


solar_station_dao = SolarStationDAO()
panel_dao = PanelDAO()
battery_dao = BatteryDAO()
households_dao = HouseholdDAO()
user_dao = UserDAO()
energy_sale_dao = EnergySaleDAO()
tilt_ange_dao = TiltAngleDAO()
battery_charge_dao = BatteryChargeDAO()
billing_account_dao = BillingAccountDAO()
user_has_solar_station_dao = UserHasSolarStationDAO()
