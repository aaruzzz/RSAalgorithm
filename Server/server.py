from flask import Flask
from flask import request
import rsa
import jsonpickle

app = Flask(__name__)

@app.route("/")
def key_generation():
    try:
        privatefile = open("private.pem", "r")
        publicfile = open("public.pem", "r")
        return "<p>Status OK!</p>"
    except:
        privatefile = open("private.pem", "w")
        publicfile = open("public.pem", "w")
        publicKey, privateKey = rsa.newkeys(2048)
        publicKeyPkcs1PEM = publicKey.save_pkcs1().decode('utf8')
        privateKeyPkcs1PEM = privateKey.save_pkcs1().decode('utf8')
        privatefile.write(privateKeyPkcs1PEM)
        publicfile.write(publicKeyPkcs1PEM)
        return "<p>Status OK!</p>"


@app.route("/message",methods=['POST'])
def message():
    privatefile = open("private.pem", "r")
    privateKey = rsa.PrivateKey.load_pkcs1(privatefile.read())
    message = request.data
    print (message)
    decryptMessage = rsa.decrypt(message, privateKey).decode()
    print("decrypted string: ", decryptMessage)
    response = "Message received by server"
    return (response)

@app.route("/getkey")
def getkey():
    publicfile = open("public.pem", "r")
    response = publicfile.read()
    return jsonpickle.encode(response)

@app.route("/test",methods=['POST'])
def test():
    privatefile = open("private.pem", "r")
    privateKey = rsa.PrivateKey.load_pkcs1(privatefile.read())
    message = request.data
    print (message)
    decryptMessage = rsa.decrypt(message, privateKey).decode()
    print("decrypted string: ", decryptMessage)
    return decryptMessage

if __name__ == "__main__":
    app.run(debug=True ,port=8080,use_reloader=False)