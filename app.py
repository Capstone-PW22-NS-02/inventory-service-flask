from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_pymongo import pymongo
import urllib.parse
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)


CONNECTION_STRING = 'mongodb+srv://suryamn:'+urllib.parse.quote_plus("qwerty@1234")+'@capstone.9nomawa.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('test')
product_collection = pymongo.collection.Collection(db,'products')



@app.route('/getProducts', methods=['GET'])
@cross_origin()
def getProducts():

    products = product_collection.find({})
    p = []
    for product in products:
        product['_id'] = str(product['_id'])
        p.append(product)
    # products = [product for product in products]
    return jsonify(p)
      

@app.route('/getProduct/<id>', methods=['GET'])
@cross_origin()
def getProduct(id):

    product = product_collection.find_one({"_id":ObjectId(id)})
    product['_id'] = str(product['_id'])
    return jsonify(product)


@app.route('/addProduct', methods=['POST'])
@cross_origin()
def addProduct():

    try:
        product = request.get_json()
        product_collection.insert_one(product)
        return jsonify({'msg':'Product added'})

    except Exception as e:
        return jsonify({'msg':e})


@app.route('/addReview', methods=['POST'])
@cross_origin()
def addReview():

    try:
        product = request.get_json()
        print(product)  
        product_collection.update_one({'_id':ObjectId(product['_id'])}, {"$set": {'reviews':product['reviews']}}, upsert=False)
        return jsonify({'msg':'Review added'})

    except Exception as e:
        return jsonify({'msg':e})

if __name__ == '__main__':
    app.run(port=8001, debug=True)