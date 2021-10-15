import os
from pymongo import MongoClient

class Database:
    def __init__(self, dbName=None) -> None:
        self.connection = None
        #connect to the database
        if(dbName):
            try:
                self.connect(dbName)
            except:
                raise

    def connect(self, dbName: str) -> None:

        #Uri of the MongoDB cloud server
        uri = "mongodb+srv://cluster0.uargx.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

        #Path of the certificate file to connect to the server
        certFile = os.path.abspath(__file__ + '/../../../') + '/X509-cert-6036829648392384800.pem'

        #Try to connect or raise a error
        try:
            client = MongoClient(uri,
                                tls=True,
                                tlsCertificateKeyFile=certFile)
        except:
            raise ConnectionError

        #Check if the database exists
        if dbName not in client.list_database_names():
            raise ValueError(f"ERROR: Database {dbName} not found!!!")

        #Stores the connection object
        self.connection = client[dbName]