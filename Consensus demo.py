import random

# PoW Simulation
miners = [
    {'id': 'Miner1', 'power': random.randint(100, 500)},
    {'id': 'Miner2', 'power': random.randint(100, 500)},
    {'id': 'Miner3', 'power': random.randint(100, 500)},
]
pow_winner = max(miners, key=lambda m: m['power'])

print("=== Proof of Work (PoW) ===")
print(f"Miners: {miners}")
print("console.log('Selecting the miner with the highest computational power.')")
print(f"Selected Miner: {pow_winner['id']} with power {pow_winner['power']}")
print(f"Consensus Method Used: Proof of Work (PoW)\n")

# PoS Simulation
stakers = [
    {'id': 'Staker1', 'stake': random.randint(1000, 5000)},
    {'id': 'Staker2', 'stake': random.randint(1000, 5000)},
    {'id': 'Staker3', 'stake': random.randint(1000, 5000)},
]
pos_winner = max(stakers, key=lambda s: s['stake'])

print("=== Proof of Stake (PoS) ===")
print(f"Stakers: {stakers}")
print("console.log('Selecting the staker with the highest stake.')")
print(f"Selected Staker: {pos_winner['id']} with stake {pos_winner['stake']}")
print(f"Consensus Method Used: Proof of Stake (PoS)\n")

# DPoS Simulation
voters = ['Voter1', 'Voter2', 'Voter3']
delegates = {'X': 0, 'Y': 0, 'Z': 0}

for voter in voters:
    vote = random.choice(list(delegates.keys()))
    delegates[vote] += 1

dpos_winner = max(delegates, key=delegates.get)

print("=== Delegated Proof of Stake (DPoS) ===")
print(f"Voters: {voters}")
print(f"Delegate votes tally: {delegates}")
print("console.log('Selecting the delegate with the most votes from voters.')")
print(f"Selected Delegate: {dpos_winner} with {delegates[dpos_winner]} votes")
print(f"Consensus Method Used: Delegated Proof of Stake (DPoS)\n")
