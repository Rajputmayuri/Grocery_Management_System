

from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()


    query = ("SELECT products.Product_ID, Products.Product_Name, Products.UOM_ID, products.Price_Per_Unit, uom.UOM_Name FROM products INNER JOIN uom ON products.UOM_ID = uom.UOM_ID")
    cursor.execute(query)
    response=[]

    for (Product_ID, Product_Name, UOM_ID, Price_Per_Unit,UOM_Name) in cursor:
        response.append(
            {
                'Product_ID' : Product_ID,
                'Product_Name' : Product_Name,
                'UOM_ID' : UOM_ID,
                'Price_Per_Unit' : Price_Per_Unit,
                'UOM_Name' : UOM_Name
            }

            )
    return response
def insert_new_product(connection,products):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
         "(Product_Name, UOM_ID, Price_Per_Unit) "
         "VALUES (%s, %s, %s)")

    data =(products['Product_Name'], products['UOM_ID'], products['Price_Per_Unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, Product_ID):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE Product_ID =" + str(Product_ID))
    cursor.execute(query)
    connection.commit()


if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 7))
