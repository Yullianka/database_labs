from http import HTTPStatus
from typing import Tuple
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import battery_charge_controller
from ..domain.battery_charge import BatteryCharge

battery_charge_bp = Blueprint('battery_charge', __name__, url_prefix='/battery_charge')


@battery_charge_bp.route('', methods=['GET'])
def get_all_battery_charges() -> Response:
    return make_response(jsonify(battery_charge_controller.find_all()), HTTPStatus.OK)


@battery_charge_bp.route('', methods=['POST'])
def create_battery_charge() -> Response:
    content = request.get_json()
    battery_charge = BatteryCharge.create_from_dto(content)
    battery_charge_controller.create(battery_charge)
    return make_response(jsonify(battery_charge.put_into_dto()), HTTPStatus.CREATED)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['GET'])
def get_battery_charge(battery_charge_id: int) -> Response:
    return make_response(jsonify(battery_charge_controller.find_by_id(battery_charge_id)), HTTPStatus.OK)



@battery_charge_bp.route('/<int:battery_charge_id>', methods=['PUT'])
def update_battery_charge(battery_charge_id: int) -> Response:
    content = request.get_json()
    battery_charge = BatteryCharge.create_from_dto(content)
    battery_charge_controller.update(battery_charge_id, battery_charge)
    return make_response("BatteryCharge updated", HTTPStatus.OK)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['PATCH'])
def patch_battery_charge(battery_charge_id: int) -> Response:
    content = request.get_json()
    battery_charge_controller.patch(battery_charge_id, content)
    return make_response("BatteryCharge updated", HTTPStatus.OK)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['DELETE'])
def delete_battery_charge(battery_charge_id: int) -> Response:
    battery_charge_controller.delete(battery_charge_id)
    return make_response("BatteryCharge deleted", HTTPStatus.OK)
