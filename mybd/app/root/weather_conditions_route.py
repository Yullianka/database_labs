from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import weather_conditions_controller
from ..domain.weather_conditions import WeatherCondition

weather_conditions_bp = Blueprint('weather_conditions', __name__, url_prefix='/weather_conditions')


@weather_conditions_bp.route('', methods=['GET'])
def get_all_panels() -> Response:
    return make_response(jsonify(weather_conditions_controller.find_all()), HTTPStatus.OK)


@weather_conditions_bp.route('', methods=['POST'])
def create_weather_conditions() -> Response:
    content = request.get_json()
    weather_conditions = WeatherCondition.create_from_dto(content)
    weather_conditions_controller.create(weather_conditions)
    return make_response(jsonify(weather_conditions.put_into_dto()), HTTPStatus.CREATED)


@weather_conditions_bp.route('/<int:weather_conditions_id>', methods=['GET'])
def get_weather_conditions(weather_conditions_id: int) -> Response:
    return make_response(jsonify(weather_conditions_controller.find_by_id(weather_conditions_id)), HTTPStatus.OK)


@weather_conditions_bp.route('/<int:weather_conditions_id>', methods=['PUT'])
def update_weather_conditions(weather_conditions_id: int) -> Response:
    content = request.get_json()
    weather_conditions = WeatherCondition.create_from_dto(content)
    weather_conditions_controller.update(weather_conditions_id, weather_conditions)
    return make_response("weather_conditions updated", HTTPStatus.OK)


@weather_conditions_bp.route('/<int:weather_conditions_id>', methods=['PATCH'])
def patch_weather_conditions(weather_conditions_id: int) -> Response:
    content = request.get_json()
    weather_conditions_controller.patch(weather_conditions_id, content)
    return make_response("weather_conditions updated", HTTPStatus.OK)


@weather_conditions_bp.route('/<int:weather_conditions_id>', methods=['DELETE'])
def delete_weather_conditions(weather_conditions_id: int) -> Response:
    weather_conditions_controller.delete(weather_conditions_id)
    return make_response("Weather_conditions deleted", HTTPStatus.OK)
