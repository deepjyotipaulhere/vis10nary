from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_books():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="mysecretpassword")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route('/api/orders', methods=['POST'])
def create_order():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="mysecretpassword")
    cur = conn.cursor()
    data = request.get_json()
    cur.execute("INSERT INTO orders (book_id, user_id, amount) VALUES (%s, %s, %s)", (data['book_id'], data['user_id'], data['amount']))
    conn.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
  app.run(debug=True)