import pymysql
from dotenv import load_dotenv
import os

def createCompagnonTable():
    try:
        cursor = connection.cursor()
        req = """CREATE TABLE IF NOT EXISTS Compagnon (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nom char(50),
            prenom char(50),
            age integer,
            email char(50),
            password char(50),
            description longtext,
            evaluation double,
            date_creation timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_modification timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            pays_id integer NULL,
            FOREIGN KEY (pays_id)
            REFERENCES Pays(id)
        );
        """
        cursor.execute(req)
        cursor.close()
    except:
        print('Une erreure est survenue lors de la création de la table Compagnon')

def createRegionTable():
    try:
        cursor = connection.cursor()
        req = """CREATE TABLE IF NOT EXISTS Region (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nom char(50),
            date_creation timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_modification timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(req)
        cursor.close()
    except:
        print('Une erreure est survenue lors de la création de la table Region')

def createPaysTable():
    try:
        cursor = connection.cursor()
        req = """CREATE TABLE IF NOT EXISTS Pays (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            nom char(50),
            region_id integer NULL,
            devise char(5),
            date_creation timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_modification timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (region_id)
            REFERENCES Region(id)
        );
        """
        cursor.execute(req)
        cursor.close()
    except:
        print('Une erreure est survenue lors de la création de la table Pays')
def createPublicationTable():
    try:
        cursor = connection.cursor()
        req = """CREATE TABLE IF NOT EXISTS Publication (
            id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
            compagnon_id integer NULL,
            pays_id integer NULL,
            titre longtext,
            budget double,
            description longtext,
            date_creation timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_modification timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(compagnon_id)
            REFERENCES Compagnon(id),
            FOREIGN KEY(pays_id)
            REFERENCES Pays(id)
        );
        """
        cursor.execute(req)
        cursor.close()
    except:
        print('Une erreure est survenue lors de la création de la table Publication')

if __name__ == '__main__':
    # Configuration des variables d'environnement
    load_dotenv()

    # Connection à la BD
    connection = pymysql.connect(host=os.getenv("DB_HOST"),user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"), db=os.getenv('DB_NAME'))
    
    # Création des tables
    createRegionTable()
    print('Table Region créé')
    createPaysTable()
    print('Table Pays créé')
    createCompagnonTable()
    print('Table Compagnon créé')
    createPublicationTable()
    print('Table Publication créé')

    connection.close()
