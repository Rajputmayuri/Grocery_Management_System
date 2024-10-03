from flask import Flask, request, jsonify

from BackEnd import orders_dao
from sql_connection import get_sql_connection
import Products_dao
import uom_dao
import json

app = Flask(__name__)
connection = get_sql_connection()


@app.route('/getproducts', methods=['GET'])
def get_products():
    products = Products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    Product_ID = Products_dao.insert_product(connection, request_payload)
    response = jsonify({
        'Product_ID': Product_ID
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertorder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    Order_ID = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'Order_ID': Order_ID
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = Products_dao.delete_product(connection, request.form['Product_ID'])
    response = jsonify({
        'Product_ID': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python Flask server for Grocery Store Management System")
    app.run(port=5000)
