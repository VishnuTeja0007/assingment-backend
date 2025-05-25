from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/listings', methods=['GET'])
def get_listings():
    try:
        with open('listing.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
