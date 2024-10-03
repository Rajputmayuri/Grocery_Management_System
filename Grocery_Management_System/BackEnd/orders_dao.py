from sql_connection import get_sql_connection
from datetime import datetime


def insert_order(connection, orders):
    cursor = connection.cursor()

    # Insert into orders table
    order_query = ("INSERT INTO orders (Customer_Name, Total, Date_Time) "
                   "VALUES (%s, %s, %s)")
    order_data = (orders['Customer_Name'], orders['Total'], datetime.now())
    cursor.execute(order_query, order_data)

    # Get the last inserted Order_ID
    Order_ID = cursor.lastrowid

    # Insert into order_details table
    order_details_query = ("INSERT INTO order_details (Order_ID, Product_ID, Quantity, Total_Price) "
                           "VALUES (%s, %s, %s, %s)")

    # Prepare data for order_details table
    order_details_data = []
    for order_detail in orders['order_details']:
        order_details_data.append((
            Order_ID,  # Foreign key reference to the orders table
            order_detail['Product_ID'],
            order_detail['Quantity'],
            order_detail['Total_Price']
        ))

    # Insert multiple rows into order_details
    cursor.executemany(order_details_query, order_details_data)
    connection.commit()

    return Order_ID


def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []
    for (Order_ID, Customer_Name, Total, Date_Time) in cursor:
        response.append({
            'Order_ID': Order_ID,
            'Customer_Name': Customer_Name,
            'Total': Total,
            'datetime': dt
        })
    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders())
    # Example order data
    orders = {
        'Customer_Name': 'John Doe',
        'Total': 120.50,
        'order_details': [
            {
                'Product_ID': 5,
                'Quantity': 2,
                'Total_Price': 100.00
            },
            {
                'Product_ID': 6,
                'Quantity': 2,
                'Total_Price': 500.00
            }
        ]
    }

    new_order_id = insert_order(connection, orders)
    print(f"Order inserted with ID: {new_order_id}")

