from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import panel_controller
from ..domain.panel import Panel

panel_bp = Blueprint('panel', __name__, url_prefix='/panel')


@panel_bp.route('', methods=['GET'])
def get_all_panels() -> Response:
    """
    Get all panels
    ---
    tags:
      - Panels
    responses:
      200:
        description: List of all panels
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID панелі
              model:
                type: string
                description: Модель панелі
              efficiency:
                type: string
                description: Ефективність
              power_output:
                type: string
                description: Вихідна потужність
              solar_station_id:
                type: integer
                description: ID сонячної станції
    """
    return make_response(jsonify(panel_controller.find_all()), HTTPStatus.OK)


@panel_bp.route('', methods=['POST'])
def create_panel() -> Response:
    """
    Create a new panel
    ---
    tags:
      - Panels
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              description: Модель панелі
            efficiency:
              type: string
              description: Ефективність
            power_output:
              type: string
              description: Вихідна потужність
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      201:
        description: Panel created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            model:
              type: string
            efficiency:
              type: string
            power_output:
              type: string
            solar_station_id:
              type: integer
      400:
        description: Invalid input data
    """
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    panel_controller.create(panel)
    return make_response(jsonify(panel.put_into_dto()), HTTPStatus.CREATED)


@panel_bp.route('/<int:panel_id>', methods=['GET'])
def get_panel(panel_id: int) -> Response:
    """
    Get panel by ID
    ---
    tags:
      - Panels
    parameters:
      - name: panel_id
        in: path
        type: integer
        required: true
        description: ID панелі
    responses:
      200:
        description: Panel details
        schema:
          type: object
          properties:
            id:
              type: integer
            model:
              type: string
            efficiency:
              type: string
            power_output:
              type: string
            solar_station_id:
              type: integer
      404:
        description: Panel not found
    """
    return make_response(jsonify(panel_controller.find_by_id(panel_id)), HTTPStatus.OK)


@panel_bp.route('/<int:panel_id>', methods=['PUT'])
def update_panel(panel_id: int) -> Response:
    """
    Update panel completely
    ---
    tags:
      - Panels
    parameters:
      - name: panel_id
        in: path
        type: integer
        required: true
        description: ID панелі
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              description: Модель панелі
            efficiency:
              type: string
              description: Ефективність
            power_output:
              type: string
              description: Вихідна потужність
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Panel updated successfully
      404:
        description: Panel not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    panel_controller.update(panel_id, panel)
    return make_response("Panel updated", HTTPStatus.OK)


@panel_bp.route('/<int:panel_id>', methods=['PATCH'])
def patch_panel(panel_id: int) -> Response:
    """
    Partially update panel
    ---
    tags:
      - Panels
    parameters:
      - name: panel_id
        in: path
        type: integer
        required: true
        description: ID панелі
      - in: body
        name: body
        schema:
          type: object
          properties:
            model:
              type: string
              description: Модель панелі
            efficiency:
              type: string
              description: Ефективність
            power_output:
              type: string
              description: Вихідна потужність
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Panel updated successfully
      404:
        description: Panel not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    panel_controller.patch(panel_id, content)
    return make_response("Panel updated", HTTPStatus.OK)


@panel_bp.route('/<int:panel_id>', methods=['DELETE'])
def delete_panel(panel_id: int) -> Response:
    """
    Delete panel
    ---
    tags:
      - Panels
    parameters:
      - name: panel_id
        in: path
        type: integer
        required: true
        description: ID панелі
    responses:
      200:
        description: Panel deleted successfully
      404:
        description: Panel not found
    """
    panel_controller.delete(panel_id)
    return make_response("Panel deleted", HTTPStatus.OK)
