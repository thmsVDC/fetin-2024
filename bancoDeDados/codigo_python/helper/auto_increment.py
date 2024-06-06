from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # substitua pelo seu URI de conexão
db = client.fetin  # substitua pelo nome do seu banco de dados
counters = db.counters


class autoIncrement():
    def getNextSequence(self):
        ret = counters.find_one_and_update(
            {"_id": "cont"},
            {"$inc": {"seq": 1}},
            return_document=True
        )

        return ret['seq']