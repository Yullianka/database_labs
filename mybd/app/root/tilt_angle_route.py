from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller import tilt_angle_controller
from ..domain.tilt_angle import TiltAngle

tilt_angle_bp = Blueprint('tilt_angle', __name__, url_prefix='/tilt_angle')


@tilt_angle_bp.route('', methods=['GET'])
def get_all_tilt_angles() -> Response:
    return make_response(jsonify(tilt_angle_controller.find_all()), HTTPStatus.OK)


@tilt_angle_bp.route('', methods=['POST'])
def create_tilt_angle() -> Response:
    content = request.get_json()
    tilt_angle = TiltAngle.create_from_dto(content)
    tilt_angle_controller.create(tilt_angle)
    return make_response(jsonify(tilt_angle.put_into_dto()), HTTPStatus.CREATED)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['GET'])
def get_tilt_angle(tilt_angle_id: int) -> Response:
    return make_response(jsonify(tilt_angle_controller.find_by_id(tilt_angle_id)), HTTPStatus.OK)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['PUT'])
def update_tilt_angle(tilt_angle_id: int) -> Response:
    content = request.get_json()
    tilt_angle = TiltAngle.create_from_dto(content)
    tilt_angle_controller.update(tilt_angle_id, tilt_angle)
    return make_response("TiltAngle updated", HTTPStatus.OK)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['PATCH'])
def patch_tilt_angle(tilt_angle_id: int) -> Response:
    content = request.get_json()
    tilt_angle_controller.patch(tilt_angle_id, content)
    return make_response("TiltAngle updated", HTTPStatus.OK)


@tilt_angle_bp.route('/<int:tilt_angle_id>', methods=['DELETE'])
def delete_tilt_angle(tilt_angle_id: int) -> Response:
    tilt_angle_controller.delete(tilt_angle_id)
    return make_response("TiltAngle deleted", HTTPStatus.OK)
