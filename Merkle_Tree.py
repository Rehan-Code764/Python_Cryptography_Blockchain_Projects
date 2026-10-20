
import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def create_merkle_tree(transaction):
    leaf_hashes = [hash_data(tx) for tx in transaction]

    while len(leaf_hashes) > 1:
        if len(leaf_hashes) % 2 != 0:
            leaf_hashes.append(leaf_hashes[-1])

        leaf_hashes = [
            hash_data(leaf_hashes[i] + leaf_hashes[i+1])
            for i in range(0, len(leaf_hashes), 2)
        ]

    return leaf_hashes[0]

transaction = []
s = int(input("enter the transaction:-"))

for i in range(s):
    tx = input(f"Enter transaction {i+1}:")
    transaction.append(tx)

merkle_root = create_merkle_tree(transaction)

print("merkle root:-", merkle_root)
