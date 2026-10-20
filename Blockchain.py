
import hashlib

def hashgenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

class block:
    def __init__(self, data, hash, pre_hash):
        self.data = data
        self.hash = hash
        self.pre_hash = pre_hash

class blockchain:
    def __init__(self):
        hashlast = hashgenerator('gen_last')
        hashstart = hashgenerator('gen_start')
        genesis = block('gen-data', hashstart, hashlast)
        self.chain = [genesis]

    def add_block(self, data):
        pre_hash = self.chain[-1].hash
        hash = hashgenerator(data + pre_hash)
        Block = block(data, hash, pre_hash)
        self.chain.append(Block)

bc = blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

for Block in bc.chain:
    print(Block.__dict__)
