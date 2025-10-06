from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import energy_sale_controller
from ..domain.energy_sale import EnergySale

energy_sale_bp = Blueprint('energy_sale', __name__, url_prefix='/energy_sale')


@energy_sale_bp.route('', methods=['GET'])
def get_all_energy_sales() -> Response:
    """
    Get all energy sales
    ---
    tags:
      - Energy Sales
    responses:
      200:
        description: List of all energy sales
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID продажу
              timestamp:
                type: string
                format: date-time
                description: Час продажу
              energy_sold:
                type: string
                description: Продана енергія
              price_per_kw:
                type: string
                description: Ціна за кВт
              energy_selected:
                type: string
                description: Вибрана енергія
              solar_station_id:
                type: integer
                description: ID сонячної станції
    """
    return make_response(jsonify(energy_sale_controller.find_all()), HTTPStatus.OK)


@energy_sale_bp.route('', methods=['POST'])
def create_energy_sale() -> Response:
    """
    Create a new energy sale
    ---
    tags:
      - Energy Sales
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            timestamp:
              type: string
              format: date-time
              description: Час продажу
            energy_sold:
              type: string
              description: Продана енергія
            price_per_kw:
              type: string
              description: Ціна за кВт
            energy_selected:
              type: string
              description: Вибрана енергія
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      201:
        description: Energy sale created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            timestamp:
              type: string
              format: date-time
            energy_sold:
              type: string
            price_per_kw:
              type: string
            energy_selected:
              type: string
            solar_station_id:
              type: integer
      400:
        description: Invalid input data
    """
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.create(energy_sale)
    return make_response(jsonify(energy_sale.put_into_dto()), HTTPStatus.CREATED)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['GET'])
def get_energy_sale(energy_sale_id: int) -> Response:
    """
    Get energy sale by ID
    ---
    tags:
      - Energy Sales
    parameters:
      - name: energy_sale_id
        in: path
        type: integer
        required: true
        description: ID продажу енергії
    responses:
      200:
        description: Energy sale details
        schema:
          type: object
          properties:
            id:
              type: integer
            timestamp:
              type: string
              format: date-time
            energy_sold:
              type: string
            price_per_kw:
              type: string
            energy_selected:
              type: string
            solar_station_id:
              type: integer
      404:
        description: Energy sale not found
    """
    return make_response(jsonify(energy_sale_controller.find_by_id(energy_sale_id)), HTTPStatus.OK)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['PUT'])
def update_energy_sale(energy_sale_id: int) -> Response:
    """
    Update energy sale completely
    ---
    tags:
      - Energy Sales
    parameters:
      - name: energy_sale_id
        in: path
        type: integer
        required: true
        description: ID продажу енергії
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            timestamp:
              type: string
              format: date-time
              description: Час продажу
            energy_sold:
              type: string
              description: Продана енергія
            price_per_kw:
              type: string
              description: Ціна за кВт
            energy_selected:
              type: string
              description: Вибрана енергія
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Energy sale updated successfully
      404:
        description: Energy sale not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    energy_sale = EnergySale.create_from_dto(content)
    energy_sale_controller.update(energy_sale_id, energy_sale)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['PATCH'])
def patch_energy_sale(energy_sale_id: int) -> Response:
    """
    Partially update energy sale
    ---
    tags:
      - Energy Sales
    parameters:
      - name: energy_sale_id
        in: path
        type: integer
        required: true
        description: ID продажу енергії
      - in: body
        name: body
        schema:
          type: object
          properties:
            timestamp:
              type: string
              format: date-time
              description: Час продажу
            energy_sold:
              type: string
              description: Продана енергія
            price_per_kw:
              type: string
              description: Ціна за кВт
            energy_selected:
              type: string
              description: Вибрана енергія
            solar_station_id:
              type: integer
              description: ID сонячної станції
    responses:
      200:
        description: Energy sale updated successfully
      404:
        description: Energy sale not found
      400:
        description: Invalid input data
    """
    content = request.get_json()
    energy_sale_controller.patch(energy_sale_id, content)
    return make_response("EnergySale updated", HTTPStatus.OK)


@energy_sale_bp.route('/<int:energy_sale_id>', methods=['DELETE'])
def delete_energy_sale(energy_sale_id: int) -> Response:
    """
    Delete energy sale
    ---
    tags:
      - Energy Sales
    parameters:
      - name: energy_sale_id
        in: path
        type: integer
        required: true
        description: ID продажу енергії
    responses:
      200:
        description: Energy sale deleted successfully
      404:
        description: Energy sale not found
    """
    energy_sale_controller.delete(energy_sale_id)
    return make_response("EnergySale deleted", HTTPStatus.OK)
