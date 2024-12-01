from flask import Blueprint, request, jsonify
from app.services import add_transaction, spend_points, get_balances

api = Blueprint('api', __name__)

@api.route('/add', methods=['POST'])
def add():
    data = request.json
    add_transaction(data['payer'], data['points'], data['timestamp'])
    return '', 200

@api.route('/spend', methods=['POST'])
def spend():
    data = request.json
    result, status = spend_points(data['points'])
    return jsonify(result), status

@api.route('/balance', methods=['GET'])
def balance():
    return jsonify(get_balances()), 200