
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for (UOM_ID, UOM_Name) in cursor:
        response.append({
            'UOM_ID': UOM_ID,
            'UOM_Name': UOM_Name
        })
    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))
