from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller import tilt_angle_controller
from ..domain.tilt_angle import TiltAngle

tilt_angle_bp = Blueprint('tilt_angle', __name__, url_prefix='/tilt_angle')

@tilt_angle_bp.route('', methods=['GET'])
def get_all_tilt_angles() -> Response:
    """
    Get all tilt angles
    ---
    tags:
      - Tilt Angles
    responses:
      200:
        description: List of all tilt angles
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID кута нахилу
              angle:
                type: string
                description: Кут нахилу
              efficiency:
                type: string
                description: Ефективність
              solar_station_id:
                type: integer
                description: ID сонячної станції
    """
    return make_response(jsonify(tilt_angle_controller.find_all()), HTTPStatus.OK)


@tilt_angle_bp.route('', methods=['POST'])
def create_tilt_angle() -> Response:
    """
    Create a new tilt angle
    ---
    tags:
      - Tilt Angles
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            angle:
              type: string
              description: Кут нахилу
            efficiency:
              type: string
              description: Ефективність
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      201:
        description: Tilt angle created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            angle:
              type: string
            efficiency:
              type: string
            solar_station_id:
              type: integer
      400:
        description: Invalid input data
    """
    content = request.get_json()
    tilt_angle = TiltAngle.create_from_dto(content)
    tilt_angle_controller.create(tilt_angle)
    return make_response(jsonify(tilt_angle.put_into_dto()), HTTPStatus.CREATED)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['GET'])
def get_tilt_angle(tilt_angle_id: int) -> Response:
    """
    Get tilt angle by ID
    ---
    tags:
      - Tilt Angles
    parameters:
      - name: tilt_angle_id
        in: path
        type: integer
        required: true
        description: ID кута нахилу
    responses:
      200:
        description: Tilt angle details
        schema:
          type: object
          properties:
            id:
              type: integer
            angle:
              type: string
            efficiency:
              type: string
            solar_station_id:
              type: integer
      404:
        description: Tilt angle not found
    """
    return make_response(jsonify(tilt_angle_controller.find_by_id(tilt_angle_id)), HTTPStatus.OK)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['PUT'])
def update_tilt_angle(tilt_angle_id: int) -> Response:
    """
    Update tilt angle completely
    ---
    tags:
      - Tilt Angles
    parameters:
      - name: tilt_angle_id
        in: path
        type: integer
        required: true
        description: ID кута нахилу
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            angle:
              type: string
              description: Кут нахилу
            efficiency:
              type: string
              description: Ефективність
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Tilt angle updated successfully
      404:
        description: Tilt angle not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    tilt_angle = TiltAngle.create_from_dto(content)
    tilt_angle_controller.update(tilt_angle_id, tilt_angle)
    return make_response("Tilt angle updated", HTTPStatus.OK)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['PATCH'])
def patch_tilt_angle(tilt_angle_id: int) -> Response:
    """
    Partially update tilt angle
    ---
    tags:
      - Tilt Angles
    parameters:
      - name: tilt_angle_id
        in: path
        type: integer
        required: true
        description: ID кута нахилу
      - in: body
        name: body
        schema:
          type: object
          properties:
            angle:
              type: string
              description: Кут нахилу
            efficiency:
              type: string
              description: Ефективність
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Tilt angle updated successfully
      404:
        description: Tilt angle not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    tilt_angle_controller.patch(tilt_angle_id, content)
    return make_response("Tilt angle updated", HTTPStatus.OK)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['DELETE'])
def delete_tilt_angle(tilt_angle_id: int) -> Response:
    """
    Delete tilt angle
    ---
    tags:
      - Tilt Angles
    parameters:
      - name: tilt_angle_id
        in: path
        type: integer
        required: true
        description: ID кута нахилу
    responses:
      200:
        description: Tilt angle deleted successfully
      404:
        description: Tilt angle not found
    """
    tilt_angle_controller.delete(tilt_angle_id)
    return make_response("Tilt angle deleted", HTTPStatus.OK)
