import unittest
import requests
import json
import os

class TestRequestMethods(unittest.TestCase):

    def test_wronginput(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + "/queries/wrongInput.json") as json_file:
            queries = json.load(json_file)
            url = 'http://127.0.0.1:5000/sales'

            for query in queries:
                with self.subTest(query=query):
                    response = requests.post(url, json=query)
                    print(response.content)
                    self.assertEqual(response.status_code, 400)