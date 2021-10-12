from pymongo import MongoClient

class Database:
    def __init__(self, dbName=None) -> None:
        self.connection = None
        if(dbName):
            self.connect(dbName)

    def connect(self, dbName: str) -> None:
        uri = "mongodb+srv://cluster0.uargx.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        client = MongoClient(uri,
                            tls=True,
                            tlsCertificateKeyFile='/home/raphael/aquarela/backend/X509-cert-6036829648392384800.pem')

        self.connection = client[dbName]