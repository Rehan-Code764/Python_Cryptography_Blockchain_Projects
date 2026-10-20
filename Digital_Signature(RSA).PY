
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

# Generate private key
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign(message, private_key):
    message = bytes(str(message), 'utf-8')

    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature

def verify(message, sig, public_key):
    message = bytes(str(message), 'utf-8')
    try:
        public_key.verify(
            sig,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except Exception:
        print("error executing public key", Exception)
        return False

if __name__ == '__main__':
    pr, pu = generate_keys()
    pr1, pu1 = generate_keys()
    #print(pr)
    #print(pu)
    message = input("enter the message:-")
    sig = sign(message, pr)
    print("This a Digital Signature:-")
    print(sig)
    correct = verify(message, sig, pu)
    if correct:
        print(" Verify Successful")
    else:
        print("Failed")
