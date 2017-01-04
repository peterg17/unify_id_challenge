import requests
from Crypto.PublicKey import RSA
import base64
import string


if __name__=='__main__':
    #example URL: "https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new"
    # tried to create my own random number generator function to replace the one for the RSA object here http://pythonhosted.org/pycrypto/
    # used this documentation: http://pythonhosted.org/pycrypto/Crypto.PublicKey.RSA._RSAobj-class.html#encrypt

    def get_random(n):
        payload = {'num': str(n), 'min': '0', 'max': "100", 'col': '1', 'base': '10', 'format': 'plain', 'rnd':'new'}
        r = requests.get('https://www.random.org/integers', params=payload)
        response = r.text
        response = response.split("\n")
        response = "".join(response)
        mb = bytearray(response)
        return mb[:n]



    key = RSA.generate(2048, randfunc=get_random)
    f = open('mykey.pem','w')
    f.write(RSA.exportKey('PEM'))
    f.close()

    f = open('mykey.pem','r')
    key = RSA.importKey(f.read())

    plaintext = "i have a large pizza"
    cipher = key.encrypt(plaintext)
    print("cipher is", cipher)
    check = key.decrypt(cipher)
    print("plaintext should be (i have a large pizza)", check)

    with open("rsa_result.txt", "w") as f:
        f.write("cipher is:{} \n plaintext should be (i have a large pizza):{}".format(cipher,check))
