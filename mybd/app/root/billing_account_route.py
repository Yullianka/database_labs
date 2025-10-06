from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import billing_account_controller
from ..domain.billing_account import BillingAccount

billing_account_bp = Blueprint('billing_account', __name__, url_prefix='/billing_account')


@billing_account_bp.route('', methods=['GET'])
def get_all_billing_accounts() -> Response:
    """
    Get all billing accounts
    ---
    tags:
      - Billing Accounts
    responses:
      200:
        description: List of all billing accounts
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID рахунку
              balance:
                type: string
                description: Баланс
              account_number:
                type: string
                description: Номер рахунку
    """
    return make_response(jsonify(billing_account_controller.find_all()), HTTPStatus.OK)


@billing_account_bp.route('', methods=['POST'])
def create_billing_account() -> Response:
    """
    Create a new billing account
    ---
    tags:
      - Billing Accounts
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            balance:
              type: string
              description: Баланс
            account_number:
              type: string
              description: Номер рахунку
    responses:
      201:
        description: Billing account created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            balance:
              type: string
            account_number:
              type: string
      400:
        description: Invalid input data
    """
    content = request.get_json()
    billing_account = BillingAccount.create_from_dto(content)
    billing_account_controller.create(billing_account)
    return make_response(jsonify(billing_account.put_into_dto()), HTTPStatus.CREATED)


@billing_account_bp.route('/<int:billing_account_id>', methods=['GET'])
def get_billing_account(billing_account_id: int) -> Response:
    """
    Get billing account by ID
    ---
    tags:
      - Billing Accounts
    parameters:
      - name: billing_account_id
        in: path
        type: integer
        required: true
        description: ID рахунку
    responses:
      200:
        description: Billing account details
        schema:
          type: object
          properties:
            id:
              type: integer
            balance:
              type: string
            account_number:
              type: string
      404:
        description: Billing account not found
    """
    return make_response(jsonify(billing_account_controller.find_by_id(billing_account_id)), HTTPStatus.OK)


@billing_account_bp.route('/<int:billing_account_id>', methods=['PUT'])
def update_billing_account(billing_account_id: int) -> Response:
    """
    Update billing account completely
    ---
    tags:
      - Billing Accounts
    parameters:
      - name: billing_account_id
        in: path
        type: integer
        required: true
        description: ID рахунку
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            balance:
              type: string
              description: Баланс
            account_number:
              type: string
              description: Номер рахунку
    responses:
      200:
        description: Billing account updated successfully
      404:
        description: Billing account not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    billing_account = BillingAccount.create_from_dto(content)
    billing_account_controller.update(billing_account_id, billing_account)
    return make_response("BillingAccount updated", HTTPStatus.OK)


@billing_account_bp.route('/<int:billing_account_id>', methods=['PATCH'])
def patch_billing_account(billing_account_id: int) -> Response:
    """
    Partially update billing account
    ---
    tags:
      - Billing Accounts
    parameters:
      - name: billing_account_id
        in: path
        type: integer
        required: true
        description: ID рахунку
      - in: body
        name: body
        schema:
          type: object
          properties:
            balance:
              type: string
              description: Баланс
            account_number:
              type: string
              description: Номер рахунку
    responses:
      200:
        description: Billing account updated successfully
      404:
        description: Billing account not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    billing_account_controller.patch(billing_account_id, content)
    return make_response("BillingAccount updated", HTTPStatus.OK)


@billing_account_bp.route('/<int:billing_account_id>', methods=['DELETE'])
def delete_billing_account(billing_account_id: int) -> Response:
    """
    Delete billing account
    ---
    tags:
      - Billing Accounts
    parameters:
      - name: billing_account_id
        in: path
        type: integer
        required: true
        description: ID рахунку
    responses:
      200:
        description: Billing account deleted successfully
      404:
        description: Billing account not found
    """
    billing_account_controller.delete(billing_account_id)
    return make_response("BillingAccount deleted", HTTPStatus.OK)
