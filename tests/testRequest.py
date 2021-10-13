import unittest
import requests
import json

class TestRequestMethods(unittest.TestCase):

    def test_wronginput(self):
        with open('./queries/wrongInput.json') as json_file:
            queries = json.load(json_file)
            url = 'http://127.0.0.1:5000/sales'

            for query in queries:
                with self.subTest(query=query):
                    response = requests.post(url, json=query)
                    self.assertNotEquals(response.status_code, 200)
