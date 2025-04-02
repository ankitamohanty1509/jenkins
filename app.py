from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Smartphone", "price": 600},
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
