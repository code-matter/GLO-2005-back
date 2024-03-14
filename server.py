from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pymysql
from dotenv import load_dotenv
import os

# Configuration des variables d'environnement
load_dotenv()

# Configuration Flask
app = Flask(__name__)
CORS(app)

def db_connection():
    connection = None
    try:
        connection =  pymysql.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"),db=os.getenv("DB_NAME"))
    except pymysql.Error as e:
        print(e)
    return connection
        

@app.route('/')
def home():
    return "Home"

@app.route("/compagnons",methods=["GET","POST"])
def get_compagnons():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        query = "SELECT * FROM Compagnon"
        cursor.execute(query)
        compagnons = [
            dict(
            id = row[0],
            nom = row[1],
            prenom = row[2],
            age = row[3],
            email = row[4],
            password = row[5],
            description = row[6],
            evaluation = row[7],
            date_creation = row[8],
            date_modification = row[9],
            pays_id = row[10]
        ) for row in cursor.fetchall()
        ]
        if compagnons is not None:
            return jsonify(compagnons),200
        
    if request.method == "POST":
        data = request.get_json()
        tuples= tuple(data.keys())
        values = tuple(data.values())
        query = f"""INSERT INTO Compagnon ({", ".join(tuples)}) VALUES {values}"""
        cursor.execute(query)
        conn.commit()
        return jsonify('success'),200

if __name__ == "__main__":
    app.run(debug=True,threaded=True)