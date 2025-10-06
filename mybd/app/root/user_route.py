from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import user_controller
from ..domain.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET'])
def get_all_users() -> Response:
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: List of all users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              contact_info:
                type: string
              amount_of_station:
                type: integer
              solar_station_id:
                type: integer
    """
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)

@user_bp.route('', methods=['POST'])
def create_user() -> Response:
    """
    Create a new user
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - contact_info
          properties:
            name:
              type: string
              description: Ім'я користувача
            contact_info:
              type: string
              description: Контактна інформація
            amount_of_station:
              type: integer
              description: Кількість станцій
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      201:
        description: User created successfully
      400:
        description: Invalid input data
    """
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> Response:
    """
    Get user by ID
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID користувача
    responses:
      200:
        description: User details
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            contact_info:
              type: string
            amount_of_station:
              type: integer
            solar_station_id:
              type: integer
      404:
        description: User not found
    """
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int) -> Response:
    """
    Update user completely
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          required:
            - name
            - contact_info
          properties:
            name:
              type: string
            contact_info:
              type: string
            amount_of_station:
              type: integer
            solar_station_id:
              type: integer
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=['PATCH'])
def patch_user(user_id: int) -> Response:
    """
    Partially update user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
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
            contact_info:
              type: string
            amount_of_station:
              type: integer
            solar_station_id:
              type: integer
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int) -> Response:
    """
    Delete user
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
