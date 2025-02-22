from app.database import get_db_connection

def create_product(name: str, price: float, seller_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO products (name, price, seller_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, price, seller_id))
    connection.commit()
    product_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return product_id

def fetch_products():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    connection.close()
    return products