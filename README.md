> This Repo is for my Blockchain independent study \
> and Study of the Bitcoin network

# CAP Theorem

- Consistency: All nodes have a consistent view of the data irrespective of where the client is connected to
- Availability: Ability to respond to requests from users at all time
- Partition Tolerance: Ability of system to continue operating even under a **network partition**

IF. a system suffers from network attack, it can prioritize either:

1. Availability but forgoes Consistency
2. Consistency but forgoes Availability

However, CAP theorem assumes ideal state of network and simple model of Consistency and Availability which is rare, no, never seen in real-world networks.

# Proof of Stake (PoS)

- Used by Ethereum, Solana etc.
- Energy Usage is very low compared to PoW
- Max scalability and efficiency

# Proof of Work (PoW)

- Used by Bitcoin
- Energy/resource usage is high as its directly tied to consensus
- Max security
- Potential issues: 51% attack,

## Process

1. First miner to find solution of the cryptographic puzzle, set by network, wins the right-to-add a new block to the network
2. Miner will receive newly minted BTC and transaction fees

Citations:

1. [CAP Theorem Simplified by ByteByteGo](https://youtu.be/BHqjEjzAicA)
2. [A Proof of Stake Overview By Pool of Stake](https://medium.com/@poolofstake/a-proof-of-stake-overview-445c52558d03)
3. 