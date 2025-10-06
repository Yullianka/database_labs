from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import user_has_solar_station_controller
from ..domain.user_has_solar_station import UserHasSolarStation

user_has_solar_station_bp = Blueprint('user_has_solar_station', __name__, url_prefix='/user_has_solar_station')

@user_has_solar_station_bp.route('', methods=['GET'])
def get_all_user_solar_stations() -> Response:
    return make_response(jsonify(user_has_solar_station_controller.find_all()), HTTPStatus.OK)

@user_has_solar_station_bp.route('', methods=['POST'])
def create_user_solar_station() -> Response:
    content = request.get_json()
    user_solar_station = UserHasSolarStation.create_from_dto(content)
    user_has_solar_station_controller.create(user_solar_station)
    return make_response(jsonify(user_solar_station.put_into_dto()), HTTPStatus.CREATED)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['GET'])
def get_user_solar_station(user_has_solar_station_id: int) -> Response:
    return make_response(jsonify(user_has_solar_station_controller.find_by_id(user_has_solar_station_id)), HTTPStatus.OK)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['PUT'])
def update_user_solar_station(user_has_solar_station_id: int) -> Response:
    content = request.get_json()
    user_solar_station = UserHasSolarStation.create_from_dto(content)
    user_has_solar_station_controller.update(user_has_solar_station_id, user_solar_station)
    return make_response("User Solar Station association updated", HTTPStatus.OK)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['PATCH'])
def patch_user_solar_station(user_has_solar_station_id: int) -> Response:
    content = request.get_json()
    user_has_solar_station_controller.patch(user_has_solar_station_id, content)
    return make_response("User Solar Station association updated", HTTPStatus.OK)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['DELETE'])
def delete_user_solar_station(user_has_solar_station_id: int) -> Response:
    user_has_solar_station_controller.delete(user_has_solar_station_id)
    return make_response("User Solar Station association deleted", HTTPStatus.OK)
