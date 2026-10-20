
import hashlib

def generate_sha256_hash(data):
    sha256 = hashlib.sha256(data.encode()).hexdigest
    return sha256

data = input("enter thr data:")
hash_value = generate_sha256_hash(data)

print("the sha256 of", data, "is:-", hash_value)
