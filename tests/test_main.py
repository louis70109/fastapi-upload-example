import io
import os
from pathlib import Path
import unittest
from _pytest.monkeypatch import MonkeyPatch
from mock import patch
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_upload():
    filename = 'requirements.txt'
    try:
        with open(filename, 'rb') as f:

            text = f.read()
            response = client.post("/upload", files={"files": (filename, text)})
            assert response.status_code == 200
            assert response.json() == {"message": "Successfully uploaded"}
    except:
        raise
    # data = {'files': [(io.StringIO('my file contents'), 'hello world.txt')]}
    # print(data)
    
    # assert response.json() == {"message": "Hello World!"}

# class TestClient(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def test_read_main(self):
#         response = client.get("/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"message": "Hello World!"})
