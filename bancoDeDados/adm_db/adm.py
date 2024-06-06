from pymongo import MongoClient, ReturnDocument

from database import Database

db = Database(database="fetin", collection="adm")


class ADMs:

    def __init__(self, database):
        self.db = database

    def createADM(self, nome: str, senha: str):
        try:
            res = self.db.collection.insert_one({
                "nome": nome,
                "senha": senha})
            print(f"ADM added to the database with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while adding ADM: {e}")
            return None