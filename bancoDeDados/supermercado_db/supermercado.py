from pymongo import MongoClient, ReturnDocument

from database import Database
from helper.auto_increment import autoIncrement

db = Database(database="fetin", collection="supermercado")
dbCounters = Database(database="fetin", collection="counters")
lista_produtos = []
auto_increment = autoIncrement()


class Produtos:

    def __init__(self, database):
        self.db = database

    def createProduct(self, nome: str, quantidadePorUnidade: str, marca: str, quantidade: int, preco: float, tipo: str,
                      localizacao: str):

        try:
            produto_id = auto_increment.getNextSequence()
            res = self.db.collection.insert_one({
                "_id": produto_id,
                "nome": nome,
                "quantidadePorUnidade": quantidadePorUnidade,
                "marca": marca,
                "quantidade": quantidade,
                "preco": preco,
                "tipo": tipo,
                "localizacao": localizacao})
            print(f"Product added to the database with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while adding product: {e}")
            return None

    def searchProduct(self, search: str):
        regex_pattern = f'.*{search}.*'

        result = self.db.collection.find({
            '$or': [
                {'nome': {'$regex': regex_pattern, '$options': 'i'}},
                {'tipo': {'$regex': regex_pattern, '$options': 'i'}},
                {'marca': {'$regex': regex_pattern, '$options': 'i'}}
            ]
        })

        if result:
            return result

    def showAllProducts(self, search):
        if isinstance(search, int):
            result = self.db.collection.find({'_id': search})
        else:
            regex_pattern = f'${search}.*'
            result = self.db.collection.find({
                '$or': [
                    {'nome': {'$regex': regex_pattern, '$options': 'i'}},
                    {'tipo': {'$regex': regex_pattern, '$options': 'i'}},
                    {'marca': {'$regex': regex_pattern, '$options': 'i'}}
                ]
            })
        return result

        if result:
            return result

        return print('Produto não encontrado')

    def editProcuct(self, id: int, nome: str, quantidadePorUnidade: str, marca: str, quantidade: int, preco: float,
                    tipo: str, localizacao: str):
        try:
            res = self.db.collection.update_one({"_id": id}, {"$set": {
                "nome": nome,
                "quantidadePorUnidade": quantidadePorUnidade,
                "marca": marca,
                "quantidade": quantidade,
                "preco": preco,
                "tipo": tipo,
                "localizacao": localizacao}})
            print(f"Procuct updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating product: {e}")
            return None
