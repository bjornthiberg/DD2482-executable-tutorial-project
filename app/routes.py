from flask import Blueprint, jsonify, render_template

api_bp = Blueprint('api', __name__)

@api_bp.route('/api', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Flask API!'})

@api_bp.route('/')
def index():
    return render_template('index.html')
