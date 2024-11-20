from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import household_controller
from ..domain.household import Household

household_bp = Blueprint('household', __name__, url_prefix='/household')


@household_bp.route('', methods=['GET'])
def get_all_households() -> Response:
    return make_response(jsonify(household_controller.find_all()), HTTPStatus.OK)


@household_bp.route('', methods=['POST'])
def create_household() -> Response:
    content = request.get_json()
    household = Household.create_from_dto(content)
    household_controller.create(household)
    return make_response(jsonify(household.put_into_dto()), HTTPStatus.CREATED)


@household_bp.route('/<int:household_id>', methods=['GET'])
def get_household(household_id: int) -> Response:
    return make_response(jsonify(household_controller.find_by_id(household_id)), HTTPStatus.OK)


@household_bp.route('/<int:household_id>', methods=['PUT'])
def update_household(household_id: int) -> Response:
    content = request.get_json()
    household = Household.create_from_dto(content)
    household_controller.update(household_id, household)
    return make_response("Household updated", HTTPStatus.OK)


@household_bp.route('/<int:household_id>', methods=['PATCH'])
def patch_household(household_id: int) -> Response:
    content = request.get_json()
    household_controller.patch(household_id, content)
    return make_response("Household updated", HTTPStatus.OK)


@household_bp.route('/<int:household_id>', methods=['DELETE'])
def delete_household(household_id: int) -> Response:
    household_controller.delete(household_id)
    return make_response("Household deleted", HTTPStatus.OK)
