import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

        # Simple Proof of Work: hash must start with '000'
        while not self.hash.startswith("000"):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def calculate_hash(self):
        input_str = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(input_str.encode()).hexdigest()

    def display(self):
        print(f"\n🔗 Block #{self.index}")
        print(f"Timestamp     : {self.timestamp}")
        print(f"Data          : {self.data}")
        print(f"Nonce         : {self.nonce}")
        print(f"Previous Hash : {self.previous_hash}")
        print(f"Hash          : {self.hash}")

# Build blockchain with 3 linked blocks
blockchain = []
genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

for i in range(1, 3):
    prev_block = blockchain[-1]
    new_block = Block(i, f"Block {i} Data", prev_block.hash)
    blockchain.append(new_block)

# Display all blocks
for block in blockchain:
    block.display()
# Tamper with Block 1 (index 1)
print("\n🔧 Tampering Block #1...")
blockchain[1].data = "Hacked Data"
blockchain[1].hash = blockchain[1].calculate_hash()

# Reprint all blocks to show effect
for block in blockchain:
    block.display()

# Validate chain integrity
print("\n🔍 Validating Blockchain Integrity...")
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]
        if current.previous_hash != previous.hash:
            print(f"❌ Block #{i} has invalid previous hash!")
            return False
        if current.hash != current.calculate_hash():
            print(f"❌ Block #{i} has invalid current hash!")
            return False
    print("✅ Blockchain is valid.")
    return True

is_chain_valid(blockchain)
