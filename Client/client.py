import requests
import os
import rsa

os.environ['NO_PROXY'] = '127.0.0.1'
publicKey = requests.get('http://127.0.0.1:5000/getkey')
k = publicKey.content
pubkey = k.replace(b'\\n', b'\n').decode('ascii')
pubkey = pubkey[1:] 
pubkey = pubkey[:-1]
k = rsa.PublicKey.load_pkcs1(pubkey)
loop = 'Y'

while (loop == 'Y'):
    print ("Enter message:\n")      #Take input from user to send to server
    message = input()
    encryptedMsg = rsa.encrypt(message.encode(), k)
    print ("Message sent:",encryptedMsg,'\n')       #Display the message being sent to server (encrypted)
    server = requests.post('http://127.0.0.1:5000/message', data = encryptedMsg)
    server = str(server.content)
    print (server[1:])
    print("\n Do you want to send another message? (Y/N)")
    loop = input().upper()