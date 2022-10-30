from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/getProducts', methods=['POST', 'GET'])
def index():
    if(request.method == 'GET'):
        products = [{
            "name": "Apple Macbook Pro",
            "description": "M1 chip, Retina display, 120Hz refresh rate",
            "price": 90000.0,
            "rating": 5
        }, {
            "name": "Asus Vivobook",
            "description": "8GB RAM, 256GB SSD + 1TB HDD",
            "price": 70000.0,
            "rating": 5
        }, ]
        return jsonify({'products': products})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
