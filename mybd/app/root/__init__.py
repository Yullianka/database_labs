from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    
    from .solar_station_route import solar_station_bp
    from .panel_route import panel_bp
    from .battery_route import battery_bp
    from .battery_charge_route import battery_charge_bp
    from .billing_account_route import billing_account_bp
    from .energy_sale_route import energy_sale_bp
    from .household_route import household_bp
    from .tilt_angle_route import tilt_angle_bp
    from .user_route import user_bp
    from .user_has_solar_station_route import user_has_solar_station_bp
    from .weather_conditions_route import weather_conditions_bp

    app.register_blueprint(solar_station_bp)
    app.register_blueprint(panel_bp)
    app.register_blueprint(battery_bp)
    app.register_blueprint(battery_charge_bp)
    app.register_blueprint(billing_account_bp)
    app.register_blueprint(energy_sale_bp)
    app.register_blueprint(household_bp)
    app.register_blueprint(tilt_angle_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(user_has_solar_station_bp)
    app.register_blueprint(weather_conditions_bp)
