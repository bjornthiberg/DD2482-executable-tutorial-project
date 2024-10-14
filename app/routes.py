from flask import Blueprint, jsonify, render_template

api_bp = Blueprint('api', __name__)

@api_bp.route('/api', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from Flask API!'})

@api_bp.route('/spoon', methods=['GET'])
def get_spoon():
    return jsonify({
'1': """ ,adPPYba, 8b,dPPYba,   ,adPPYba,   ,adPPYba,  8b,dPPYba, """,
'2': """ I8[    '' 88P'    '8a a8'     '8a a8'     '8a 88P'   `'8a""",
'3': """  `'Y8ba,  88       d8 8b       d8 8b       d8 88       88""",
'4': """ aa    ]8I 88b,   ,a8' '8a,   ,a8' '8a,   ,a8' 88       88""",
'5': """ `'YbbdP'' 88`YbbdP''   `'YbbdP''   `'YbbdP''  88       88""",
'6': """           88                                             """,
'7': """           88                                             """, 
'8': """                is the greatest Java analyser in the world"""
})
