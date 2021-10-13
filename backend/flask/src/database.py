import os
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

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

        try:
            self.connection.validate_collection(dbName)
        except CollectionInvalid:
            raise
