from sql_connection import get_sql_connection 
from datetime import datetime

def insert_order(connection, order):

    cursor = connection.cursor()
    query = ("INSERT INTO orders"
             "(customer_name, total, datetime)"
              "VALUES (%s, %s, %s)")
    data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(query, data)

    order_id = cursor.lastrowid
    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")
    order_details_data = []

    for i in order['order_details']:
        order_details_data.append([
            order_id,
            int(i['product_id']),
            float(i['quantity']),
            float(i['total_price'])
        ])

    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id 

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)

    response = []
    for (order_id, customer_name, total, datetime) in cursor:
        response.append({
            'order_id':order_id,
            'customer_name':customer_name,
            'total':total,
            'datetime':datetime
        })

    return response


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(insert_order(connection, {
    #     'customer_name': 'abcdegh',
    #     'grand_total': '1000',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 3,
    #             'quantity': 2,
    #             'total_price': 150
    #         },
    #         {
    #             'product_id': 10,
    #             'quantity': 2,
    #             'total_price':24 
    #         },

    #     ]
    # }))
    print(get_all_orders(connection))
          
















