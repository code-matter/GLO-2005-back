import pymysql
from dotenv import load_dotenv
import os

def createDatabase():
    try:
        connection = pymysql.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"))

        cursor = connection.cursor()
        create = """CREATE DATABASE IF NOT EXISTS compagnon;"""

        cursor.execute(create)
        cursor.close()

        connection.close()
    except:
        print('Une erreure est survenue lors de la création de la base de donnée')

if __name__ == '__main__':
    # Configuration des variables d'environnement
    load_dotenv()
    createDatabase()