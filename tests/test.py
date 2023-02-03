import requests
import os
import rsa
import unittest

class TestMessage(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(message, server_response)


if __name__ == '__main__':

    os.environ['NO_PROXY'] = '127.0.0.1'
    publicKey = requests.get('http://127.0.0.1:5000/getkey')
    k = publicKey.content
    pubkey = k.replace(b'\\n', b'\n').decode('ascii')
    pubkey = pubkey[1:] 
    pubkey = pubkey[:-1]
    k = rsa.PublicKey.load_pkcs1(pubkey)

    message = "Test message. Anyone there?"
    encryptedMsg = rsa.encrypt(message.encode(), k)
    server = requests.post('http://127.0.0.1:5000/test', data = encryptedMsg)
    server_response = str(server.content)
    server_response = server_response[2:]
    server_response = server_response[:-1]

    unittest.main()