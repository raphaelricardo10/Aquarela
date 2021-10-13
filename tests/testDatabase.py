import unittest
from backend.flask.src.database import Database
from pymongo.errors import CollectionInvalid

class TestSalesRequestMethods(unittest.TestCase):

    def test_empty_db(self):
        self.assertEqual(Database().connection, None)

    def test_connection_ok(self):
        self.assertNotEqual(Database('sample_supplies').connection, None)

    def test_connection_failed(self):
        #It is needed to implement a network blocker method before
            with self.assertRaises(ConnectionError):
                Database('sample_supplies')
    
    def test_invalid_collection(self):
        with self.assertRaises(CollectionInvalid):
            Database('Invalid-name-15335413513')