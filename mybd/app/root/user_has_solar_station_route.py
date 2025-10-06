from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import user_has_solar_station_controller
from ..domain.user_has_solar_station import UserHasSolarStation

user_has_solar_station_bp = Blueprint('user_has_solar_station', __name__, url_prefix='/user_has_solar_station')

@user_has_solar_station_bp.route('', methods=['GET'])
def get_all_user_solar_stations() -> Response:
    """
    Get all user-solar station relationships
    ---
    tags:
      - User-Solar Station Relations
    responses:
      200:
        description: List of all user-solar station relationships
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID зв'язку
              user_id:
                type: integer
                description: ID користувача
              solar_station_id:
                type: integer
                description: ID сонячної станції
              ownership_date:
                type: string
                description: Дата володіння
    """
    return make_response(jsonify(user_has_solar_station_controller.find_all()), HTTPStatus.OK)

@user_has_solar_station_bp.route('', methods=['POST'])
def create_user_solar_station() -> Response:
    """
    Create a new user-solar station relationship
    ---
    tags:
      - User-Solar Station Relations
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              description: ID користувача
            solar_station_id:
              type: integer
              description: ID сонячної станції
            ownership_date:
              type: string
              description: Дата володіння
    responses:
      201:
        description: User-solar station relationship created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            user_id:
              type: integer
            solar_station_id:
              type: integer
            ownership_date:
              type: string
      400:
        description: Invalid input data
    """
    content = request.get_json()
    user_solar_station = UserHasSolarStation.create_from_dto(content)
    user_has_solar_station_controller.create(user_solar_station)
    return make_response(jsonify(user_solar_station.put_into_dto()), HTTPStatus.CREATED)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['GET'])
def get_user_solar_station(user_has_solar_station_id: int) -> Response:
    """
    Get user-solar station relationship by ID
    ---
    tags:
      - User-Solar Station Relations
    parameters:
      - name: user_has_solar_station_id
        in: path
        type: integer
        required: true
        description: ID зв'язку користувач-сонячна станція
    responses:
      200:
        description: User-solar station relationship details
        schema:
          type: object
          properties:
            id:
              type: integer
            user_id:
              type: integer
            solar_station_id:
              type: integer
            ownership_date:
              type: string
      404:
        description: User-solar station relationship not found
    """
    return make_response(jsonify(user_has_solar_station_controller.find_by_id(user_has_solar_station_id)), HTTPStatus.OK)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['PUT'])
def update_user_solar_station(user_has_solar_station_id: int) -> Response:
    """
    Update user-solar station relationship completely
    ---
    tags:
      - User-Solar Station Relations
    parameters:
      - name: user_has_solar_station_id
        in: path
        type: integer
        required: true
        description: ID зв'язку користувач-сонячна станція
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              description: ID користувача
            solar_station_id:
              type: integer
              description: ID сонячної станції
            ownership_date:
              type: string
              description: Дата володіння
    responses:
      200:
        description: User-solar station relationship updated successfully
      404:
        description: User-solar station relationship not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    user_solar_station = UserHasSolarStation.create_from_dto(content)
    user_has_solar_station_controller.update(user_has_solar_station_id, user_solar_station)
    return make_response("User Solar Station association updated", HTTPStatus.OK)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['PATCH'])
def patch_user_solar_station(user_has_solar_station_id: int) -> Response:
    """
    Partially update user-solar station relationship
    ---
    tags:
      - User-Solar Station Relations
    parameters:
      - name: user_has_solar_station_id
        in: path
        type: integer
        required: true
        description: ID зв'язку користувач-сонячна станція
      - in: body
        name: body
        schema:
          type: object
          properties:
            user_id:
              type: integer
              description: ID користувача
            solar_station_id:
              type: integer
              description: ID сонячної станції
            ownership_date:
              type: string
              description: Дата володіння
    responses:
      200:
        description: User-solar station relationship updated successfully
      404:
        description: User-solar station relationship not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    user_has_solar_station_controller.patch(user_has_solar_station_id, content)
    return make_response("User Solar Station association updated", HTTPStatus.OK)

@user_has_solar_station_bp.route('/<int:user_has_solar_station_id>', methods=['DELETE'])
def delete_user_solar_station(user_has_solar_station_id: int) -> Response:
    """
    Delete user-solar station relationship
    ---
    tags:
      - User-Solar Station Relations
    parameters:
      - name: user_has_solar_station_id
        in: path
        type: integer
        required: true
        description: ID зв'язку користувач-сонячна станція
    responses:
      200:
        description: User-solar station relationship deleted successfully
      404:
        description: User-solar station relationship not found
    """
    user_has_solar_station_controller.delete(user_has_solar_station_id)
    return make_response("User Solar Station association deleted", HTTPStatus.OK)
