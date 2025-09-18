from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="devopsdb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from Flask + MySQL!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
