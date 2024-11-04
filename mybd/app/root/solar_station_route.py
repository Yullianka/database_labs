from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import solar_station_controller, user_controller
from ..domain.solar_station import SolarStation

solar_station_bp = Blueprint('solar_station', __name__, url_prefix='/solar_station')


@solar_station_bp.route('', methods=['GET'])
def get_all_solar_stations() -> Response:
    return make_response(jsonify(solar_station_controller.find_all()), HTTPStatus.OK)


@solar_station_bp.route('', methods=['POST'])
def create_solar_station() -> Response:
    content = request.get_json()
    solar_station = SolarStation.create_from_dto(content)
    solar_station_controller.create(solar_station)
    return make_response(jsonify(solar_station.put_into_dto()), HTTPStatus.CREATED)


@solar_station_bp.route('/<int:solar_station_id>', methods=['GET'])
def get_solar_station(solar_station_id: int) -> Response:
    return make_response(jsonify(solar_station_controller.find_by_id(solar_station_id)), HTTPStatus.OK)


@solar_station_bp.route('/<int:solar_station_id>', methods=['PUT'])
def update_solar_station(solar_station_id: int) -> Response:
    content = request.get_json()
    solar_station = SolarStation.create_from_dto(content)
    solar_station_controller.update(solar_station_id, solar_station)
    return make_response("SolarStation updated", HTTPStatus.OK)


@solar_station_bp.route('/<int:solar_station_id>', methods=['PATCH'])
def patch_solar_station(solar_station_id: int) -> Response:
    content = request.get_json()
    solar_station_controller.patch(solar_station_id, content)
    return make_response("SolarStation updated", HTTPStatus.OK)


@solar_station_bp.route('/<int:solar_station_id>', methods=['DELETE'])
def delete_solar_station(solar_station_id: int) -> Response:
    solar_station_controller.delete(solar_station_id)
    return make_response("SolarStation deleted", HTTPStatus.OK)
