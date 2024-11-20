from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import battery_controller
from ..domain.battery import Battery

battery_bp = Blueprint('battery', __name__, url_prefix='/battery')


@battery_bp.route('', methods=['GET'])
def get_all_batteries() -> Response:
    return make_response(jsonify(battery_controller.find_all()), HTTPStatus.OK)


@battery_bp.route('', methods=['POST'])
def create_battery() -> Response:
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.create(battery)
    return make_response(jsonify(battery.put_into_dto()), HTTPStatus.CREATED)


@battery_bp.route('/<int:battery_id>', methods=['GET'])
def get_battery(battery_id: int) -> Response:
    return make_response(jsonify(battery_controller.find_by_id(battery_id)), HTTPStatus.OK)


@battery_bp.route('/<int:battery_id>', methods=['PUT'])
def update_battery(battery_id: int) -> Response:
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.update(battery_id, battery)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.route('/<int:battery_id>', methods=['PATCH'])
def patch_battery(battery_id: int) -> Response:
    content = request.get_json()
    battery_controller.patch(battery_id, content)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.route('/<int:battery_id>', methods=['DELETE'])
def delete_battery(battery_id: int) -> Response:
    battery_controller.delete(battery_id)
    return make_response("Battery deleted", HTTPStatus.OK)
