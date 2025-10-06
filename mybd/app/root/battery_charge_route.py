from http import HTTPStatus
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


@battery_charge_bp.route('', methods=['GET'])
def get_all_battery_charges() -> Response:
    """
    Get all battery charges
    ---
    tags:
      - Battery Charges
    responses:
      200:
        description: List of all battery charges
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID заряду батареї
              battery_id:
                type: integer
                description: ID батареї
              charge_level:
                type: string
                description: Рівень заряду
              date:
                type: string
                description: Дата
    """
    return make_response(jsonify(battery_charge_controller.find_all()), HTTPStatus.OK)


@battery_charge_bp.route('', methods=['POST'])
def create_battery_charge() -> Response:
    """
    Create a new battery charge
    ---
    tags:
      - Battery Charges
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            battery_id:
              type: integer
              description: ID батареї
            charge_level:
              type: string
              description: Рівень заряду
            date:
              type: string
              description: Дата
    responses:
      201:
        description: Battery charge created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            battery_id:
              type: integer
            charge_level:
              type: string
            date:
              type: string
      400:
        description: Invalid input data
    """
    content = request.get_json()
    battery_charge = BatteryCharge.create_from_dto(content)
    battery_charge_controller.create(battery_charge)
    return make_response(jsonify(battery_charge.put_into_dto()), HTTPStatus.CREATED)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['GET'])
def get_battery_charge(battery_charge_id: int) -> Response:
    """
    Get battery charge by ID
    ---
    tags:
      - Battery Charges
    parameters:
      - name: battery_charge_id
        in: path
        type: integer
        required: true
        description: ID заряду батареї
    responses:
      200:
        description: Battery charge details
        schema:
          type: object
          properties:
            id:
              type: integer
            battery_id:
              type: integer
            charge_level:
              type: string
            date:
              type: string
      404:
        description: Battery charge not found
    """
    return make_response(jsonify(battery_charge_controller.find_by_id(battery_charge_id)), HTTPStatus.OK)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['PUT'])
def update_battery_charge(battery_charge_id: int) -> Response:
    """
    Update battery charge completely
    ---
    tags:
      - Battery Charges
    parameters:
      - name: battery_charge_id
        in: path
        type: integer
        required: true
        description: ID заряду батареї
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            battery_id:
              type: integer
              description: ID батареї
            charge_level:
              type: string
              description: Рівень заряду
            date:
              type: string
              description: Дата
    responses:
      200:
        description: Battery charge updated successfully
      404:
        description: Battery charge not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    battery_charge = BatteryCharge.create_from_dto(content)
    battery_charge_controller.update(battery_charge_id, battery_charge)
    return make_response("Battery charge updated", HTTPStatus.OK)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['PATCH'])
def patch_battery_charge(battery_charge_id: int) -> Response:
    """
    Partially update battery charge
    ---
    tags:
      - Battery Charges
    parameters:
      - name: battery_charge_id
        in: path
        type: integer
        required: true
        description: ID заряду батареї
      - in: body
        name: body
        schema:
          type: object
          properties:
            battery_id:
              type: integer
              description: ID батареї
            charge_level:
              type: string
              description: Рівень заряду
            date:
              type: string
              description: Дата
    responses:
      200:
        description: Battery charge updated successfully
      404:
        description: Battery charge not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    battery_charge_controller.patch(battery_charge_id, content)
    return make_response("Battery charge updated", HTTPStatus.OK)


@battery_charge_bp.route('/<int:battery_charge_id>', methods=['DELETE'])
def delete_battery_charge(battery_charge_id: int) -> Response:
    """
    Delete battery charge
    ---
    tags:
      - Battery Charges
    parameters:
      - name: battery_charge_id
        in: path
        type: integer
        required: true
        description: ID заряду батареї
    responses:
      200:
        description: Battery charge deleted successfully
      404:
        description: Battery charge not found
    """
    battery_charge_controller.delete(battery_charge_id)
    return make_response("Battery charge deleted", HTTPStatus.OK)
