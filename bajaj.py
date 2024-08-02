from flask import Flask, request, jsonify

app = Flask(__name__)

# POST method endpoint to process data
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Extracting data from the request
        data = request.json.get('data', [])
        
        # Separating numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Finding the highest alphabet (case insensitive)
        highest_alphabet = max(alphabets, key=str.lower) if alphabets else None

        # Response structure
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

# GET method endpoint to return operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
