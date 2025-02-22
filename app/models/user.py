from app.database import get_db_connection

def create_user(name: str, email: str, password: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, password))
    connection.commit()
    user_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return user_id

def find_user_by_email(email: str):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user