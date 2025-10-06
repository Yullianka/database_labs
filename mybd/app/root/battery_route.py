from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import battery_controller
from ..domain.battery import Battery

battery_bp = Blueprint('battery', __name__, url_prefix='/battery')


@battery_bp.route('', methods=['GET'])
def get_all_batteries() -> Response:
    """
    Get all batteries
    ---
    tags:
      - Batteries
    responses:
      200:
        description: List of all batteries
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID батареї
              station_id:
                type: integer
                description: ID станції
              capacity:
                type: string
                description: Ємність батареї
              usage_duration:
                type: string
                description: Тривалість використання
              solar_station_id:
                type: integer
                description: ID сонячної станції
    """
    return make_response(jsonify(battery_controller.find_all()), HTTPStatus.OK)


@battery_bp.route('', methods=['POST'])
def create_battery() -> Response:
    """
    Create a new battery
    ---
    tags:
      - Batteries
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            station_id:
              type: integer
              description: ID станції
            capacity:
              type: string
              description: Ємність батареї
            usage_duration:
              type: string
              description: Тривалість використання
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      201:
        description: Battery created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            station_id:
              type: integer
            capacity:
              type: string
            usage_duration:
              type: string
            solar_station_id:
              type: integer
      400:
        description: Invalid input data
    """
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.create(battery)
    return make_response(jsonify(battery.put_into_dto()), HTTPStatus.CREATED)


@battery_bp.route('/<int:battery_id>', methods=['GET'])
def get_battery(battery_id: int) -> Response:
    """
    Get battery by ID
    ---
    tags:
      - Batteries
    parameters:
      - name: battery_id
        in: path
        type: integer
        required: true
        description: ID батареї
    responses:
      200:
        description: Battery details
        schema:
          type: object
          properties:
            id:
              type: integer
            station_id:
              type: integer
            capacity:
              type: string
            usage_duration:
              type: string
            solar_station_id:
              type: integer
      404:
        description: Battery not found
    """
    return make_response(jsonify(battery_controller.find_by_id(battery_id)), HTTPStatus.OK)


@battery_bp.route('/<int:battery_id>', methods=['PUT'])
def update_battery(battery_id: int) -> Response:
    """
    Update battery completely
    ---
    tags:
      - Batteries
    parameters:
      - name: battery_id
        in: path
        type: integer
        required: true
        description: ID батареї
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            station_id:
              type: integer
              description: ID станції
            capacity:
              type: string
              description: Ємність батареї
            usage_duration:
              type: string
              description: Тривалість використання
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Battery updated successfully
      404:
        description: Battery not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    battery = Battery.create_from_dto(content)
    battery_controller.update(battery_id, battery)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.route('/<int:battery_id>', methods=['PATCH'])
def patch_battery(battery_id: int) -> Response:
    """
    Partially update battery
    ---
    tags:
      - Batteries
    parameters:
      - name: battery_id
        in: path
        type: integer
        required: true
        description: ID батареї
      - in: body
        name: body
        schema:
          type: object
          properties:
            station_id:
              type: integer
              description: ID станції
            capacity:
              type: string
              description: Ємність батареї
            usage_duration:
              type: string
              description: Тривалість використання
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Battery updated successfully
      404:
        description: Battery not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    battery_controller.patch(battery_id, content)
    return make_response("Battery updated", HTTPStatus.OK)


@battery_bp.route('/<int:battery_id>', methods=['DELETE'])
def delete_battery(battery_id: int) -> Response:
    """
    Delete battery
    ---
    tags:
      - Batteries
    parameters:
      - name: battery_id
        in: path
        type: integer
        required: true
        description: ID батареї
    responses:
      200:
        description: Battery deleted successfully
      404:
        description: Battery not found
    """
    battery_controller.delete(battery_id)
    return make_response("Battery deleted", HTTPStatus.OK)
