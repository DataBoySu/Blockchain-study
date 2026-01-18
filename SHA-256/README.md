# SHA - Secure Hashing Algorithms

> [!NOTE]
> In this Repo, lets learn about SHA 256 hash function \
> Since understanding the cryptographic puzzle is paramount to understanding Blockchain

## SHA 1

- Released + Published in 1995
- Takes any length of string and outputs a **160-bit** value

### Implementation

1. Take a loop and chunk file down to 512 bits
2. Keep updating the internal state until files expended

If data is not a multiple of 512 bits, we need to pad it.

## SHA 3

Has hidden data that interacts with your data to give the output.

- Prevents Hash Length Extension Attack
- 
