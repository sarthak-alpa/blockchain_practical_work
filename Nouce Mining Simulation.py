# mining_simulation.py

import hashlib
import time

class Block:
    def __init__(self, data):
        self.timestamp = time.time()
        self.data = data
        self.nonce = 0
        self.hash = ''

    def mine_block(self, difficulty):
        prefix = '0' * difficulty  # Target: hash must start with '0000' if difficulty=4
        print(f"⛏️ Mining block with difficulty {difficulty}...")

        start = time.time()

        while True:
            input_string = f"{self.timestamp}{self.data}{self.nonce}"
            self.hash = hashlib.sha256(input_string.encode()).hexdigest()

            if self.hash.startswith(prefix):
                break
            self.nonce += 1

        end = time.time()
        duration = round(end - start, 2)

        print(f"✅ Mined Block!")
        print(f"🔑 Nonce       : {self.nonce}")
        print(f"🔗 Hash        : {self.hash}")
        print(f"⏱️ Time Taken : {duration} seconds")

# Run Example
if __name__ == "__main__":
    block = Block("Test Mining")
    block.mine_block(difficulty=4)
