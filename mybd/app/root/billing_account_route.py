from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import billing_account_controller
from ..domain.billing_account import BillingAccount, insert_billing_account

billing_account_bp = Blueprint('billing_account', __name__, url_prefix='/billing_account')

@billing_account_bp.route('/parametrized', methods=['POST'])
def insert_parametrized() -> Response:
    content = request.get_json()
    new_billing = insert_billing_account(
        balance=content['balance'],
        account_number=content['account_number']
    )
    return make_response(jsonify(new_billing.put_into_dto()), HTTPStatus.CREATED)


@billing_account_bp.route('', methods=['GET'])
def get_all_billing_accounts() -> Response:
    return make_response(jsonify(billing_account_controller.find_all()), HTTPStatus.OK)


@billing_account_bp.route('', methods=['POST'])
def create_billing_account() -> Response:
    content = request.get_json()
    billing_account = BillingAccount.create_from_dto(content)
    billing_account_controller.create(billing_account)
    return make_response(jsonify(billing_account.put_into_dto()), HTTPStatus.CREATED)


@billing_account_bp.route('/<int:billing_account_id>', methods=['GET'])
def get_billing_account(billing_account_id: int) -> Response:
    return make_response(jsonify(billing_account_controller.find_by_id(billing_account_id)), HTTPStatus.OK)


@billing_account_bp.route('/<int:billing_account_id>', methods=['PUT'])
def update_billing_account(billing_account_id: int) -> Response:
    content = request.get_json()
    billing_account = BillingAccount.create_from_dto(content)
    billing_account_controller.update(billing_account_id, billing_account)
    return make_response("BillingAccount updated", HTTPStatus.OK)


@billing_account_bp.route('/<int:billing_account_id>', methods=['PATCH'])
def patch_billing_account(billing_account_id: int) -> Response:
    content = request.get_json()
    billing_account_controller.patch(billing_account_id, content)
    return make_response("BillingAccount updated", HTTPStatus.OK)


@billing_account_bp.route('/<int:billing_account_id>', methods=['DELETE'])
def delete_billing_account(billing_account_id: int) -> Response:
    billing_account_controller.delete(billing_account_id)
    return make_response("BillingAccount deleted", HTTPStatus.OK)
