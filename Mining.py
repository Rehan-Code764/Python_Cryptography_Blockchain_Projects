
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, difficulty, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_String = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}".encode()
        return hashlib.sha256(block_String).hexdigest()

    def mine_block(self):
        target = '0' * self.difficulty
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.generate_hash()
        print(f"Block mined:{self.hash} with nonce {self.nonce}")


class Blockchain:
    def __init__(self, difficulty, nonce=0):
        self.chain = [self.create_genesis_block(difficulty)]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self, difficulty):
        return Block(0, "0", time.time(), "GenesisBlock", difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block()
        self.chain.append(new_block)


bc = Blockchain(difficulty=4)

block1 = Block(
    1, "", time.time(),
    "Transaction 1:Rehan->Rohan",
    bc.difficulty
)
bc.add_block(block1)

block2 = Block(
    2, "", time.time(),
    "Transaction 2:Rohan->Muskan",
    bc.difficulty
)
bc.add_block(block2)

for block in bc.chain:
    print(f"Block {block.index}")
    print("Hash", block.hash)
    print("Previous_hash", block.previous_hash)
    print("Timestamp", block.timestamp)
    print("Data", block.data)
