from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import panel_controller
from ..domain.panel import Panel

panel_bp = Blueprint('panel', __name__, url_prefix='/panel')


@panel_bp.route('', methods=['GET'])
def get_all_panels() -> Response:
    return make_response(jsonify(panel_controller.find_all()), HTTPStatus.OK)


@panel_bp.route('', methods=['POST'])
def create_panel() -> Response:
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    panel_controller.create(panel)
    return make_response(jsonify(panel.put_into_dto()), HTTPStatus.CREATED)


@panel_bp.route('/<int:panel_id>', methods=['GET'])
def get_panel(panel_id: int) -> Response:
    return make_response(jsonify(panel_controller.find_by_id(panel_id)), HTTPStatus.OK)


@panel_bp.route('/<int:panel_id>', methods=['PUT'])
def update_panel(panel_id: int) -> Response:
    content = request.get_json()
    panel = Panel.create_from_dto(content)
    panel_controller.update(panel_id, panel)
    return make_response("Panel updated", HTTPStatus.OK)


@panel_bp.route('/<int:panel_id>', methods=['PATCH'])
def patch_panel(panel_id: int) -> Response:
    content = request.get_json()
    panel_controller.patch(panel_id, content)
    return make_response("Panel updated", HTTPStatus.OK)


@panel_bp.route('/<int:panel_id>', methods=['DELETE'])
def delete_panel(panel_id: int) -> Response:
    panel_controller.delete(panel_id)
    return make_response("Panel deleted", HTTPStatus.OK)
