
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

#Data to be signed
message = input("Enter the message:").encode()

signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)
print("ECC Digital Signature:-", signature.hex())

#verify the signature
try:
    public_key.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
    )
    print("Signature is valid")
except:
    print("Signature is invalid")
