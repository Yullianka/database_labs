from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import household_controller
from ..domain.household import Household

household_bp = Blueprint('household', __name__, url_prefix='/household')


@household_bp.route('', methods=['GET'])
def get_all_households() -> Response:
    """
    Get all households
    ---
    tags:
      - Households
    responses:
      200:
        description: List of all households
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID домогосподарства
              address:
                type: string
                description: Адреса
              square_footage:
                type: string
                description: Площа
              energy_consumption:
                type: string
                description: Споживання енергії
    """
    return make_response(jsonify(household_controller.find_all()), HTTPStatus.OK)


@household_bp.route('', methods=['POST'])
def create_household() -> Response:
    """
    Create a new household
    ---
    tags:
      - Households
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
              description: Адреса
            square_footage:
              type: string
              description: Площа
            energy_consumption:
              type: string
              description: Споживання енергії
    responses:
      201:
        description: Household created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            address:
              type: string
            square_footage:
              type: string
            energy_consumption:
              type: string
      400:
        description: Invalid input data
    """
    content = request.get_json()
    household = Household.create_from_dto(content)
    household_controller.create(household)
    return make_response(jsonify(household.put_into_dto()), HTTPStatus.CREATED)


@household_bp.route('/<int:household_id>', methods=['GET'])
def get_household(household_id: int) -> Response:
    """
    Get household by ID
    ---
    tags:
      - Households
    parameters:
      - name: household_id
        in: path
        type: integer
        required: true
        description: ID домогосподарства
    responses:
      200:
        description: Household details
        schema:
          type: object
          properties:
            id:
              type: integer
            address:
              type: string
            square_footage:
              type: string
            energy_consumption:
              type: string
      404:
        description: Household not found
    """
    return make_response(jsonify(household_controller.find_by_id(household_id)), HTTPStatus.OK)


@household_bp.route('/<int:household_id>', methods=['PUT'])
def update_household(household_id: int) -> Response:
    """
    Update household completely
    ---
    tags:
      - Households
    parameters:
      - name: household_id
        in: path
        type: integer
        required: true
        description: ID домогосподарства
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            address:
              type: string
              description: Адреса
            square_footage:
              type: string
              description: Площа
            energy_consumption:
              type: string
              description: Споживання енергії
    responses:
      200:
        description: Household updated successfully
      404:
        description: Household not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    household = Household.create_from_dto(content)
    household_controller.update(household_id, household)
    return make_response("Household updated", HTTPStatus.OK)


@household_bp.route('/<int:household_id>', methods=['PATCH'])
def patch_household(household_id: int) -> Response:
    """
    Partially update household
    ---
    tags:
      - Households
    parameters:
      - name: household_id
        in: path
        type: integer
        required: true
        description: ID домогосподарства
      - in: body
        name: body
        schema:
          type: object
          properties:
            address:
              type: string
              description: Адреса
            square_footage:
              type: string
              description: Площа
            energy_consumption:
              type: string
              description: Споживання енергії
    responses:
      200:
        description: Household updated successfully
      404:
        description: Household not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    household_controller.patch(household_id, content)
    return make_response("Household updated", HTTPStatus.OK)


@household_bp.route('/<int:household_id>', methods=['DELETE'])
def delete_household(household_id: int) -> Response:
    """
    Delete household
    ---
    tags:
      - Households
    parameters:
      - name: household_id
        in: path
        type: integer
        required: true
        description: ID домогосподарства
    responses:
      200:
        description: Household deleted successfully
      404:
        description: Household not found
    """
    household_controller.delete(household_id)
    return make_response("Household deleted", HTTPStatus.OK)
