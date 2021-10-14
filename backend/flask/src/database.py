import os
from pymongo import MongoClient

class Database:
    def __init__(self, dbName=None) -> None:
        self.connection = None
        if(dbName):
            try:
                self.connect(dbName)
            except:
                raise

    def connect(self, dbName: str) -> None:
        uri = "mongodb+srv://cluster0.uargx.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        certFile = os.path.abspath(__file__ + '/../../../') + '/X509-cert-6036829648392384800.pem'
        try:
            client = MongoClient(uri,
                                tls=True,
                                tlsCertificateKeyFile=certFile)
        except:
            raise ConnectionError

        self.connection = client[dbName]

        if dbName not in client.list_database_names():
            raise ValueError(f"ERROR: Database {dbName} not found!!!")
