from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import energy_sale_controller
from ..domain.energy_sale import EnergySale, insert_energy_sales

energy_sale_bp = Blueprint('energy_sale', __name__, url_prefix='/energy_sale')


@energy_sale_bp.route('', methods=['GET'])
def get_all_energy_sales() -> Response:
    return make_response(jsonify(energy_sale_controller.find_all()), HTTPStatus.OK)


@energy_sale_bp.route('', methods=['POST'])
def create_energy_sale() -> Response:
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.create(energy_sale)
    return make_response(jsonify(energy_sale.put_into_dto()), HTTPStatus.CREATED)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['GET'])
def get_energy_sale(energy_sale_id: int) -> Response:
    return make_response(jsonify(energy_sale_controller.find_by_id(energy_sale_id)), HTTPStatus.OK)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['PUT'])
def update_energy_sale(energy_sale_id: int) -> Response:
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.update(energy_sale_id, energy_sale)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['PATCH'])
def patch_energy_sale(energy_sale_id: int) -> Response:
    content = request.get_json()
    energy_sale_controller.patch(energy_sale_id, content)
    return make_response("EnergySale create", HTTPStatus.OK)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['DELETE'])
def delete_energy_sale(energy_sale_id: int) -> Response:
    energy_sale_controller.delete(energy_sale_id)
    return make_response("EnergySale deleted", HTTPStatus.OK)

@energy_sale_bp.route('/auto_insert', methods=['POST'])
def auto_sales_create() -> Response | tuple[Response, int]:
    num_sales = request.args.get('amount')
    result = insert_energy_sales(int(num_sales))
    if result != -1:
        res = [sales.put_into_dto() for sales in result]
        return jsonify({"new_energy_sale": res})
    else:
        return jsonify({"error"}), 400