from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import solar_station_controller, user_controller
from ..domain.solar_station import SolarStation

solar_station_bp = Blueprint('solar_station', __name__, url_prefix='/solar_station')


@solar_station_bp.route('', methods=['GET'])
def get_all_solar_stations() -> Response:
    """
    Get all solar stations
    ---
    tags:
      - Solar Stations
    responses:
      200:
        description: List of all solar stations
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              household:
                type: integer
              billing_account_id:
                type: integer
    """
    return make_response(jsonify(solar_station_controller.find_all()), HTTPStatus.OK)


@solar_station_bp.route('', methods=['POST'])
def create_solar_station() -> Response:
    """
    Create a new solar station
    ---
    tags:
      - Solar Stations
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
          properties:
            name:
              type: string
              description: Назва станції
            household:
              type: integer
              description: ID домогосподарства
            billing_account_id:
              type: integer
              description: ID рахунку
    responses:
      201:
        description: Solar station created successfully
      400:
        description: Invalid input data
    """
    content = request.get_json()
    solar_station = SolarStation.create_from_dto(content)
    solar_station_controller.create(solar_station)
    return make_response(jsonify(solar_station.put_into_dto()), HTTPStatus.CREATED)


@solar_station_bp.route('/<int:solar_station_id>', methods=['GET'])
def get_solar_station(solar_station_id: int) -> Response:
    """
    Get solar station by ID
    ---
    tags:
      - Solar Stations
    parameters:
      - name: solar_station_id
        in: path
        type: integer
        required: true
        description: ID сонячної станції
    responses:
      200:
        description: Solar station details
      404:
        description: Solar station not found
    """
    return make_response(jsonify(solar_station_controller.find_by_id(solar_station_id)), HTTPStatus.OK)


@solar_station_bp.route('/<int:solar_station_id>', methods=['PUT'])
def update_solar_station(solar_station_id: int) -> Response:
    """
    Update solar station completely
    ---
    tags:
      - Solar Stations
    parameters:
      - name: solar_station_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
          properties:
            name:
              type: string
              description: Назва станції
            household:
              type: integer
              description: ID домогосподарства
            billing_account_id:
              type: integer
              description: ID рахунку
    responses:
      200:
        description: Solar station updated successfully
      404:
        description: Solar station not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    solar_station = SolarStation.create_from_dto(content)
    solar_station_controller.update(solar_station_id, solar_station)
    return make_response("SolarStation updated", HTTPStatus.OK)


@solar_station_bp.route('/<int:solar_station_id>', methods=['PATCH'])
def patch_solar_station(solar_station_id: int) -> Response:
    """
    Partially update solar station
    ---
    tags:
      - Solar Stations
    parameters:
      - name: solar_station_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
              description: Назва станції
            household:
              type: integer
              description: ID домогосподарства
            billing_account_id:
              type: integer
              description: ID рахунку
    responses:
      200:
        description: Solar station updated successfully
      404:
        description: Solar station not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    solar_station_controller.patch(solar_station_id, content)
    return make_response("SolarStation updated", HTTPStatus.OK)


@solar_station_bp.route('/<int:solar_station_id>', methods=['DELETE'])
def delete_solar_station(solar_station_id: int) -> Response:
    """
    Delete solar station
    ---
    tags:
      - Solar Stations
    parameters:
      - name: solar_station_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Solar station deleted successfully
      404:
        description: Solar station not found
    """
    solar_station_controller.delete(solar_station_id)
    return make_response("SolarStation deleted", HTTPStatus.OK)
